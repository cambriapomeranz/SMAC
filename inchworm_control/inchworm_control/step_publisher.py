#!/usr/bin/env python3
import rclpy
import os
from rclpy.node import Node
from std_msgs.msg import Float32, String  # or whatever message type you need
# import sys
# sys.path.append("~/MQP/dev_ws/src/inchworm_control/block_simulation")
# import minecraft_sim

class StepPublisher(Node):
    def __init__(self):
        super().__init__('step_publisher')
        self.publisher_ = self.create_publisher(String, 'motor_command', 10)
        # subscription to receive when a step is completed
        self.subscription = self.create_subscription(
            Float32,
            'motor_status',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.get_logger().info('Node starting')

        # get list of steps from block_simulation
        # self.steps =  minecraft_sim.complete_steps
        self.file_path = '~/MQP/dev_ws/src/inchworm_control/block_simulation/steps.txt'
        self.file_path = os.path.expanduser(self.file_path)
        # file_path = rclpy.get_param('~file_path', '~/MQP/dev_ws/src/inchworm_control/block_simulation/steps.txt')

        # Read from file
        self.steps = read_file_callback(self)

        print('steps FROM STEP_PUBLISHER', self.steps)
    
    def listener_callback(self, msg):
        step_status = msg.data
        self.get_logger().info('Received step status "%s' % msg.data)
        print('steps when recieved a msg: ', self.steps)
        try:
            if msg.data == 0.0:
                self.get_logger().info("movement complete")
                # steps is a list of tuples like (<step type>, holding_block)
                # if holding block is true, it is holding a block for this step
                #TODO: have it publish entire tuple
                step = self.steps.pop(0)[0]
                self.publisher_.publish(step)
                self.get_logger().info('Publishing: "%s"' % msg.data)
            elif msg.data == 1.0:
                self.get_logger().info("movement error")

        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))
 	
def read_file_callback(self):
        try:
            with open(self.file_path, 'r') as file:
                file_content = file.read()
                return file_content
        except Exception as e:
            self.get_logger().error('Failed to read file: %s', str(e))
    
def main(args=None):
    rclpy.init(args=args)
    step_publisher = StepPublisher()
    rclpy.spin(step_publisher)
    step_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
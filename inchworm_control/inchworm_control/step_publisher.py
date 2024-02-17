#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String  # or whatever message type you need
# import block_sim
# from ..block_simulation.path_conversion import path_getter
# from block_simulation.path_conversion import path_getter
import sys
# sys.path.append("/block_simulation/path_conversion")
sys.path.append("~/MQP/dev_ws/src/inchworm_control/block_simulation")
import path_conversion


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
        steps = path_conversion.step_getter()

        print('steps',steps)


    
    def listener_callback(self, msg):
        step_status = msg.data
        self.get_logger().info('Received step status "%s' % msg.data)

        try:
            if msg.data == 'complete':
                self.get_logger().info("movement complete")
                # steps is a list of tuples like (<step type>, holding_block)
                # if holding block is true, it is holding a block for this step
                #TODO: have it publish entire tuple
                step = steps.pop(0)[0]
                self.publisher_.publish(step)
                self.get_logger().info('Publishing: "%s"' % msg.data)
            elif msg.data == 'error':
                self.get_logger().info("movement error")

        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))
 	
def main(args=None):
    rclpy.init(args=args)
    step_publisher = StepPublisher()
    rclpy.spin(step_publisher)
    step_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
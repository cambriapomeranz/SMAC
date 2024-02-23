#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String  # or whatever message type you need
from inchworm_control.msg import Thruple

class MotorWalking(Node):
    def __init__(self):
        super().__init__('motor_walking')
        self.publisher_ = self.create_publisher(String, 'motor_command', 10)
        timer_period = 3  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.step = -1
        self.get_logger().info('Node starting')

    def timer_callback(self):
        # Home motors to step 0 position
        if self.step == -1:  
            msg = String()
            msg.data = "STEP_LEFT"
            # msg.data = "step_left"
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)

            self.step = 10 
        	
def main(args=None):
    rclpy.init(args=args)
    motor_walking = MotorWalking()
    rclpy.spin(motor_walking)
    motor_walking.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # or whatever message type you need
from inchworm_control.msg import Thruple

# this script is our first attempt at walking
# it will home the robot into step 0, then publish msgs to move to step 1 then 2
class MotorWalking(Node):
    def __init__(self):
        super().__init__('motor_walking')
        self.publisher_ = self.create_publisher(Thruple, 'motor_command', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.step = -1

    def timer_callback(self):
        self.get_logger().info('Node starting')

        # Home motors to step 0 position
        if self.step == -1:  
            msg = Thruple()
            msg.motor1 = 30.0
            msg.motor2 = 60.0
            msg.motor3 = 90.0
            self.publisher_.publish(msg)
            # self.get_logger().info('Publishing: "%s"' % msg.data)
            self.get_logger().info('Publishing: "%s, %s, %s"' % (msg.motor1, msg.motor2, msg.motor3))
            self.step = 0 
        # Move from step 0 to step 1
        elif self.step == 0:
            msg = Thruple()
            msg.motor1 = 60.0
            msg.motor2 = 60.0
            msg.motor3 = 90.0
            self.publisher_.publish(msg)
            # self.get_logger().info('Publishing: "%s"' % msg.data)
            self.get_logger().info('Publishing: "%s, %s, %s"' % (msg.motor1, msg.motor2, msg.motor3))
            self.step = 1  # Update the instance variable, not a local variable
        # Move from step 1 to step 2
        elif self.step == 1:
            msg = Thruple()
            msg.motor1 = 90.0
            msg.motor2 = 60.0
            msg.motor3 = 90.0
            self.publisher_.publish(msg)
            # self.get_logger().info('Publishing: "%s"' % msg.data)
            self.get_logger().info('Publishing: "%s, %s, %s"' % (msg.motor1, msg.motor2, msg.motor3))
            self.step = 2  # Update the instance variable, not a local variable
        	
def main(args=None):
    rclpy.init(args=args)
    motor_walking = MotorWalking()
    rclpy.spin(motor_walking)
    motor_walking.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import sys
import os

from inchworm_control.lewansoul_servo_bus import ServoBus
from time import sleep 

class MotorController(Node):

    def __init__(self):
        super().__init__('motor_controller')
        self.publisher_ = self.create_publisher(Float32, 'motor_status', 10)
        self.subscription = self.create_subscription(
            Float32,
            'motor_command',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Initialize your servo bus here
        # /dev/ttyUSB0 is for Cambria's laptop
        self.servo_bus = ServoBus('/dev/ttyUSB0')  # Adjust your port
        self.get_logger().info('Node starting')

    def listener_callback(self, msg):
        # Extract the target position from the message
        target_position = msg.data
        self.get_logger().info('Received command to move to position: "%f"' % target_position)

        try:
            servo_id = 2  
            servo_id2 = 3
            servo_id3 = 4

            servo_1 = self.servo_bus.get_servo(servo_id)
            servo_2 = self.servo_bus.get_servo(servo_id2)
            servo_3 = self.servo_bus.get_servo(servo_id3)

            time_to_move = 1.0  

            # send command 
            servo_1.move_time_write(172.08, time_to_move)
            servo_2.move_time_write(202.08, time_to_move)
            servo_3.move_time_write(65.28, time_to_move)

            sleep(3)

            servo_1.move_time_write(152.40, time_to_move)
            servo_2.move_time_write(221.40, time_to_move)
            servo_3.move_time_write(30.00, time_to_move)

            

            
            sleep(5)

            # Optionally, read back the position to confirm
            current_position = servo_1.pos_read()
            self.get_logger().info('Motor 2 Moved to position: "%f"' % current_position)
            current_position2 = servo_2.pos_read()
            self.get_logger().info('Motor 3 Moved to position: "%f"' % current_position2)
            current_position3 = servo_3.pos_read()
            self.get_logger().info('Motor 4 Moved to position: "%f"' % current_position3)
            
            # Publish the status
            status_message = Float32()
            status_message.data = current_position
            self.publisher_.publish(status_message)

        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))



def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import sys
import os

# for servo
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

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
        # /de is port of RP
        self.servo_bus = ServoBus('/dev/ttyUSB0')  # Adjust your port
        self.get_logger().info('Node starting')

        servo1.start(0)

    def listener_callback(self, msg):
        # Extract the target position from the message
        target_position = msg.data
        self.get_logger().info('Received command to move to position: "%f"' % target_position)

        try:
            angle = 0
            # command to move servo, angle of 180 is open, 0 closed
            servo1.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            # [v, w, x, yself, z]

            self.get_logger().info('trying rn:')

            servo_id = 2  
            servo_id2 = 3
            servo_id3 = 4

            servo_1 = self.servo_bus.get_servo(servo_id)
            servo_2 = self.servo_bus.get_servo(servo_id2)
            servo_3 = self.servo_bus.get_servo(servo_id3)

            time_to_move = 1.0  

            # send command 
            servo_1.move_time_write(-0.24, time_to_move)
            servo_2.move_time_write(141.60, time_to_move)
            servo_3.move_time_write(39.84, time_to_move)

            sleep(3)

            servo_1.move_time_write(20.88, time_to_move)
            servo_2.move_time_write(147.84, time_to_move)
            servo_3.move_time_write(67.20, time_to_move)

            

            
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


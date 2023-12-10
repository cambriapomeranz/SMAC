#!/usr/bin/env python3
from inchworm_control.ik import inverseKinematicsMQP
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
servo2 = GPIO.PWM(13,50) # pin 11 for servo1, pulse 50Hz

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
        servo2.start(0)

    def listener_callback(self, msg):
        # Extract the target position from the message
        target_position = msg.data
        self.get_logger().info('Received command to move to position: "%f"' % target_position)

        try:
            servo_id1 = 1 
            servo_id2 = 2  
            servo_id3 = 3
            servo_id4 = 4
            # MOTOR CANNOT GO NEGATIVE  
            servo_1 = self.servo_bus.get_servo(servo_id1)
            servo_2 = self.servo_bus.get_servo(servo_id2)
            servo_3 = self.servo_bus.get_servo(servo_id3)
            servo_4 = self.servo_bus.get_servo(servo_id4)

            time_to_move = 2.0  
            # servo angle of 180 is open, 0 closed
            angleOpen = 180
            angleClose = 0

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,2,1)
            theta4 += 20

            servo1.ChangeDutyCycle(2+(angleClose/18))
            servo2.ChangeDutyCycle(2+(angleOpen/18))
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            servo2.ChangeDutyCycle(0)

            servo_1.move_time_write(theta1, time_to_move)
            servo_2.move_time_write(theta2, time_to_move)
            servo_3.move_time_write(theta3, time_to_move)
            servo_4.move_time_write(theta4, time_to_move)
            
            sleep(2)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,3,1)

            servo_1.move_time_write(theta1, time_to_move)
            servo_2.move_time_write(theta2, time_to_move)
            servo_3.move_time_write(theta3, time_to_move)
            servo_4.move_time_write(theta4, time_to_move)
            
            sleep(4)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,0,1)

            servo_1.move_time_write(theta1, time_to_move)
            servo_2.move_time_write(theta2, time_to_move)
            servo_3.move_time_write(theta3, time_to_move)
            servo_4.move_time_write(theta4, time_to_move)
            
            sleep(4)

            servo2.ChangeDutyCycle(2+(angleClose/18))
            servo1.ChangeDutyCycle(2+(angleOpen/18))
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            servo2.ChangeDutyCycle(0)
    
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,3,5)

            servo_1.move_time_write(theta1, time_to_move)
            servo_2.move_time_write(theta2, time_to_move)
            servo_3.move_time_write(theta3, time_to_move)
            servo_4.move_time_write(theta4, time_to_move)
            
            sleep(4)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,0,5)

            servo_1.move_time_write(theta1, time_to_move)
            servo_2.move_time_write(theta2, time_to_move)
            servo_3.move_time_write(theta3, time_to_move)
            servo_4.move_time_write(theta4, time_to_move)
            
            sleep(4)

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


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

        self.servo_bus = ServoBus('/dev/ttyUSB0')  # /dev/ttyUSB0 is port for Cambria and RP
        self.get_logger().info('Node starting')

        # init servos
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
        servo2 = GPIO.PWM(13,50) # pin 11 for servo1, pulse 50Hz
        servo1.start(0)
        servo2.start(0)

        # MOTOR CANNOT GO NEGATIVE  
        motor_1 = self.servo_bus.get_servo(1)
        motor_2 = self.servo_bus.get_servo(2)
        motor_3 = self.servo_bus.get_servo(3)
        motor_4 = self.servo_bus.get_servo(4)

        time_to_move = 2.0  

    def listener_callback(self, msg):
        target_position = msg.data
        self.get_logger().info('Received command to move to position: "%f"' % target_position)

        try:
            activate_servo(self.servo_1)
            release_servo(self.servo_2)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,2,1)
            theta4 += 20
            move_to(theta1, theta2, theta3, theta4, theta5)
            move_to(inverseKinematicsMQP(6,0,3,1))
            move_to(inverseKinematicsMQP(6,0,0,1))

            activate_servo(self.servo_2)
            release_servo(self.servo_1)

            move_to(inverseKinematicsMQP(6,0,3,5))
            move_to(inverseKinematicsMQP(3,0,0,5))
                    
        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))


# servo angle of 180 is open, 0 closed
def activate_servo(servo_id):
    servo_id.ChangeDutyCycle(2+(180/18))
    time.sleep(0.5)
    servo_id.ChangeDutyCycle(0)

def release_servo(servo_id):
    servo_id.ChangeDutyCycle(2+(0/18))
    time.sleep(0.5)
    servo_id.ChangeDutyCycle(0)

def move_to(self, theta1, theta2, theta3, theta4, theta5):
    self.motor_1.move_time_write(theta1, self.time_to_move)
    self.motor_2.move_time_write(theta2, self.time_to_move)
    self.motor_3.move_time_write(theta3, self.time_to_move)
    self.motor_4.move_time_write(theta4, self.time_to_move)
    sleep(2)

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


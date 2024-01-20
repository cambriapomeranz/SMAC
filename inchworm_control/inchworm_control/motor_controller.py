#!/usr/bin/env python3
from inchworm_control.ik import inverseKinematicsMQP
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from inchworm_control.scripts.movement_command import *

import sys
import os

# for servo
# import RPi.GPIO as GPIO
# import time
# servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
# servo2 = GPIO.PWM(13,50) # pin 13 for servo1, pulse 50Hz

from inchworm_control.lewansoul_servo_bus import ServoBus
from time import sleep 

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.publisher_ = self.create_publisher(Float32, 'motor_status', 10)
        self.subscription = self.create_subscription(
            String,
            'motor_command',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.servo_bus = ServoBus('/dev/ttyUSB0')  # /dev/ttyUSB0 is port for RP /dev/ttylUSB0 or USB1 for cambria(switches randomly)
        self.get_logger().info('Node starting')

        # init motors
        init_motors(self)

        # init servos
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(11,GPIO.OUT)
        # GPIO.setup(13,GPIO.OUT)
        
        # servo1.start(0)
        # servo2.start(0)

        # MOTOR CANNOT GO NEGATIVE  
        
        # self.motor_1 = self.servo_bus.get_servo(1)
        # self.motor_2 = self.servo_bus.get_servo(2)
        # self.motor_3 = self.servo_bus.get_servo(3)
        # self.motor_4 = self.servo_bus.get_servo(4)
        # self.motor_5 = self.servo_bus.get_servo(5)

        # self.time_to_move = 2.0  

    def listener_callback(self, msg):
        target_position = msg.data
        self.get_logger().info('Received command to "%s' % msg.data)

        try:
            # initial motor configs
            #print(self.motor_1.pos_read(), self.motor_2.pos_read(), self.motor_3.pos_read(), self.motor_4.pos_read(), self.motor_5.pos_read())
           
            if msg.data == 'step_forward':
                step_forward(self)
            elif msg.data == 'turn_left':
                turn_left(self)
                    
        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))


# servo angle of 180 is activated, 0 released
def activate_servo(servo_id):
    servo_id.ChangeDutyCycle(2+(180/18))
    time.sleep(0.5)
    servo_id.ChangeDutyCycle(0)

def release_servo(servo_id):
    servo_id.ChangeDutyCycle(2+(0/18))
    time.sleep(0.5)
    servo_id.ChangeDutyCycle(0)

def move_to(self, theta1, theta2, theta3, theta4):
    # print(theta1, theta2, theta3, theta4, theta5)
    self.motor_1.move_time_write(theta1, self.time_to_move)
    self.motor_2.move_time_write(theta2, self.time_to_move)
    self.motor_3.move_time_write(theta3, self.time_to_move)
    self.motor_4.move_time_write(theta4, self.time_to_move)
    # self.motor_5.move_time_write(theta5, self.time_to_move)

    sleep(2)

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
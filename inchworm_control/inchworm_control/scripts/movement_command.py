#!/usr/bin/env python3
from inchworm_control.lewansoul_servo_bus import ServoBus
from inchworm_control.ik import inverseKinematicsMQP
from time import sleep 

def init_motors(self):
    self.motor_1 = self.servo_bus.get_servo(1)
    self.motor_2 = self.servo_bus.get_servo(2)
    self.motor_3 = self.servo_bus.get_servo(3)
    self.motor_4 = self.servo_bus.get_servo(4)
    self.motor_5 = self.servo_bus.get_servo(5)

    self.time_to_move = 2

def move_to(self, theta1, theta2, theta3, theta4):
    # print(theta1, theta2, theta3, theta4, theta5)
    self.motor_1.move_time_write(theta1, self.time_to_move)
    self.motor_2.move_time_write(theta2, self.time_to_move)
    self.motor_3.move_time_write(theta3, self.time_to_move)
    self.motor_4.move_time_write(theta4, self.time_to_move)
    # self.motor_5.move_time_write(theta5, self.time_to_move)

    sleep(2)

def step_forward(self):
    print('stepping forward')
    theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,2,1)
    theta4 += 40
    move_to(self, theta1, theta2, theta3, theta4)

    theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,3,1)
    theta4 += 20
    move_to(self, theta1, theta2, theta3, theta4)

    theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,0,1)
    theta4 += 20
    move_to(self, theta1, theta2, theta3, theta4)

def turn_left(self):
    print('stepping left')
    theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,3,1)
    theta4 += 50
    move_to(self, theta1, theta2, theta3, theta4)

    theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,5,2,1)
    move_to(self, theta1, theta2, theta3, theta4)

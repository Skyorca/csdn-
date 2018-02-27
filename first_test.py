#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:26:44 2018

@author: u6614921
"""
 # you should open your folder in the air and then go down to close for an obj

import robot

robot.init()

def move():
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    
def swap_left_mid():
    robot.drive_right()
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    move()

def swap_right_mid():
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_open()
    
    
def swap_right_left():
    swap_left_mid()
    swap_right_mid()
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_closed()
    move()
    
    
swap_right_left()


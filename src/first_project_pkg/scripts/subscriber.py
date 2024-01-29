#!/usr/bin/env python3
import time
import busio
import board
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import UInt16MultiArray

class PCA():

    def __init__(self):
        self.i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.pca = PCA9685(self.i2c_bus)
        self.pca.frequency = 50

    def microToDuty(self, value):
        return int(((value / 20000) * 0xFFFF) + 130)

    def servo(self, channel_number, value):
        self.pca.channels[channel_number].duty_cycle = self.microToDuty(value)

def callback(data, pca):
    rospy.loginfo("Received gripper positions: %s", data.data)
    
    if len(data.data) == 2:
        pca.servo(6, data.data[0])
        pca.servo(7, data.data[1])
    else:
        rospy.logwarn("Received invalid gripper positions. Expected 2 positions.")

def gripper_node():
    rospy.init_node('gripper_node', anonymous=True)
    pca = PCA()

    # Create a subscriber for receiving gripper positions
    rospy.Subscriber("gripper_positions_msg", UInt16MultiArray, callback, pca)

    rospy.spin()

if __name__ == '__main__':
    try:
        gripper_node()
    except rospy.ROSInterruptException:
        pass


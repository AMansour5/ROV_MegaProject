#!/usr/bin/env python3
import time
import busio
import board
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import UInt16MultiArray
from first_project_pkg.msg import joy

class PCA():

    def __init__(self):
        self.i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.pca = PCA9685(self.i2c_bus)
        self.pca.frequency = 50
        self.sub = rospy.Subscriber("webtoros", joy, self.callback)
        self.value = 0

    def microToDuty(self, value):
        return int(((value / 20000) * 0xFFFF) + 130)

    def servo(self, channel_number, value):
        self.pca.channels[channel_number].duty_cycle = self.microToDuty(value)

    def callback(self, data):
 #       rospy.loginfo("Received joystick data: %s", data)

        if data.button_index == 6:
            self.value += 1  # Adjust the increment as needed
            pca.servo(6, 350)
            pca.servo(7,19500)
        elif data.button_index == 7:
            self.value -= 1  # Adjust the decrement as needed
            pca.servo(7, 350)
            pca.servo(6,19500)
        else:
            pca.servo(7,350)
            pca.servo(6,350)
#            rospy.logwarn("Received invalid button index. Expected 6 or 7.")

        # Use self.value to perform any actions based on the updated value

def gripper_node():
    rospy.init_node('gripper_node', anonymous=True)
    pca = PCA()

    # Create a subscriber for receiving joystick data
    rospy.spin()

if __name__ == '__main__':
    while not rospy.is_shutdown():
        pca = PCA()
        try:
            gripper_node()
        except rospy.ROSInterruptException:
            pass


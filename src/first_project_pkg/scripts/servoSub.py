#!/usr/bin/env python3
import time
import board
import busio
from adafruit_pca9685 import PCA9685
import rospy
from std_msgs.msg import Int32
from first_project_pkg.msg import joy

class PCA():
   def __init__(self):
       self.i2c = busio.I2C(board.SCL, board.SDA)
       self.pca = PCA9685(self.i2c)
       self.pca.frequency = 50
       self.sub = rospy.Subscriber('webtoros',joy, self.callback)
       self.value = 1500

   def microToDuty(self,value):
       return int(((value/20000)*0xFFFF)+130)

   def servo (self,channel_number,value):
       self.pca.channels[channel_number].duty_cycle = self.microToDuty(value)

   def callback(self, data):
       if data.button_index == 11 and self.value<2000:
           self.value += 10
       elif data.button_index == 10 and self.value>1000:
           self.value -= 10
       self.servo(9,self.value)

if __name__ == '__main__':
   rospy.init_node('servo_joy', anonymous=False)
   pca = PCA()
   try:
       rospy.spin()
   except KeyboardInterrupt:
       pass


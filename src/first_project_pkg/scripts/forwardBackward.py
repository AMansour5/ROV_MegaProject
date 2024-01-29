#!/usr/bin/env python3
import time
import busio
import board
from adafruit_pca9685 import PCA9685
import rospy
#from std_msgs.msg import Float64
from first_project_pkg.msg import joy

class PCA():
  def __init__(self):
      self.i2c_bus = busio.I2C(board.SCL, board.SDA)
      self.pca = PCA9685(self.i2c_bus)
      self.pca.frequency = 50
      self.sub = rospy.Subscriber("webtoros", joy ,self.callback)
#     self.sub = rospy.Subscriber('Thrusters_command', Float64, self.callback)

  def microToDuty(self,value):
      return int(((value/20000)*0xFFFF)+130)

  def Thrusters (self,channel_number,value):
      self.pca.channels[channel_number].duty_cycle = self.microToDuty(value)

  def map_values(self, x):
     # Define the input and output ranges
        input_range = [-1, 1]
        output_range = [1100, 1900]

        # Calculate the ratio of the output range to the input range
        ratio = (output_range[1] - output_range[0]) / (input_range[1] - input_range[0])

        # Calculate the new value
        new_value = x * ratio + output_range[0] - input_range[0] * ratio
        return new_value

  def callback(self, data):

      value = self.map_values(data.y)
      pca.Thrusters(11,value)
      pca.Thrusters(12,value)
      pca.Thrusters(14,value)
      pca.Thrusters(15,value)

if __name__ == '__main__':
  rospy.init_node('servo_controller', anonymous=False)
  pca = PCA()
  try:
      pca.Thrusters(11,1500)
      pca.Thrusters(12,1500)
      pca.Thrusters(14,1500)
      pca.Thrusters(15,1500)
      time.sleep(3)
      rospy.spin()

  except KeyboardInterrupt:
      pass

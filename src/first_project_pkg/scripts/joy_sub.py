#!/usr/bin/env python3
import rospy
from first_project_pkg.msg import joy

def callback(data):
    rospy.loginfo("Pressed Button: %d",data.button_index)
    rospy.loginfo("X-axis: %f",data.x)
    rospy.loginfo("Y-axis: %f",data.y)
    rospy.loginfo("Z-axis: %f",data.z)
    rospy.loginfo("Yaw: %f",data.yaw)
    rospy.loginfo("Pitch: %f",data.pitch)
"""
    if data.button_index == 0:
    if data.button_index == 1:
    if data.button_index == 2:
    if data.button_index == 3:
    if data.button_index == 4:
    if data.button_index == 5:
    if data.button_index == 6:
    if data.button_index == 7:
    if data.button_index == 8:
    if data.button_index == 9:
    if data.button_index == 10:
    if data.button_index == 11:

"""

def subscribe_to_sensor_data():
    rospy.init_node("joystick_subscriber" , anonymous=False)
    rospy.Subscriber("webtoros", joy ,callback)

if __name__ == '__main__':
    try:
        subscribe_to_sensor_data()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

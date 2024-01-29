#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16MultiArray
import time

def gripper_publisher():
    rospy.init_node('gripper_publisher', anonymous=True)
    gripper_pub = rospy.Publisher('gripper_positions_msg', UInt16MultiArray, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        gripper_positions = [350, 350]  # Modify this list with your desired positions
        rospy.loginfo("Publishing gripper positions: %s", gripper_positions)
        
        gripper_positions_msg = UInt16MultiArray(data=gripper_positions)
        gripper_pub.publish(gripper_positions_msg)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        gripper_publisher()
    except rospy.ROSInterruptException:
        pass


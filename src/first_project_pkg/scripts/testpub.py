#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64


def talker():
 pub = rospy.Publisher('Thrusters_command', Float64, queue_size=10)
 rospy.init_node('talker', anonymous=True)
 rate = rospy.Rate(10) # 10hz
 while not rospy.is_shutdown():
       hello_int = 0.6
       rospy.loginfo(hello_int)
       pub.publish(hello_int)
       rate.sleep()

if __name__ == '__main__':
 try:
     talker()
 except rospy.ROSInterruptException:
     pass

#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def show_hiragana(msg):
    print("sub: " + msg.data)


if __name__ == "__main__":
    rospy.init_node("led_sub")
    sub = rospy.Subscriber('MorsePulse', String, show_hiragana)
    rospy.spin()

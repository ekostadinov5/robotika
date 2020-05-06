#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_name() + "I received: %s" % data.data)


def student():
    rospy.init_node("student", anonymous=True)
    rospy.Subscriber("notify", String, callback)
    rospy.spin()


if __name__ == "__main__":
    student()

#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def faculty():
    pub = rospy.Publisher('notify', String)

    rospy.init_node('faculty')

    while not rospy.is_shutdown():
        str = "Hello student, greetings from FINKI %s" % rospy.get_time()

        rospy.loginfo("Sending: %s" % str)

        pub.publish(String(str))

        rospy.sleep(1.0)


if __name__ == "__main__":
    try:
        faculty()
    except rospy.ROSInterruptException:
        pass

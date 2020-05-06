#!/usr/bin/env python

import rospy
from robotika.msg import AirPollution
import random


def get_pollution_message():
    id = 14
    location = "Kisela Voda"
    pm10 = 55 + random.random() * 10
    co = 25 + random.random() * 40

    msg = AirPollution(id=id, location=location, pm10=pm10, co=co)
    return msg


def sensor():
    pub = rospy.Publisher("pollution_data", AirPollution, queue_size=10)

    rospy.init_node("sensor")

    while not rospy.is_shutdown():
        msg = get_pollution_message()

        str = "Sending info from %s" % msg.location
        rospy.loginfo(str)

        pub.publish(msg)

        rospy.sleep(5.0)


if __name__ == "__main__":
    try:
        sensor()
    except rospy.ROSInterruptException:
        pass

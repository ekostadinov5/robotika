#!/usr/bin/env python

import rospy
from robotika.msg import AirPollution


def callback(data):
    rospy.loginfo(rospy.get_name() + " I received:\n"
                                     "ID: {0}\n"
                                     "Location: {1}\n"
                                     "PM10: {2}\n"
                                     "CO: {3}"
                  .format(data.id, data.location, data.pm10, data.co))


def client():
    rospy.init_node("client", anonymous=True)
    rospy.Subscriber("pollution_data", AirPollution, callback)
    rospy.spin()


if __name__ == "__main__":
    client()

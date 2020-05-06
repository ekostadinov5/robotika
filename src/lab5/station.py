#!/usr/bin/env python

import rospy
from robotika.msg import AirPollution
from robotika.srv import AlertService


cnt_alert = 0
ALERT_THRESH = 60
CNT_THRESH = 3


def send_request(data):
    rospy.wait_for_service("alert_service")

    try:
        rospy.loginfo("Sending request.")
        service = rospy.ServiceProxy("alert_service", AlertService)
        response = service(data)
        rospy.loginfo("Service response: {}".format(response.response_string))
    except rospy.ServiceException as e:
        print("Service access failed: %s" % e)


def callback(data):
    global cnt_alert

    rospy.loginfo(rospy.get_name() + " I received:\n"
                                     "ID: {0}\n"
                                     "Location: {1}\n"
                                     "PM10: {2}\n"
                                     "CO: {3}"
                  .format(data.id, data.location, data.pm10, data.co))

    cnt_alert = ((cnt_alert + 1) if data.pm10 > ALERT_THRESH else 0)

    if cnt_alert == CNT_THRESH:
        send_request(data)
        cnt_alert = 0


def client():
    rospy.init_node("client", anonymous=True)
    rospy.Subscriber("pollution_data", AirPollution, callback)
    rospy.spin()


if __name__ == "__main__":
    client()

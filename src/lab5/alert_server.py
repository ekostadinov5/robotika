#!/usr/bin/env python

import rospy
from robotika.srv import AlertService
from robotika.srv import AlertServiceResponse
import time


def write_to_db(location, pm10):
    rospy.loginfo("Writing to DB: " + location + " " + str(pm10))
    # Write to db
    time.sleep(2)
    return True


def email_users():
    rospy.loginfo("Emailing users.")
    # Email all users for pollution
    time.sleep(2)
    return True


def handle_request(request):
    pollution = request.pollution

    write_to_db(pollution.location, pollution.pm10)
    email_users()

    return AlertServiceResponse("Alert successfully served.")


def create_alert_service():
    rospy.init_node("alert_server")
    rospy.Service("alert_service", AlertService, handle_request)
    rospy.spin()


if __name__ == "__main__":
    create_alert_service()

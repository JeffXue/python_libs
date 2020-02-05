#!/usr/bin/env python3.7

import datetime


def datetime_earlier(d, hours=0, days=0):
    time_delta = datetime.timedelta(hours=hours, days=days)
    day = d - time_delta
    date_to = datetime.datetime(day.year, day.month, day.day,
                                day.hour, day.minute, day.second)
    return date_to


def datetime_later(d, hours=0, days=0):
    time_delta = datetime.timedelta(hours=hours, days=days)
    day = d + time_delta
    date_to = datetime.datetime(day.year, day.month, day.day,
                                day.hour, day.minute, day.second)
    return date_to


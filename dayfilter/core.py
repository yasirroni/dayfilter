import pytz
from suntime import Sun
from datetime import timezone, timedelta

# TODO:
# 1. No need to make sr and ss if we already have the data
# 2. Reimplement suntime.Sun() for speed and because it use LGPL License

def are_nights(ds, latitude, longitude, time_zone, ceil_sr=False, floor_sr=False, ceil_ss=False, floor_ss=False):
    sun = Sun(latitude, longitude)
    tz = timezone(timedelta(hours=time_zone))
    return [_is_night(ds_, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss) for ds_ in ds]

def is_night(ds, latitude, longitude, time_zone, ceil_sr=False, floor_sr=False, ceil_ss=False, floor_ss=False):
    sun = Sun(latitude, longitude)
    tz = timezone(timedelta(hours=time_zone))
    return _is_night(ds, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss)

def _is_night(ds, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss):
    sr, ss = get_sr_ss(ds, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss)
    if sr <= ds < ss:
        return False
    else:
        return True

def are_noons(ds, latitude, longitude, time_zone, ceil_sr=False, floor_sr=False, ceil_ss=False, floor_ss=False):
    sun = Sun(latitude, longitude)
    tz = timezone(timedelta(hours=time_zone))
    return [_is_noon(ds_, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss) for ds_ in ds]

def is_noon(ds, latitude, longitude, time_zone, ceil_sr=False, floor_sr=False, ceil_ss=False, floor_ss=False):
    sun = Sun(latitude, longitude)
    tz = timezone(timedelta(hours=time_zone))
    return _is_noon(ds, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss)

def _is_noon(ds, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss):
    sr, ss = get_sr_ss(ds, sun, tz, ceil_sr, floor_sr, ceil_ss, floor_ss)
    if sr <= ds < ss:
        return True
    else:
        return False

def get_sr_ss(ds_, sun, tz, ceil_sr=False, floor_sr=False, ceil_ss=False, floor_ss=False):
    # sr and ss have precision up to minute, thus ceil and floor only on hour
    sr = sun.get_sunrise_time(ds_).astimezone(tz).replace(tzinfo=None)
    ss = sun.get_sunset_time(ds_).astimezone(tz).replace(tzinfo=None)
    if ceil_sr:
        sr = ceil_date_hour(sr)
    elif floor_sr:
        sr = floor_date_hour(sr)
    if ceil_ss:
        ss = ceil_date_hour(ss)
    elif floor_ss:
        ss = floor_date_hour(ss)
    return sr, ss

def ceil_date_hour(dt):
    # sr and ss have precision up to minute, thus ceil and floor only on hour
    return floor_date_hour(dt) + timedelta(hours=1)

def floor_date_hour(dt):
    # sr and ss have precision up to minute, thus ceil and floor only on hour
    return dt.replace(minute=0)

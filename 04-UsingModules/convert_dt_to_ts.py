import time

def dt_to_ts(dt):
    return time.mktime(dt.timetuple())

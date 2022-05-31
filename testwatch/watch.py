import math
import time

from testwatch import store


def current_time():
    return math.floor(time.time())


def last_time():
    return store.last_entry().timestamp

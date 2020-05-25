from testwatch import store

import math
import time


def current_time():
    return math.floor(time.time())


def last_time():
    return store.last_entry()[0]

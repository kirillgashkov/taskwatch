import math
import time

from testwatch import store


def current_time() -> int:
    return math.floor(time.time())


def last_time() -> int:
    return store.last_entry().timestamp

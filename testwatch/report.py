#
# Task
#


class Task:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def duration(self):
        return self.end_time - self.start_time


def _make_task_from_entry(entry, task_start):
    return Task(entry.content, task_start, entry.timestamp)

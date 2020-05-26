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


#
# Report
#


class Report:
    def __init__(self, tasks, start_time, end_time):
        self.tasks = tasks
        self.start_time = start_time
        self.end_time = end_time

    def total_time_spent(self):
        return self.end_time - self.start_time

    def time_spent_on_starting(self):
        return self.tasks[0].start_time - self.start_time

    def time_spent_on_ending(self):
        return self.end_time - self.tasks[-1].end_time

    def time_spent_on_tasks(self):
        time = 0

        for task in self.tasks:
            time += task.duration()

        return time

    def time_spent_on_breaks(self):
        time = self.total_time_spent()

        time -= self.time_spent_on_starting()
        time -= self.time_spent_on_ending()
        time -= self.time_spent_on_tasks()

        return time

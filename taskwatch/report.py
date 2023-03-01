from taskwatch import store
from taskwatch.store import Entry


#
# Task
#


class Task:
    def __init__(self, name: str, start_time: int, end_time: int) -> None:
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def duration(self) -> int:
        return self.end_time - self.start_time


def _make_task_from_entry(entry: Entry, task_start: int) -> Task:
    return Task(entry.content, task_start, entry.timestamp)


#
# Report
#


class Report:
    def __init__(self, tasks: list[Task], start_time: int, end_time: int) -> None:
        self.tasks = tasks
        self.start_time = start_time
        self.end_time = end_time

    def total_time_spent(self) -> int:
        return self.end_time - self.start_time

    def time_spent_on_starting(self) -> int:
        if not self.tasks:
            return 0

        return self.tasks[0].start_time - self.start_time

    def time_spent_on_ending(self) -> int:
        if not self.tasks:
            return self.end_time - self.start_time

        return self.end_time - self.tasks[-1].end_time

    def time_spent_on_tasks(self) -> int:
        time = 0

        for task in self.tasks:
            time += task.duration()

        return time

    def time_spent_on_breaks(self) -> int:
        time = self.total_time_spent()

        time -= self.time_spent_on_starting()
        time -= self.time_spent_on_ending()
        time -= self.time_spent_on_tasks()

        return time


def make_report() -> Report:
    tasks: list[Task] = []
    start_time = -1
    end_time = -1

    last_time = -1
    for entry in store.entries():
        if entry.type == "start":
            start_time = entry.timestamp

        if entry.type == "end":
            end_time = entry.timestamp

        if entry.type == "amend":
            task = tasks.pop()
            last_time = task.start_time

        if entry.type in {"record", "amend"} and entry.content != "break":
            task = _make_task_from_entry(entry, last_time)
            tasks.append(task)

        last_time = entry.timestamp

    return Report(tasks, start_time, end_time)

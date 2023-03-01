import os
from collections.abc import Iterable

from taskwatch import io, report

SESSION_FILE = ".taskwatch_session"


#
# Entry
#


class Entry:
    def __init__(self, timestamp: int, entry_type: str, entry_content: str) -> None:
        self.timestamp = timestamp
        self.type = entry_type
        self.content = entry_content


def _make_entry_from_line(s: str) -> Entry:
    timestamp, entry_type, entry_content = s.split("\t")
    return Entry(int(timestamp), entry_type, entry_content.strip())


def _make_line_from_entry(entry: Entry) -> str:
    return f"{entry.timestamp}\t{entry.type}\t{entry.content}"


#
# Init
#


def init() -> None:
    if os.path.exists(SESSION_FILE):
        io.info("Session file is detected.")

        first_line, last_line = _get_first_and_last_lines(SESSION_FILE)

        if not first_line:
            return

        first_entry = _make_entry_from_line(first_line)
        last_entry = _make_entry_from_line(last_line)

        if last_entry.type == "end":
            io.info("Last session has ended.")

            if io.confirm("Would you like to see its report and exit? [y/n]"):
                io.print_report(report.make_report())
                exit()
            else:
                io.info("Archived last session file.")
                _archive_session_file(first_entry)
        else:
            _set_last_entry(last_entry)
            io.info("Loaded last session file.")


def _get_first_and_last_lines(file: str) -> tuple[str, str]:
    with open(file) as f:
        first_line = f.readline().rstrip("\n")
        last_line = first_line

        for line in f:
            last_line = line

    return first_line, last_line


def _archive_session_file(first_entry: Entry) -> None:
    archived_session_file = f"{SESSION_FILE}_{first_entry.timestamp}"
    os.rename(SESSION_FILE, archived_session_file)


#
# Add entry
#


def add_entry(timestamp: int, entry_type: str, entry_content: str) -> None:
    if "\t" in entry_content:
        io.error(
            "Tabs are not allowed in entry's content. Last entry was not registered."
        )
        return

    entry = Entry(timestamp, entry_type, entry_content)

    with open(SESSION_FILE, "a") as f:
        line = _make_line_from_entry(entry)
        f.write(f"{line}\n")

    _set_last_entry(entry)


#
# Last entry
#


_last_entry = Entry(-1, "", "")


def last_entry() -> Entry:
    return _last_entry


def _set_last_entry(entry: Entry) -> None:
    global _last_entry
    _last_entry = entry


#
# Entries
#


def entries() -> Iterable[Entry]:
    with open(SESSION_FILE) as f:
        for line in f:
            yield _make_entry_from_line(line)

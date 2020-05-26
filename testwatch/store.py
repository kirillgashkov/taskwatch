import os

from testwatch import io


SESSION_FILE = '.testwatch_session'


#
# Entry
#


class Entry:
    def __init__(self, timestamp, entry_type, entry_content):
        self.timestamp = timestamp
        self.type = entry_type
        self.content = entry_content


def _make_entry_from_line(s):
    timestamp, entry_type, entry_content = s.split('\t')
    return Entry(timestamp, entry_type, entry_content)


def _make_line_from_entry(entry):
    return f'{entry.timestamp}\t{entry.type}\t{entry.content}'


#
# Init
#


def init():
    if os.path.exists(SESSION_FILE):
        io.info('Session file is detected.')

        first_line, last_line = _get_first_and_last_lines(SESSION_FILE)

        if not first_line:
            return

        first_entry_ = _make_entry_from_line(first_line)
        last_entry_ = _make_entry_from_line(last_line)

        if last_entry_.type == 'end':
            _make_session_file_complete(first_entry_)
            io.info('Complete session file is created.')
        else:
            _set_last_entry(last_entry_)
            io.info('Last session file is loaded.')


def _get_first_and_last_lines(file):
    with open(file) as f:
        first_line = f.readline().rstrip('\n')
        last_line = first_line

        for line in f:
            last_line = line

    return first_line, last_line


def _make_session_file_complete(first_entry):
    complete_session_file = f'{SESSION_FILE}_{first_entry.timestamp}'
    os.rename(SESSION_FILE, complete_session_file)


#
# Add entry
#


def add_entry(timestamp, entry_type, entry_content):
    if '\t' in entry_content:
        io.error(
            "Tabs are not allowed in entry's content. "
            "Last entry was not registered."
        )
        return

    entry = Entry(timestamp, entry_type, entry_content)

    with open(SESSION_FILE, 'a') as f:
        line = _make_line_from_entry(entry)
        f.write(f'{line}\n')

    _set_last_entry(entry)


#
# Last entry
#


_last_entry = Entry(-1, '', '')


def last_entry():
    return _last_entry


def _set_last_entry(entry):
    global _last_entry
    _last_entry = entry

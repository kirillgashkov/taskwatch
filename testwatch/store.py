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


#
# Init
#


def init():
    if os.path.exists(SESSION_FILE):
        io.info('Session file is detected.')
        _handle_session_file()


def _handle_session_file():
    with open(SESSION_FILE) as f:
        first_line = f.readline().rstrip('\n')
        last_line = first_line

        for line in f:
            last_line = line

    if not first_line:
        return


    first_entry = _make_entry_from_line(first_line)
    last_entry = _make_entry_from_line(last_line)

    if last_entry.type == 'end':
        os.rename(SESSION_FILE, f'{SESSION_FILE}_{first_entry.timestamp}')
        io.info('Complete session file is created.')
    else:
        global _last_entry
        _last_entry = last_entry
        io.info('Last session file is loaded.')


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

    with open(SESSION_FILE, 'a') as f:
        f.write(f'{timestamp}\t{entry_type}\t{entry_content}\n')

    global _last_entry
    _last_entry = Entry(timestamp, entry_type, entry_content)


#
# Last entry
#


_last_entry = Entry(-1, '', '')


def last_entry():
    return _last_entry

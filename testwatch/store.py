import os

from testwatch import io


SESSION_FILE = '.testwatch_session'


_last_entry = (-1, '', '')


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

    first_timestamp, _, _ = first_line.split('\t')
    last_timestamp, last_type, last_content = last_line.split('\t')

    if last_type == 'end':
        os.rename(SESSION_FILE, f'{SESSION_FILE}_{first_timestamp}')
        io.info('Complete session file is created.')
    else:
        global _last_entry
        _last_entry = (last_timestamp, last_type, last_content)
        io.info('Last session file is loaded.')


def last_entry():
    return _last_entry

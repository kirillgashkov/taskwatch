from testwatch import store, watch


def start():
    store.add_entry(watch.current_time(), 'start', '')


def end():
    store.add_entry(watch.current_time(), 'end', '')


def write(s):
    if s.startswith('*') or s.endswith('*'):
        _amend(s.strip('*').strip())
    else:
        _record(s)


def _record(s):
    store.add_entry(watch.current_time(), 'record', s)


def _amend(s):
    store.add_entry(watch.current_time(), 'amend', s)

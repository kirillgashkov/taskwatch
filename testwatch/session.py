from testwatch import store, watch


def start():
    store.add_entry(watch.current_time(), 'start', '')


def end():
    store.add_entry(watch.current_time(), 'end', '')

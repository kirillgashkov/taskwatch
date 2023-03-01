from taskwatch import store, watch


def start() -> None:
    store.add_entry(watch.current_time(), "start", "")


def end() -> None:
    store.add_entry(watch.current_time(), "end", "")


def write(s: str) -> None:
    if s.startswith("*") or s.endswith("*"):
        store.add_entry(watch.current_time(), "record", s)
    else:
        store.add_entry(watch.current_time(), "amend", s)

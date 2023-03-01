from taskwatch import store, watch


def start() -> None:
    store.add_entry(watch.current_time(), "start", "")


def end() -> None:
    store.add_entry(watch.current_time(), "end", "")


def write(s: str) -> None:
    if s.startswith("*") or s.endswith("*"):
        _amend(s.strip("*").strip())
    else:
        _record(s)


def _record(s: str) -> None:
    store.add_entry(watch.current_time(), "record", s)


def _amend(s: str) -> None:
    store.add_entry(watch.current_time(), "amend", s)

import datetime


#
# Low-level Input
#


def readline():
    s = input('>>> ').strip()
    return s or readline()


def ask(prompt):
    if prompt:
        print(prompt)
    s = readline().strip()
    return s


def confirm(prompt):
    s = ask(prompt).lower()
    if s in {'y', 'yes'}:
        return True
    if s in {'n', 'no'}:
        return False
    return confirm(prompt)


#
# Low-level Output
#


def info(s):
    print(s)


def error(s):
    print(s)


#
# Formatters
#


def format_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    h_str = f'{h}h ' if h else ''
    m_str = f'{m}m ' if m else ''
    s_str = f'{s}s'

    return h_str + m_str + s_str


def format_date(unix):
    fmt = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.utcfromtimestamp(unix).strftime(fmt)

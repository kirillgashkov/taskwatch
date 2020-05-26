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


def format_date(unix):
    fmt = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.utcfromtimestamp(unix).strftime(fmt)

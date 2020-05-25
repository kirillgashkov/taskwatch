#
# Input
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

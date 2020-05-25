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

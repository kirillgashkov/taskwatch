#
# Input
#


def readline():
    s = input('>>> ').strip()
    return s or readline()

from testwatch import io, session


def main():
    if not io.confirm('Shall we begin? [y/n]'):
        return

    session.start()

    while True:
        s = io.readline()

        if s == 'end':
            break

        session.write(s)

    session.end()


if __name__ == '__main__':
    main()

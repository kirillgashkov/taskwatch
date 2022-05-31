from testwatch import io, report, session, store


def main():
    store.init()

    if not io.confirm("Shall we begin? [y/n]"):
        return

    session.start()

    while True:
        s = io.readline()

        if s == "end":
            break

        session.write(s)

    session.end()

    io.print_report(report.make_report())


if __name__ == "__main__":
    main()

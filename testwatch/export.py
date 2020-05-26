def report_to_tsv(report):
    rows = list()

    start_row = ['start', str(report.start_time), str(report.start_time)]
    rows.append(start_row)

    for task in report.tasks:
        task_row = [task.name, str(task.start_time), str(task.end_time)]
        rows.append(task_row)

    end_row = ['end', str(report.end_time), str(report.end_time)]
    rows.append(end_row)

    lines = map(lambda row: '\t'.join(row), rows)
    return '\n'.join(lines)

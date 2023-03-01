# Taskwatch

A stopwatch for tasks.

## Requirements

- Python 3.10

## Installation

```sh
$ git clone git@github.com:kirillgashkov/taskwatch.git
```

## Usage

This is an interactive program. Run these commands to start interacting.

```bash
$ cd taskwatch
$ python -m taskwatch
```

### Example

Send "y" to start the `taskwatch` session (aka the stopwatch).

```
Shall we begin? [y/n]
>>> y
```

Each line you send creates a new entry with a label and a timestamp
(aka stopwatch's lap with a label). The line's text is the entry's label. 

```
>>> 1
>>> 2
>>> break
>>> 33
>>> 3*
>>> end
```

Note that there are a couple of special lines:

- A line with text "break".
    - Send it to tell `taskwatch` not to take into account the time that passed
      since the last entry. This may be useful when you want to take a break
      from the test and do other things.
- A line that starts with or ends with asterisks (\*).
    - Send it to amend the last entry. Basically, it overrides its timestamp and
      label with the current ones (asterisks are stripped).
- A line with text "end".
    - Send it to end the `taskwatch` session and see the session report.

## FAQ

### What is a session report?

When your session is ended, you are presented its report (aka summary) in two
forms: human-readable and computer readable.

Human-readable report makes it easy to see how much time you spent on this test,
on breaks and on each individual task.

Computer readable report makes it easy to parse and process the data. Each line
of the computer readable report represents an event with a label, unix start
time and unix end time. 

### What is a `.taskwatch_session` file?

Your current session is being saved in this file. It's not recommended to open
this file in any editor (since they might trim the whitespaces). 

### What are `.taskwatch_session_<DIGITS>` files?

It is one of your archived sessions. `<DIGITS>` represents the unix time when
this session was started. If you want to see this session's report, rename it to
`.taskwatch_session`, run the program and follow instructions. 

## License

Distributed under the MIT License. See the [LICENSE.md](LICENSE.md) for details.

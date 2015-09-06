cleverbot
=========

A python3 binding of cleverbot wich **support special characters**.

How to
------
### Install
```bash
$ pip install .
```

### Library

Example of how to use the library:

```python
from cleverbot import cleverbot

myBot = cleverbot.Session()
answer = myBot.Ask("Hello there")
print(answer)
```

### Command Line

Start from command line, exit with `bye`

```bash
$ cleverbot
> hello
Hi.
> how are you?
I'm ok.
> bye
Don't leave.
$
```

Contribution
------------

This library is currently maintained. Pull Requests and issues are welcomed !

Credits
-------

This library is a port of [pycleverbot](https://code.google.com/p/pycleverbot/) to python3 with some fixes

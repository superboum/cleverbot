cleverbot
=========

A python3 binding of cleverbot wich **support special characters**
This library lets you open chat session with cleverbot (www.cleverbot.com)

How to
------

### The Binding

Example of how to use the bindings:

```python
import cleverbot

myBot = cleverbot.Session()
answer = myBot.Ask("Hello there")
print(answer)
```

### Command Line

Just run

```bash
python3 cleverbot.py
```

Credits
-------

This library is a port of [pycleverbot](https://code.google.com/p/pycleverbot/) to python3 with some fixes

# BackBot
A in-development chatbot.

# How the chatbot works
This is a simple chatbot that relies on the user input. It already has a (small) set of general sentences that builds on the user input.

# How to use
Put this import in:

```python
import BackBot
```

Create a bot object.

```python
bot = Bot()
```

The `Bot` class signiture is

```python
Bot(*, default_info=True, runner=ConservationRunner, prompt=_default_prompt)
```

If `default_info` is true, use the default sentences. If it is false, It collects 5 sentences of input from the user. `runner` is the conservation runner. `prompt` is the prompt for entering messages.

Next, run a conservation!

```python
bot.run_conservation()
```

And there, you started a conservation! (Large argument warning.)

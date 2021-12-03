_training_file = open("traindata.txt")
_training_file_content = eval(_training_file.read())


def reset_info(self):
    self.info = _training_file_content


_default_prompt = ">>> "
_special_commands = {
    "/exit": lambda self: exit(),
    "/clear": reset_info
}


def get(*, prompt=_default_prompt):
    return input(prompt)


def collect(*, prompt=_default_prompt):
    info = set()

    for _ in range(5):
        info.add(get(prompt=prompt))
        print("I am sorry. I cannot respond now. I am collecting info.")

    return info


class ConservationRunner:
    def __init__(self, *, info, prompt=_default_prompt):
        self.info = info
        self.prompt = prompt

    def handle_response(self, response):
        if response.startswith("/"):
            try:
                _special_commands[response.strip()](self)
            except KeyError:
                print("error: special command not found")
            return

        self.info.add(response)
        self.info.intersection_update(_training_file_content)
        self.info.update(_training_file_content)
        print(self.info.pop())

    def receive_and_respond(self):
        self.handle_response(get(prompt=self.prompt))


class Bot:
    def __init__(self, *, default_info=True, runner=ConservationRunner, prompt=_default_prompt):
        if not isinstance(prompt, str):
            raise TypeError("argument 'prompt' must be str")

        self.info = (collect(prompt=prompt)
                     if default_info is False
                     else _training_file_content)
        self.runner = runner(info=self.info, prompt=prompt)

    def run_conversation(self):
        while True:
            self.runner.receive_and_respond()


if __name__ == "__main__":
    bot = Bot()
    bot.run_conversation()

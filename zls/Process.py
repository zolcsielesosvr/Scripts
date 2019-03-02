import subprocess


class Process:
    def __init__(self, command=None):
        if command is None:
            self.command = []
        elif isinstance(command, list):
            self.command = command
        else:
            self.command = [command]

    def add_arg(self, arg):
        self.command.append(arg)

    def run(self):
        return subprocess.run(self.command)

    def clone(self):
        return Process(self.command)

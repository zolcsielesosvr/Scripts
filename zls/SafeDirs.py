import os

class Dirs:
    def __init__(self, start=None):
        self.olddirs = [os.getcwd()]
        if start is not None:
            os.chdir(start)

    def cd(self, path):
        os.chdir(path)

    def exists(self, path):
        return os.path.exists(path)

    def md(self, path, change = False):
        if not self.exists(path):
            os.mkdir(path)
        if change:
            self.cd(path)

    def mdcd(self, path):
        self.md(path, True)

    def cwd(self):
        return os.getcwd()

    def push(self):
        self.olddirs.append(self.cwd())

    def pop(self):
        if len(self.olddirs) > 1:
            self.cd(self.olddirs.pop())
        else:
            self.cd(self.olddirs[0])

    def __del__(self):
        os.chdir(self.olddirs[0])

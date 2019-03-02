from .Process import *


class Git:
    def __init__(self, remote=None, local=None):
        self.process = Process("git")
        self.branchOrTag = None
        self.recursive = False
        self.remote = remote
        self.local = local

    def setRemote(self, remote):
        self.remote = remote

    def setLocal(self, local):
        self.local = local

    def setBranchOrTag(self, branchOrTagName):
        self.branchOrTag = branchOrTagName

    def setRecursive(self, value=True):
        self.recursive = value

    def clone(self):
        process = self.process.clone()
        process.add_arg("clone")

        if self.branchOrTag is not None:
            process.add_arg("--branch")
            process.add_arg(self.branchOrTag)

        if self.recursive:
            process.add_arg("--recursive")

        if self.remote is None:
            raise RuntimeError("git clone requires remote branch")
        process.add_arg(self.remote)

        if self.local is not None:
            process.add_arg(self.local)

        return process.run()

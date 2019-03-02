from .Process import *


class Hg:
    def __init__(self, remote=None, local=None):
        self.process = Process("hg")
        self.branchOrTag = None
        self.remote = remote
        self.local = local

    def setRemote(self, remote):
        self.remote = remote

    def setLocal(self, local):
        self.local = local

    def setBranchOrTag(self, branchOrTagName):
        self.branchOrTag = branchOrTagName

    def clone(self):
        process = self.process.clone()
        process.add_arg("clone")

        if self.branchOrTag is not None:
            process.add_arg("--updaterev")
            process.add_arg(self.branchOrTag)

        if self.remote is None:
            raise RuntimeError("hg clone requires remote branch")
        process.add_arg(self.remote)

        if self.local is not None:
            process.add_arg(self.local)

        return process.run()

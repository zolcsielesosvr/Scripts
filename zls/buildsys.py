from .Git import *
Build32 = 32
Build64 = 64


class BuildSys:
    def __init__(self, repo_type=Git, local_dir=None):
        self.repoType = repo_type
        self.localDir = local_dir

    def download(self, vcs_root=None, vcs_branch_or_tag=None, vcs_recursive=True):
        vcs = self.repoType()
        vcs.setRemote(vcs_root)
        vcs.setBranchOrTag(vcs_branch_or_tag)
        vcs.setLocal(self.localDir)
        vcs.setRecursive(vcs_recursive)
        vcs.clone()

    def config(self):
        pass

    def build(self, config="Release"):
        pass

    def install(self, config="Release"):
        pass

    def isDownloaded(self):
        return False

    def isConfigured(self):
        return False

    def isBuilt(self):
        return False

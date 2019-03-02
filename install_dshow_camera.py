import zls
from settings import *


def download_dshow_camera():
    """ Download dshow camera """
    git = zls.Git()
    git.setRemote(dshow_git_root)
    git.setLocal("DirectShowCamera")
    git.clone()


def install_dshow_camera_full():
    d = zls.Dirs()
    target = zls.getInstallPath(None, zls.Arch.Common)
    target = target.replace("\\", "/")
    target = target.split("/")
    d.cd(target.pop(0) + "/")
    for path in target:
        d.mdcd(path)
    download_dshow_camera()


if __name__ == "__main__":
    install_dshow_camera_full()

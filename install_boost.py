import zls
from settings import *


def download_boost():
    """ Download boost repository """
    git = zls.Git()
    git.setRemote(boost_git_root)
    git.setBranchOrTag(boost_git_branch)
    git.setLocal("Boost")
    git.setRecursive()
    git.clone()


def bootstrap_boost():
    proc = zls.Process()
    if zls.IsWindows():
        proc.add_arg("bootstrap.bat")
    elif zls.IsLinux():
        proc.add_arg("bootstrap.sh")
    return proc.run()


def build_and_install_boost(justRequiredModules=False):
    proc = zls.Process("b2")

    proc.add_arg("install")
    proc.add_arg("--prefix=" + zls.getInstallPath("Boost"))

    proc.add_arg("--build-dir=" + zls.getThirdPartyBuildPath("Boost"))

    if justRequiredModules:
        proc.add_arg("--with-thread")
        proc.add_arg("--with-system")
        proc.add_arg("--with-date_time")
        proc.add_arg("--with-chrono")
        proc.add_arg("--with-program_options")
        proc.add_arg("--with-filesystem")
        proc.add_arg("--with-locale")
    proc.add_arg("link=static")
    proc.add_arg("runtime-link=shared")
    proc.add_arg("threading=multi")
    proc.run()


def install_boost_full():
    d = zls.Dirs()
    d.mdcd("ThirdParty")
    d.mdcd("sources")
    if not d.exists("Boost"):
        download_boost()
    d.cd("Boost")
    if not d.exists("bootstrap.log"):
        bootstrap_boost()
    build_and_install_boost()


if __name__ == "__main__":
    install_boost_full()

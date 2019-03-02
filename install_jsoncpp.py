import zls
from settings import *

def download_jsoncpp():
    """ Download jsoncpp repository """
    git = zls.Git()
    git.setRemote(jsoncpp_git_root)
    git.setBranchOrTag(jsoncpp_git_branch)
    git.setLocal("jsoncpp")
    git.setRecursive()
    git.clone()


def config_jsoncpp(is64bit=False):
    """ Configure jsoncpp """
    cmake = zls.CMake(zls.getThirdPartySourcePath("jsoncpp"))
    cmake.set_generator(is64bit)
    if is64bit:
        arch = zls.Arch.x64
    else:
        arch = zls.Arch.x86
    cmake.add_definition("CMAKE_INSTALL_PREFIX", zls.getInstallPath("jsoncpp", arch))
    if zls.IsWindows():
        cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING")
    cmake.add_definition("DEBUG_LIBNAME_SUFFIX", "d")
    cmake.config()


def build_jsoncpp(config="Release"):
    """ Build jsoncpp """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.build()


def install_jsoncpp(config="Release"):
    """ Install jsoncpp """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.set_build_target("INSTALL")
    cmake.build()


def install_jsoncpp_full():
    d = zls.Dirs()
    d.mdcd("ThirdParty")
    d.push()
    d.mdcd("sources")
    if not d.exists("jsoncpp"):
        download_jsoncpp()
    sourceDir = d.cwd()
    d.pop()
    d.mdcd("build")
    for is64bit in [False, True]:
        if is64bit:
            if not jsoncpp_build_64_bit:
                continue
            d.push()
            d.mdcd("jsoncpp_x64")
        else:
            if not jsoncpp_build_32_bit:
                continue
            d.push()
            d.mdcd("jsoncpp_x86")
        if not d.exists("CMakeFiles"):
            config_jsoncpp(is64bit)

        for config in jsoncpp_build_configs:
            if True or d.exists("CMakeFiles") and not d.exists(config): #x64/config | config
                build_jsoncpp(config)
            if True or d.exists(config):
                install_jsoncpp(config)
        d.pop()


if __name__ == "__main__":
    install_jsoncpp_full()

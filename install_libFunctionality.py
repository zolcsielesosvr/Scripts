import zls
from settings import *

def download_libFunctionality():
    """ Download libFunctionality repository """
    git = zls.Git()
    git.setRemote(libFunctionality_git_root)
    git.setBranchOrTag(libFunctionality_git_branch)
    git.setLocal("libFunctionality")
    git.setRecursive()
    git.clone()


def config_libFunctionality(is64bit=False):
    """ Configure libFunctionality """
    cmake = zls.CMake(zls.getSourcePath("libFunctionality"))
    cmake.set_generator(is64bit)
    if is64bit:
        arch = zls.Arch.x64
    else:
        arch = zls.Arch.x86
    cmake.add_definition("CMAKE_INSTALL_PREFIX", zls.getInstallPath("libFunctionality", arch))
    if zls.IsWindows():
        cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING /DWIN32") # /wd4530
    cmake.add_definition("BUILD_TESTING", "OFF")
    cmake.config()


def build_libFunctionality(config="Release"):
    """ Build libFunctionality """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.build()


def install_libFunctionality(config="Release"):
    """ Install libFunctionality """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.set_build_target("INSTALL")
    cmake.build()


def install_libFunctionality_full():
    d = zls.Dirs()
    d.mdcd("sources")
    if not d.exists("libFunctionality"):
        download_libFunctionality()
    sourceDir = d.cwd()
    d.pop()
    d.mdcd("build")
    for is64bit in [False, True]:
        if is64bit:
            if not libFunctionality_build_64_bit:
                continue
            d.push()
            d.mdcd("libFunctionality_x64")
        else:
            if not libFunctionality_build_32_bit:
                continue
            d.push()
            d.mdcd("libFunctionality_x86")
        if not d.exists("CMakeFiles"):
            config_libFunctionality(is64bit)

        for config in libFunctionality_build_configs:
            if True or d.exists("CMakeFiles") and not d.exists("bin"):
                build_libFunctionality(config)
            if d.exists("bin"):
                install_libFunctionality(config)
        d.pop()


if __name__ == "__main__":
    install_libFunctionality_full()

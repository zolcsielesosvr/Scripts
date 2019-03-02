import zls
from settings import *


def download_opencv():
    """ Download OpenCV repository """
    git = zls.Git()
    git.setRemote(opencv_git_root)
    git.setBranchOrTag(opencv_git_branch)
    git.setLocal("OpenCV")
    git.setRecursive()
    git.clone()


def config_opencv(is64bit=False):
    """ Configure OpenCV """
    cmake = zls.CMake(zls.getThirdPartySourcePath("OpenCV"))
    cmake.set_generator(is64bit)
    cmake.add_definition("CMAKE_INSTALL_PREFIX", zls.getInstallPath("OpenCV"))
    if zls.IsWindows():
        cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING /DWIN32 /wd4530")
        """
        Disable warning: /wd4530 or Enable exception handling: /EHsc
        """
    cmake.add_definition("BUILD_SHARED_LIBS", "ON")
    cmake.add_definition("BUILD_PERF_TESTS", "OFF")
    cmake.add_definition("BUILD_TESTS", "OFF")
    cmake.add_definition("BUILD_opencv_python", "OFF")
    cmake.add_definition("BUILD_opencv_java", "OFF")
    cmake.config()


def build_opencv(config="Release"):
    """ Build OpenCV """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.build()


def install_opencv(config="Release"):
    """ Install OpenCV """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.set_build_target("INSTALL")
    cmake.build()


def install_opencv_full():
    d = zls.Dirs()
    d.mdcd("ThirdParty")
    d.push()
    d.mdcd("sources")
    if not d.exists("OpenCV"):
        download_opencv()
    sourceDir = d.cwd()
    d.pop()
    d.mdcd("build")
    for is64bit in [False, True]:
        if is64bit:
            if not opencv_build_64_bit:
                continue
            d.push()
            d.mdcd("OpenCV_x64")
        else:
            if not opencv_build_32_bit:
                continue
            d.push()
            d.mdcd("OpenCV_x86")
        if not d.exists("cvconfig.h"):
            config_opencv(is64bit)

        for config in opencv_build_configs:
            if d.exists("cvconfig.h") and not d.exists("bin"):
                build_opencv(config)
            if d.exists("bin"):
                install_opencv(config)
        d.pop()


if __name__ == "__main__":
    install_opencv_full()

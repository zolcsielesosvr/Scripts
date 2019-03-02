import zls
from settings import *

def download_osvr_core():
    """ Download OSVR Core Repository """
    git = zls.Git()
    git.setRemote(osvr_core_git_root)
    git.setBranchOrTag(osvr_core_git_branch)
    git.setLocal("OSVR-Core")
    git.setRecursive()
    git.clone()


def config_osvr_core(is64bit=False):
    """ Configure OSVR-Core """
    cmake = zls.CMake(zls.getSourcePath("OSVR-Core"))
    cmake.set_generator(is64bit)
    if is64bit:
        arch = zls.Arch.x64
    else:
        arch = zls.Arch.x86
    cmake.add_definition("CMAKE_PREFIX_PATH", zls.getPrefixPath(arch))
    cmake.add_definition("CMAKE_INSTALL_PREFIX", zls.getInstallPath("OSVR-Core", arch))

    #SDL2:
    cmake.add_definition("SDL2_LIBRARY", zls.getInstallPath("SDL", arch) + "/lib/SDL2.lib")
    cmake.add_definition("SDL2_SDLMAIN_LIBRARY", zls.getInstallPath("SDL", arch) + "/lib/SDL2main.lib")
    cmake.add_definition("SDL2_INCLUDE_DIR", zls.getInstallPath("SDL", arch) + "/include/SDL2")

    #Boost:
    cmake.add_definition("BOOST_ROOT", zls.getInstallPath("Boost"))

    #jsoncpp:
    #cmake.add_definition("JsonCpp_INCLUDE_DIR", zls.root + "/install/jsoncpp_" + arch_postfix + "/include")
    #cmake.add_definition("JsonCpp_LIBRARY", zls.root + "/install/jsoncpp_" + arch_postfix + "/lib/jsoncpp.lib")

    if zls.IsWindows():
        cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING /MP  /EHsc")
        cmake.add_definition("DIRECTSHOW_QEDIT_INCLUDE_DIR", zls.getInstallPath("DirectShowCamera") + "/include")
        cmake.add_definition("DIRECTSHOW_STRMIIDS_LIBRARY", zls.getInstallPath("DirectShowCamera") + zls.appendArchSuffix("/lib", arch) + "/strmiids.lib")
    cmake.add_definition("BUILD_HEADER_DEPENDENCY_TESTS", "OFF")
    cmake.config()


def build_osvr_core(config="Release"):
    """ Build OSVR-Core """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.build()


def install_osvr_core(config="Release"):
    """ Install OSVR-Core """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.set_build_target("INSTALL")
    cmake.build()


def install_osvr_core_full():
    d = zls.Dirs()
    d.mdcd("sources")
    if not d.exists("OSVR-Core"):
        download_osvr_core()
    sourceDir = d.cwd()
    d.pop()
    d.mdcd("build")
    for is64bit in [False, True]:
        if is64bit:
            if not osvr_core_build_64_bit:
                continue
            d.push()
            d.mdcd("OSVR-Core_x64")
        else:
            if not osvr_core_build_32_bit:
                continue
            d.push()
            d.mdcd("OSVR-Core_x86")
        if not d.exists("CMakeFiles"):
            config_osvr_core(is64bit)

        for config in osvr_core_build_configs:
            if True or d.exists("CMakeFiles") and not d.exists("bin"):
                build_osvr_core(config)
            if True or d.exists("bin"):
                install_osvr_core()
        d.pop()


if __name__ == "__main__":
    install_osvr_core_full()

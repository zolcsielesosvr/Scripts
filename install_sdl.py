import zls
from settings import *

def download_sdl():
    """ Download SDL repository """
    hg = zls.Hg()
    hg.setRemote(sdl_hg_root)
    hg.setBranchOrTag(sdl_hg_branch)
    hg.setLocal("SDL")
    hg.clone()


def config_sdl(is64bit=False):
    """ Configure SDL """
    cmake = zls.CMake(zls.getThirdPartySourcePath("SDL"))
    cmake.set_generator(is64bit)
    if is64bit:
        arch = zls.Arch.x64
    else:
        arch = zls.Arch.x86
    cmake.add_definition("CMAKE_INSTALL_PREFIX", zls.getInstallPath("SDL", arch))
    cmake.config()


def build_sdl(config="Release"):
    """ Build SDL """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.build()


def install_sdl(config="Release"):
    """ Install SDL """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.set_build_target("INSTALL")
    cmake.build()


def install_sdl_full():
    d = zls.Dirs()
    d.mdcd("ThirdParty")
    d.push()
    d.mdcd("sources")
    if not d.exists("SDL"):
        download_sdl()
    sourceDir = d.cwd()
    d.pop()
    d.mdcd("build")
    for is64bit in [False, True]:
        if is64bit:
            if not sdl_build_64_bit:
                continue
            d.push()
            d.mdcd("SDL_x64")
        else:
            if not sdl_build_32_bit:
                continue
            d.push()
            d.mdcd("SDL_x86")
        if True:
            config_sdl(is64bit)

        for config in sdl_build_configs:
            if True:
                build_sdl(config)
            if True:
                install_sdl(config)
        d.pop()


if __name__ == "__main__":
    install_sdl_full()

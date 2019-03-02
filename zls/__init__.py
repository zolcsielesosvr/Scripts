from .Process import *
from .CMake import *
from .Platform import *
from .SafeDirs import *
from .Git import *
from .Hg import *
from .buildsys import *

rootDir = Dirs("..")
root = rootDir.cwd()

print("Current root path is:", root)


def getArchString(arch: Arch = Arch.Common):
    if arch == Arch.x86:
        return "x86"
    elif arch == Arch.x64:
        return "x64"
    elif arch == Arch.Common:
        return "common"


def appendArchSuffix(name, arch: Arch = Arch.Common):
    if arch != Arch.Common:
        return name + "_" + getArchString(arch)
    return name


def getInstallPath(name=None, arch: Arch = Arch.Common):
    path = root + "/install/" + getArchString(arch)
    if name is not None:
        path = path + "/" + name
    return path


def getThirdPartyBuildPath(name, arch: Arch = Arch.Common):
    path = root + "/ThirdParty/build/" + name
    return appendArchSuffix(path, arch)


def getThirdPartySourcePath(name):
    path = root + "/ThirdParty/sources/" + name
    return path


def getBuildPath(name, arch: Arch = Arch.Common):
    path = root + "/build/" + name
    return appendArchSuffix(path, arch)


def getSourcePath(name):
    path = root + "/sources/" + name
    return path


def getPrefixPath(arch):
    directories = ""
    directories = directories + getInstallPath(None, arch)
    directories = directories + ";"
    directories = directories + getInstallPath()
    return directories

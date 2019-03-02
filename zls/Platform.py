import platform
from enum import Enum


class Arch(Enum):
    Common = 0
    x86 = 1
    x64 = 2


def IsWindows():
    return platform.system() == "Windows"


def IsLinux():
    return platform.system() == "Linux"



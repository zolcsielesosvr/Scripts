git_root = "https://github.com/zolcsielesosvr/"

#Configs: ["Release", "Debug"]

all_configs = ["Release", "Debug"]
release_config = ["Release"]
debug_config = ["Debug"]
default_configs = all_configs

#Boost settings:
boost_git_root = "https://github.com/boostorg/boost.git"
boost_git_branch = "boost-1.69.0"

#DirectShow settings:
dshow_git_root = git_root + "DirectShow.git"

#SDL settings:
sdl_hg_root = "http://hg.libsdl.org/SDL"
sdl_hg_branch = "release-2.0.9"
sdl_build_configs = release_config
sdl_build_32_bit = True
sdl_build_64_bit = True

#jsoncpp settings:
jsoncpp_git_root = "https://github.com/open-source-parsers/jsoncpp.git"
jsoncpp_git_branch = None
jsoncpp_build_configs = all_configs
jsoncpp_build_32_bit = True
jsoncpp_build_64_bit = True

#OpenCV settings:
opencv_git_root = "https://github.com/opencv/opencv.git"
opencv_git_branch = "2.4"
opencv_build_configs = release_config
opencv_build_32_bit = True
opencv_build_64_bit = True

#libFunctionality settings:
libFunctionality_git_root = git_root + "libFunctionality"
libFunctionality_git_branch = None
libFunctionality_build_configs = release_config
libFunctionality_build_32_bit = True
libFunctionality_build_64_bit = True

#OSVR Core settings:
osvr_core_git_root = git_root + "OSVR-Core.git"
osvr_core_git_branch = None
osvr_core_build_configs = all_configs
osvr_core_build_32_bit = True
osvr_core_build_64_bit = True


from .Process import *


class CMake:
    def __init__(self, path = ".."):
        self.path = path
        self.process = Process("cmake")
        self.definitions = []
        self.generator = None
        self.build_config = None
        self.build_target = None

    def add_definition(self, definition, value):
        self.definitions.append([definition, value])

    def set_generator(self, is64bit):
        if not is64bit:
            self.generator = "Visual Studio 15 2017"
        else:
            self.generator = "Visual Studio 15 2017 Win64"

    def config(self):
        process = self.process.clone()
        for d in self.definitions:
            process.add_arg("-D%s=%s" % (d[0], d[1]))

        process.add_arg(self.path)

        if self.generator is not None:
            process.add_arg("-G%s" % self.generator)

        return process.run()

    def set_build_config(self, config):
        self.build_config = config

    def set_build_target(self, target):
        self.build_target = target

    def build(self):
        process = self.process.clone()
        process.add_arg("--build")
        process.add_arg(".")

        if self.build_target != None:
            process.add_arg("--target")
            process.add_arg(self.build_target)

        if self.build_config != None:
            process.add_arg("--config")
            process.add_arg(self.build_config)

        return process.run()

import os
from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, CMakeToolchain


class BIMGCConan(ConanFile):
    name = "bimg"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"
    exports_sources = "CMakeLists.txt"

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def requirements(self):
        self.requires("bx/local@", transitive_headers=True)
        self.requires("astc_encoder/local@")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.presets_prefix = f"{self.settings.os}_{self.settings.build_type}_{self.settings.arch}"
        tc.generate()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
        conan.tools.files.copy(self, "*.h",
                               os.path.join(self.folders.base_build, "bimg/include"),
                               os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.includedirs = ["include", "include/bimg"]
        self.cpp_info.libs = conan.tools.files.collect_libs(self)

# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cxxmpi(CMakePackage):
    """Modern C++20 wrapper for MPI.
    
    cxxmpi is a header-only C++20 wrapper library for MPI that provides 
    type-safe, RAII-compliant interfaces with modern C++ features.
    """

    homepage = "https://github.com/range3/cxxmpi"
    url = "https://github.com/range3/cxxmpi/archive/v0.1.0.tar.gz"
    git = "https://github.com/range3/cxxmpi.git"


    maintainers("range3")

    license("UNKNOWN", checked_by="range3")

    version("master", branch="master")
    version("0.1.6", sha256="28d020568a20873693a0acc08f42a908cbad36c22873c13d966c2f4f924aaa63", preferred=True)

    depends_on("cxx", type="build")
    depends_on("cmake@3.15:", type="build")
    depends_on("mpi")
    # depends_on("catch2@3.0.0:", type=("build", "test"))

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_STANDARD", "20"),
            self.define("CMAKE_CXX_STANDARD_REQUIRED", "ON"),
        ]
        return args

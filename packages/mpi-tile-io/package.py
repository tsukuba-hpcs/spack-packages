# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mpi-tile-io
#
# You can edit this file again by typing:
#
#     spack edit mpi-tile-io
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class MpiTileIo(MakefilePackage):
    """a tile reading MPI-IO application"""

    homepage = "https://www.mcs.anl.gov/research/projects/pio-benchmark/"
    url = "https://www.mcs.anl.gov/research/projects/pio-benchmark/code/mpi-tile-io-01022003.tgz"

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version(
        "01022003",
        sha256="8ae81a10a06c1ec4cbb6205eb979373fa217156ce8afa025e7b2f11c41d4b5ce",
    )

    depends_on("c", type="build")
    depends_on("mpi", type=("build", "run"))

    def edit(self, spec, prefix):
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass

    @property
    def build_targets(self):
        spec = self.spec
        return [
            "all",
            "CC={}".format(spec["mpi"].mpicc),
            "CFLAGS=-Wall -g -O2 -DHAVE_GETOPT_LONG",
        ]

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("mpi-tile-io", prefix.bin)

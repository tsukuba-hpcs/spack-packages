# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import sys

from spack.build_environment import dso_suffix
from spack.package import *

try:
    from spack_repo.builtin.packages.mpich.package import Mpich as BuiltinMpich
except:
    from spack.pkg.builtin.mpich import Mpich as BuiltinMpich

class LocalityAwareMpiio(BuiltinMpich):
    '''locality-aware MPI-IO'''

    homepage = 'https://github.com/tsukuba-hpcs/locality-aware-mpi-io'
    git = 'https://github.com/tsukuba-hpcs/locality-aware-mpi-io.git'

    maintainers("sugihara@hpcs.cs.tsukuba.ac.jp")

    version("develop", branch="develop", preferred=False, submodules=True)
    version("4.2", branch="work-4.2.x", preferred=True, submodules=True)
    version("4.2-debug", branch="work-4.2.x", preferred=False, submodules=True)
    version("4.2-profiler", branch="profiler", preferred=False, submodules=True)
    version("4.3", branch="work-4.3.x", preferred=True, submodules=True)
    version("4.3-debug", branch="work-4.3.x", preferred=False, submodules=True)
    version("4.3-profiler", branch="profiler", preferred=False, submodules=True)

    variant(
        "romio-filesystem",
        description="Add the filesystem to romio",
        values=disjoint_sets(
            (
                "daos",
                "nfs",
                "ufs",
                "pvfs2",
                "testfs",
                "xfs",
                "panfs",
                "lustre",
                "gpfs",
                "ime",
                "quobytefs",
                "gfarm",
                "gfarms",
            )
        ).with_non_feature_values("none"),
    )
    depends_on("gfarm", type=("build", "link", "run"), when="romio-filesystem=gfarm,gfarms")
    depends_on("libbptree", type=("build", "link", "run"), when="romio-filesystem=gfarms")

    def configure_args(self):
        spec = self.spec
        config_args = super(LocalityAwareMpiio, self).configure_args()
        # ROMIO
        if "+romio" in spec and not spec.satisfies("romio-filesystem=none"):
            args = "+".join(spec.variants["romio-filesystem"].value)
            config_args.append(f"--with-file-system={args}")
        return config_args

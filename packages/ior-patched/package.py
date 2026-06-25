import os
import re
import sys

from spack.build_environment import dso_suffix
from spack.package import *

try:
    from spack_repo.builtin.packages.ior.package import Ior as BuiltinIor
except:
    from spack.pkg.builtin.ior import Ior as BuiltinIor

class IorPatched(BuiltinIor):
    homepage = 'https://github.com/tsukuba-hpcs/ior'
    git = 'https://github.com/tsukuba-hpcs/ior.git'

    maintainers("sugihara@hpcs.cs.tsukuba.ac.jp")

    version("4.0.0-statfs", branch="4.0.0-statfs", preferred=True, submodules=True)

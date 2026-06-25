import os
import re
import sys

from spack.build_environment import dso_suffix
from spack.package import *

try:
    from spack_repo.builtin.packages.ior.package import Ior as BuiltinIor
except:
    from spack.pkg.builtin.ior import Ior as BuiltinIor

class Ior(BuiltinIor):
    variant("chfs", default=False, description="support IO with CHFS backend", when="@4:")
    variant("gfarm", default=False, description="support IO with Gfarm backend")

    requires("@4.0.0:", when="+chfs", msg="CHFS backend requires IOR 4.0.0 or later")

    depends_on("pkg-config", type="build")
    depends_on("chfs",  type=("build", "link", "run"), when="+chfs")
    depends_on("gfarm", type=("build", "link", "run"), when="+gfarm")

    def configure_args(self):
        spec = self.spec

        if spec.satisfies("+chfs"):
            pkg_config = which("pkg-config")
            pkg_config("--exists", "chfs")

        config_args = super(Ior, self).configure_args()

        if spec.satisfies("+gfarm"):
            config_args.append("--with-gfarm")
        else:
            config_args.append("--without-gfarm")

        return config_args

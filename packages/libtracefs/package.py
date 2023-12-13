from spack.package import *
import os


class Libtracefs(MakefilePackage):
    """libtracefs"""

    homepage = "https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/"
    url = "https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-1.7.0.tar.gz"

    version("1.7.0", sha256="411fcbf3434ecbaefa6c2b1bf092266293a672e2d7ee46fdd6b402753cb8bd16")

    conflicts("platform=darwin", msg="Linux-only")

    def install(self, spec, prefix):
        make(
                "install",
                f"prefix={prefix}",
                f"libdir_relative={os.path.basename(prefix.lib)}",
                f"libdir={prefix.lib}",
                f"pkgconfig_dir={prefix.lib.pkgconfig}")

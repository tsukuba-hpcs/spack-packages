from spack.package import *
import os


class Libtraceevent(MakefilePackage):
    """Library to parse raw trace event formats"""

    homepage = "https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/"
    url = "https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-1.7.3.tar.gz"

    version("1.7.3", sha256="097b72e0d907f3107825fb2edf0188324bf70dc9da360f6efa68dc484ffde541")

    conflicts("platform=darwin", msg="Linux-only")

    def install(self, spec, prefix):
        make(
                "install",
                f"prefix={prefix}",
                f"libdir_relative={os.path.basename(prefix.lib)}",
                f"libdir={prefix.lib}",
                f"pkgconfig_dir={prefix.lib.pkgconfig}")

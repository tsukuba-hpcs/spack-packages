from spack.package import *


class Ndctl(MesonPackage):
    """ndctl: A "device memory" enabling project encompassing tools and libraries
    for CXL, NVDIMMs, DAX, memory tiering and other platform memory device topics.
    """

    homepage = "https://github.com/pmem/ndctl"
    url = "https://github.com/pmem/ndctl/archive/v78.tar.gz"

    maintainers("range3")

    version("78", sha256="80596932920a3eb42551fc0d978f22bfa6a620f57af60c898dc0d0e303c086a5")

    depends_on('kmod')
    depends_on('libuuid')
    depends_on('json-c')
    depends_on('libtraceevent')
    depends_on('libtracefs')
    depends_on('iniparser')
    depends_on('libudev')
    depends_on('keyutils')

    depends_on('pkgconfig', type=('build'))

    def meson_args(self):
        args = [
                f"-Drootprefix={self.prefix}",
                f"-Diniparserdir={self.spec['iniparser'].prefix.include}",
                f"-Dsysconfdir={self.prefix.etc}",
                "-Dbashcompletiondir=no",
                "-Ddocs=disabled",
                "-Dsystemd=disabled",
                ]
        return args

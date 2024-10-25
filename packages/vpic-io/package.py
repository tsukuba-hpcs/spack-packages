from spack.package import *


class VpicIo(MakefilePackage):
    '''VPIC-IO kernel from the ExaHDF5 Parallel I/O Kernels (PIOK) suite'''

    homepage = 'https://github.com/glennklockwood/vpic-io'
    url = 'https://github.com/glennklockwood/vpic-io'
    git = 'https://github.com/glennklockwood/vpic-io.git'

    version('master', branch='master')
    
    depends_on('h5hut')

    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))

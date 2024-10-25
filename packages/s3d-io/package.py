from spack.package import *


class S3dIo(MakefilePackage):
    '''VPIC-IO kernel from the ExaHDF5 Parallel I/O Kernels (PIOK) suiterallel I/O benchmark using S3D application I/O kernel'''

    homepage = 'https://github.com/wkliao/S3D-IO.git'
    url = 'https://github.com/wkliao/S3D-IO'
    git = 'https://github.com/wkliao/S3D-IO.git'
    parallel = False

    version('master', branch='master')
    
    depends_on('parallel-netcdf')

    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))

    def install(self, spec, prefix):
        # Manual installation
        mkdir(prefix.bin)
        install("s3d_io.x", prefix.bin)

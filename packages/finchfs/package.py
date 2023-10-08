from spack.package import *


class Finchfs(AutotoolsPackage):
    '''FINCHFS is an ad hoc parallel file system for HPC.'''

    homepage = 'https://github.com/tsukuba-hpcs/finchfs'
    git = 'https://github.com/tsukuba-hpcs/finchfs.git'

    version('master', branch='master')

    variant('pmemkv', default=True, description='use pmemkv instead of a POSIX backend')

    depends_on('mpi')
    depends_on('ucx@1.14.1')
    depends_on('pmemkv', when='+pmemkv')

    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))

    def autoreconf(self, spec, prefix):
        autoreconf = which('autoreconf')
        autoreconf('-fiv')

    def configure_args(self):
        args = []

        if '+pmemkv' in self.spec:
            args.extend(['--with-pmemkv'])

        if '+zero_copy_read_rdma' in self.spec:
            args.extend(['--enable-zero-copy-read-rdma'])

        return args

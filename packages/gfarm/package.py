from spack.package import *


class Gfarm(AutotoolsPackage):
    '''distributed file system for large-scale cluster computing and wide-area data sharing. provides fine-grained replica location control.'''

    homepage = 'https://github.com/oss-tsukuba/gfarm'
    url = 'https://github.com/oss-tsukuba/gfarm/archive/refs/tags/2.8.0.tar.gz'
    git = 'https://github.com/oss-tsukuba/gfarm.git'

    version('master', branch='master')
    version('2.8.0', tag='2.8.0', preferred=True)
    version('2.7.25', tag='2.7.25')
    
    variant('infiniband', default=False, description='enable InfiniBand')

    depends_on('postgresql')
    depends_on('openssl')
    depends_on('rdma-core', when="+infiniband")
    depends_on('py-docopt')
    depends_on('py-schema')

    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))

    def configure_args(self):
        args = []

        if '+infiniband' in self.spec:
            args.extend(['--with-infiniband'])

        return args

from spack.package import *


class Chfs(AutotoolsPackage):
    '''CHFS parallel and distributed file system for node-local persistent memory'''

    homepage = 'https://github.com/otatebe/chfs'
    git = 'https://github.com/otatebe/chfs.git'
    url = 'https://github.com/otatebe/chfs/archive/1.0.0.tar.gz'

    maintainers = ['range3']

    version('master', branch='cache')
    version('develop', branch='cache')
    version('3.0.3', sha256='3bf0926e79d120383877ea6b3f8eb3b7e04c2560b441d0b91a505a7ee9dd8ea4', preferred=True)
    version('3.0.2', sha256='9f5960b1095a4ae8b8aba27e201de6ed84777bf3d4eca6b96c060d9c60af923c')
    version('3.0.1', sha256='22cdb14f7875a680858895e7fe01bcc710e66357db069c207c04ad41e289e266')
    version('3.0.0', sha256='93a2399af7b3fb1a1c8df42c2cd9bd30a5d28dbbfc4714e0c72d3c2555e3f80a')
    version('2.1.2', sha256='8ab41060d43c96db98db62df05ec19335574f264bd271b745a16195b3d5b26eb')
    version('2.1.0', sha256='6cc21e9b890628eab0c8a669ec71787de6b71dd77827519e2723472d48337d63')
    version('2.0.0', sha256='61aa3600963bded220c28adc8be8bcb0e6dd2ef56f7fb596f4bdefcec37f73ae')
    version('1.0.0', sha256='315295bf10b3b3fb93620791e844c540f6f238b4eab6a5c56825c6b7896737a2')
    # version('1.0.0-exp', git='', branch='experimental')

    variant('verbs', default=True, description='enable verbs')
    variant('pandoc', default=False, description='generate manual pages')
    variant('pmemkv', default=True, description='use pmemkv instead of a POSIX backend')
    variant('devdax', default=False, when='+pmemkv', description='enable devdax support')
    variant('zero_copy_read_rdma', default=False, when='+pmemkv', description='enable zero copy read rdma')

    depends_on('libfabric fabrics=rxm,sockets,tcp,udp', when='~verbs')
    depends_on('libfabric fabrics=rxm,sockets,tcp,udp,verbs', when='+verbs')
    depends_on('mochi-margo')
    depends_on('pmemkv', when='+pmemkv')
    depends_on('pmdk+ndctl', when='+devdax')
    depends_on('libfuse@2')
    depends_on('pandoc', when='+pandoc', type='build')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('pkgconfig', type='build')

    def autoreconf(self, spec, prefix):
        autoreconf = which('autoreconf')
        autoreconf('-fiv')

    def configure_args(self):
        args = []

        if self.spec.satisfies('@3.0.1:'):
            args.append(f"--with-fuse={self.spec['libfuse'].prefix}")

        if '+pmemkv' in self.spec:
            args.append('--with-pmemkv')

        if '+zero_copy_read_rdma' in self.spec:
            args.append('--enable-zero-copy-read-rdma')
        
        return args

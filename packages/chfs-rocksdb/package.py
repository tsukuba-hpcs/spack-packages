from spack.package import *


class ChfsRocksDB(AutotoolsPackage):
    '''CHFS parallel and distributed file system for node-local persistent memory'''

    homepage = 'https://github.com/onokatio/chfs-rocksdb'
    git = 'https://github.com/onokatio/chfs-rocksdb.git'
    url = 'https://github.com/onokatio/chfs-rocksdb'

    maintainers = ['onokatio']

    version('master', branch='feature/rocksdb')

    variant('verbs', default=True, description='enable verbs')
    variant('pandoc', default=False, description='generate manual pages')
    variant('devdax', default=False, when='+pmemkv', description='enable devdax support')
    variant('zero_copy_read_rdma', default=False, when='+pmemkv', description='enable zero copy read rdma')

    depends_on('libfabric fabrics=rxm,sockets,tcp,udp', when='~verbs')
    depends_on('libfabric fabrics=rxm,sockets,tcp,udp,verbs', when='+verbs')
    depends_on('mochi-margo')
    depends_on('pmdk+ndctl', when='+devdax')
    depends_on('libfuse@2')
    depends_on('pandoc', when='+pandoc', type='build')
    depends_on('rocksdb')

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

        if '+zero_copy_read_rdma' in self.spec:
            args.append('--enable-zero-copy-read-rdma')
        
        return args

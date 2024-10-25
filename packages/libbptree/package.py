from spack.package import *


class Libbptree(AutotoolsPackage):
    '''a library for B+-tree index'''

    homepage = 'https://github.com/k5342/libbptree'
    git = 'https://github.com/k5342/libbptree'

    version('master', branch='master')
    
    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))
    
    def setup_run_environment(self, env):
        env.prepend_path("CPATH", prefix.include)
        env.prepend_path("LIBRARY_PATH", prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", prefix.lib)

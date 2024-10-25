from spack.package import *


class LesIo(AutotoolsPackage):
    '''les-io: an I/O benchmark using City-LES kernel'''

    homepage = 'https://github.com/tsukuba-ccs/les-io'
    url = 'https://github.com/tsukuba-ccs/les-io'
    git = 'https://github.com/k5342/les-io.git'
    parallel = False

    version('master', branch='master')
    version('gfarms', branch='gfarms')
    version('separated', branch='separated')
    
    depends_on('netcdf-c+mpi',   type=("build", "link", "run"))
    depends_on('netcdf-fortran', type=("build", "link", "run"))
    depends_on('hdf5+mpi',       type=("build", "link", "run"))
    depends_on("mpi",            type=("build", "link", "run"))

    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))

    filter_compiler_wrappers("mpicc", "mpicxx", "mpif77", "mpif90", "mpifort", relative_root="bin")

    def setup_build_environment(self, env):
        env.set("FC", self.spec["mpi"].mpifc, force=True)
        env.set("F77", self.spec["mpi"].mpif77, force=True)
        env.set("CC", self.spec["mpi"].mpicc, force=True)
        env.set("CXX", self.spec["mpi"].mpicxx, force=True)

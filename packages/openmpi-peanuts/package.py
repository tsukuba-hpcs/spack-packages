# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.openmpi import Openmpi as BuiltinOpenmpi 

class OpenmpiPeanuts(BuiltinOpenmpi):

    git = "https://github.com/tsukuba-hpcs/ompi-peanuts.git"

    version("5.0.0rc12-peanuts", branch="peanuts", submodules=True)

    variant("romio", default=True, description="Enable ROMIO support")
    variant('aggregate_read', default=True, description='Enable aggregate read optimization')
    variant('debug', default=False, description='Enable debug')

    depends_on("autoconf @2.69:", type="build", when="@5.0.0rc12-peanuts,main")
    depends_on("automake @1.13.4:", type="build", when="@5.0.0rc12-peanuts,main")
    depends_on("libtool @2.4.2:", type="build", when="@5.0.0rc12-peanuts,main")
    depends_on("m4", type="build", when="@5.0.0rc12-peanuts,main")
    depends_on("libevent@2:", when="@5.0.0rc12-peanuts,main")

    @when("@5.0.0rc12-peanuts,main")
    def autoreconf(self, spec, prefix):
      perl = which("perl")
      perl("autogen.pl")

    def configure_args(self):
        spec = self.spec
        config_args = super(OpenmpiPeanuts, self).configure_args()
        if spec.satisfies("@5:") and not spec.satisfies("schedulers=tm"):
            config_args.append("--without-pbs")
        romio_flags=[
            "--with-file-system=testfs+ufs+peanuts",
        ]
        if spec.satisfies("+aggregate_read"):
            romio_flags.append("--enable-peanuts-aggregate-read")
        else:
            romio_flags.append("--disable-peanuts-aggregate-read")

        config_args.append("--with-io-romio-flags=" + " ".join(romio_flags))

        if spec.satisfies("+debug"):
            config_args.append("--enable-debug")

        return config_args

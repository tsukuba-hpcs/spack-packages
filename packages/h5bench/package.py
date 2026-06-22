# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

try:
    from spack_repo.builtin.packages.h5bench.package import H5bench as BuiltinH5bench
except:
    from spack.pkg.builtin.h5bench import H5bench as BuiltinH5bench


class H5bench(BuiltinH5bench):
    patch("e3sm-hdf5-extra-libs-v2.patch", when="+e3sm")
    patch("e3sm-hdf5-extra-libs-v2.patch", when="+all")
    patch("e3sm-install-binary.patch", when="+e3sm")
    patch("e3sm-install-binary.patch", when="+all")
    patch("metadata-write-strategy.patch", when="+mdc_write_strategy")

    variant(
        "mdc_write_strategy",
        default=False,
        description="Adds METADATA_WRITE_STRATEGY config support for HDF5 metadata cache writes",
    )

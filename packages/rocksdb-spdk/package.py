# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install rocksdb-spdk
#
# You can edit this file again by typing:
#
#     spack edit rocksdb-spdk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RocksdbSpdk(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://spdk.io/doc/blobfs.html"
    url = "https://github.com/spdk/rocksdb/archive/refs/heads/6.15.fb.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("6.15.fb", sha256="cdb4e9f50411e70c20a2018bda5d251c39c5b9b34ceb9c037071e7ad26eef78a")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make('static_lib')
        make('install')

from spack.package import *
import os


class Libudev(MesonPackage):
    """
    API for enumerating and introspecting local devices.
    The libudev library is included in the Systemd project.
    This spack package first builds the entire systemd and extracts only libudev.
    """

    homepage = "https://systemd.io/"
    url = "https://github.com/systemd/systemd/archive/v255.tar.gz"

    maintainers("range3")

    version("255", sha256="28854ffb2cb5f9e07fcbdbaf1e03a80b3462a12edeef84893ca2f37b22e4491e")

    depends_on("libcap")
    depends_on("util-linux@2.27.1:", type=("build", "link", "run"))

    depends_on("meson@0.60:", type="build")
    depends_on("python@3.7:", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("ninja", type="build")
    depends_on("awk", type="build")
    depends_on("sed", type="build")
    depends_on("grep", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("gperf", type="build")

    def meson_args(self):
        # Build entire the Systemd project.
        # Options should be as minimal as possible.
        args = [
            f"-Dsysconfdir={self.prefix.etc}",
            f"-Dlocalstatedir={self.prefix.var}",
            f"-Dsharedstatedir={self.prefix.var.lib}",
            f"-Dsysvinit-path={join_path(self.prefix.etc, 'init.d')}",
            f"-Dsysvrcnd-path={join_path(self.prefix.etc, 'rc.d')}",
            "-Dcreate-log-dirs=false",
            "-Dlink-journalctl-shared=false",
            "-Dbashcompletiondir=no",
            "-Dzshcompletiondir=no",
            "-Dauto_features=disabled",
            "-Ddbus=disabled",
        ]

        options = [
            "backlight",
            "binfmt",
            "dns-over-tls",
            "efi",
            "environment-d",
            "firstboot",
            "gshadow",
            "hibernate",
            "hwdb",
            "ima",
            "ldconfig",
            "nscd",
            "quotacheck",
            "randomseed",
            "rfkill",
            "smack",
            "standalone-binaries",
            "storagetm",
            "sysusers",
            "tmpfiles",
            "urlify",
            "utmp",
            "vconsole",
            "strip",
            "analyze",
            "coredump",
            "default-network",
            "hostnamed",
            "initrd",
            "install-sysconfdir",
            "install-tests",
            "kernel-install",
            "localed",
            "logind",
            "machined",
            "networkd",
            "nss-myhostname",
            "nss-systemd",
            "oomd",
            "portabled",
            "pstore",
            "static-libsystemd",
            "static-libudev",
            "sysext",
            "timedated",
            "timesyncd",
            "translations",
            "userdb",
            "xdg-autostart",
        ]
        for opt in options:
            args.append(f"-D{opt}=false")

        return args

    @run_after("install")
    def post_install(self):
        # Extract libudev
        # Delete all files except those containing "libudev" in the file name or under the ".spack" directory.
        for cur, dirs, files in os.walk(self.prefix, topdown=False):
            rel_cur = os.path.relpath(cur, self.prefix)
            if '.spack' in rel_cur:
                continue
            for name in files:
                if 'libudev' not in name:
                    os.remove(join_path(cur, name))
            try:
                os.rmdir(cur)
            except OSError:
                pass

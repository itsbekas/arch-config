from util import run_cmd 

class Package:
    """Base class for packages"""
    name = ""               # Name of package
    requirements = []       # Packages required for this package to work
    extras = []             # Extra packages that can be installed
    config_files = []       # Files to be appended, ordered
    output_location = ""    # Output location of files

    to_install = True       # Whether or not to install this package

    _instance = None        # Singleton instance

    def install(self):
        self.__install_requirements()
        run_cmd(f"sudo pacman -S {pkg}")

    def __install_requirements(self):
        requirements = [requirement() for requirement in self.requirements]
        for requirement in requirements:
            if not requirement.exists():
                requirement.install()

    def exists(self):
        return os.path.exists("/usr/bin/" + pkg) or os.path.exists("/bin/" + pkg)

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class AURPackage(Package):
    """Base class for AUR packages"""
    requirements = [yay] + requirements

    def install(self):
        self.__install_requirements()
        run_cmd(f"yay -S {pkg}")


class CustomPackage(Package):
    """Base class for custom packages"""
    def install(self):
        raise NotImplementedError


class zsh(Package):
    extras = [oh_my_zsh, powerlevel10k]
    config_files = ["welcome", "base", "util", "aliases", "keybinds"]
    output_location = "~/.zshrc"


class reflector(Package):
    output_location = "/etc/xdg/reflector/reflector.conf"


class yay(CustomPackage):

    requirements = [git, base_devel]

    def install(self):
        run_cmd("git clone https://aur.archlinux.org/yay-bin.git")
        run_cmd("cd yay-bin")
        run_cmd("makepkg -si")
        run_cmd("cd ..")
        run_cmd("rm -rf yay-bin")

class oh_my_zsh(CustomPackage):
    name = "oh-my-zsh"
    requirements = [zsh]

    def install(self):
        pass

class powerlevel10k(CustomPackage):

    requirements = [zsh, oh_my_zsh]

    def install(self):
        pass

class git(Package):
    pass


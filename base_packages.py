from util import run_cmd 

class Package:
    """Base class for packages"""
    name = ""               # Name of package
    requirements = []       # Packages required for this package to work
    extras = []             # Extra packages that can be installed
    post_requirements = []  # Packages that are required after installation
    config_directory = ""   # Directory where config files are stored
    config_files = []       # Files to be appended, ordered
    output_location = ""    # Output location of files

    to_install = True       # Whether or not to install this package
    is_installed = False    # Whether or not this package is installed

    _instance = None        # Singleton instance

    def __init__(self):
        if not self.name:
            self.name = self.__class__.__name__.lower()
        if not self.config_directory:
            self.config_directory = self.name
        self.__load_packages()

    def __clean_pkg_name(self, pkg):
        return pkg.replace("-", "_")
    
    def __load_packages(self):
        requirement_pkgs = [self.__clean_pkg_name(pkg) for pkg in self.requirements]
        extra_pkgs = [self.__clean_pkg_name(pkg) for pkg in self.extras]
        post_requirement_pkgs = [self.__clean_pkg_name(pkg) for pkg in self.post_requirements]

        self.requirements = [globals()[pkg] for pkg in requirement_pkgs]
        self.extras = [globals()[pkg] for pkg in extra_pkgs]
        self.post_requirements = [globals()[pkg] for pkg in post_requirement_pkgs]

    def __run_cmd(self, cmd):
        return run_cmd(cmd)

    def install(self):
        self.__install_requirements(self.requirements)
        run_cmd(f"sudo pacman -S {pkg}")
        self.__install_requirements(self.post_requirements)
        self.is_installed = True

    def __install_requirements(self, requirements):
        requirements = [requirement() for requirement in requirements]
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
    
    def __init__(self):
        self.__super().__init__()
        self.requirements = [yay] + self.requirements

    def install(self):
        self.__install_requirements()
        run_cmd(f"yay -S {pkg}")


class CustomPackage(Package):
    """Base class for custom packages"""
    def install(self):
        raise NotImplementedError

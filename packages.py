from base_packages import Package, AURPackage, CustomPackage

class oh_my_zsh(CustomPackage):
    name = "oh-my-zsh"
    requirements = ["zsh"]

    def install(self):
        pass

class zsh(Package):
    extras = ["oh-my-zsh", "powerlevel10k"]
    config_files = ["welcome", "base", "util", "aliases", "keybinds"]
    output_location = "~/.zshrc"


class reflector(Package):
    output_location = "/etc/xdg/reflector/reflector.conf"


class yay(CustomPackage):

    requirements = ["git", "base_devel"]

    def install(self):
        self.__run_cmd("git clone https://aur.archlinux.org/yay-bin.git")
        self.__run_cmd("cd yay-bin")
        self.__run_cmd("makepkg -si")
        self.__run_cmd("cd ..")
        self.__run_cmd("rm -rf yay-bin")


class powerlevel10k(AURPackage):

    requirements = ["zsh"]
    config_file = ["p10k.zshrc"]
    config_directory = "zsh"

    def install(self):
        pass


class git(Package):
    pass


class vivaldi(Package):
    post_requirements = ["vivaldi_ffmepg_codecs", "vivaldi_update_ffmepg_hook"]


class vivaldi_ffmepg_codecs(AURPackage):
    requirements = [vivaldi]


class vivaldi_update_ffmepg_hook(AURPackage):
    requirements = [vivaldi]

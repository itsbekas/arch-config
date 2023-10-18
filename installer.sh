ESSENTIAL_PACKAGES = "python"

# Update system and install essential packages
sudo pacman -Syu --noconfirm --needed $ESSENTIAL_PACKAGES

python ./installer.py

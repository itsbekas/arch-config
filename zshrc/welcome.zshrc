# Welcome user
echo "Welcome, $USER"

# Ask if the user wants to update the server (default to yes)
read -q "REPLY?Update packages? [Y/n] "
echo
if [[ $REPLY =~ ^[Yy]$ ]] ; then
    sudo pacman -Syu
fi

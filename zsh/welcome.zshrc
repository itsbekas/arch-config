# Welcome user
echo "Welcome, $USER"

# Ask if the user wants to update the server (default to yes) (use pacman)
# remember this is zsh, not bash
read -q "REPLY?Update server? [Y/n] "
echo
if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
    sudo pacman -Syu
fi
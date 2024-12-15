#!/bin/bash
clear
echo "Tails1154 Installer pre install script"
echo "Deleting existing venv (if it exists)"
rm -rf venv
echo "Creating venv..."
python3 -m venv venv
echo "Entering venv..."
. venv/bin/activate
echo "Upgrading pip..."
pip install --upgrade pip
echo "Installing Deps..."
pip install tk
echo "Select your linux distro"
echo "1) Arch based distro (tested)"
echo "2) Debian based distro (untested)"
read -p "?" distro
if [ $distro = '1' ]; then
	echo "Installing arch deps"
	sudo pacman -Syu --noconfirm cdrtools tk
	echo "Installed arch deps!"
elif [ $distro = '2' ]; then
	echo "Installing debian deps"
	sudo apt install -y cdrecord tk
else
	echo "Not a valid distro! exiting!"
	echo "Reverting changes"
	. venv/bin/deactivate
	deactivate
	rm -rf venv
	echo "Install failed."
	exit
fi
echo "Starting dvdburn..."
cd src
python3 dvdburn.py

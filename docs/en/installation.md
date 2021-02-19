# Installation

We use the following installation to ensure that all modules are working properly.

## Pre-Installation
Install python `version 3.7.3`  
We preferred `Miniconda3-4.6.14` in a seperate directory. Be free for using a installation via env.

    wget https://repo.anaconda.com/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh -O ./Miniconda3-4.6.14-Linux-x86_64.sh 

Check checksum sha:  https://docs.conda.io/en/latest/miniconda_hashes.html for Miniconda3-4.6.14-Linux-x86_64.sh **0d6b23895a91294a4924bd685a3a1f48e35a17970a073cd2f684ffe2c31fc4be**

    sha256sum ./Miniconda3-4.6.14-Linux-x86_64.sh
    
if the checksum is correct make the file executable

    chmod +x ./Miniconda3-4.6.14-Linux-x86_64.sh

start Miniconda installation
   
    ./Miniconda3-4.6.14-Linux-x86_64.sh
   
* View and accept the license terms.
* Leave installation location at the default or change it `~/miniconda3` or `~/miniconda3-py37`
* Do you wish the installer to initialize Miniconda3 by running conda init? no  
  (**no** means that bin path of the installation is not included in the system search path)

check installation (location=~/miniconda3-py37)::

    ~/miniconda3-py37/bin/python --version
    > Python 3.7.3 
    ~/miniconda3-py37/bin/pip  --version
    > pip 19.0.3 or higher
 
> **⚠ NOTE**  
> Do all of the following **pip / python / pigar / spyder3** calls with your installation location in front **~/miniconda3-py37/bin/**  
> to run it in the correct directory
  
## Installation from repository

Create a directory in which you want to copy the repository.  
Later the repository is created there as a new directory.
 
### Clone repository

1. On the main page of the repository above the list of files open button menu `Code`.
2. To clone the repository copy the url under HTTPS.
3. Open terminal and change the current working directory to the location of your created directory.

    git clone <paste url here>
    
### or download / unpack repository

1. On the main page of the repository above the list of files open button menu `Code`.
2. Download the whole code in a zip file by clicking the "Download Zip" button.
3. unpack the zip file to your created directory.

## Install modules and resources

Open Terminal and change the current working directory to the repository in your created directory.

Install modules used with the required versions

    <your miniconda binpath>/pip install -r requirements.txt
  
Download Javascript / CSS and Fonts to resources/vendor for weasyprint and offline using.

With installation script

    <your miniconda binpath>/python install-resources.py

Make materialdesignicons-webfont.ttf to be usable by all users

    sudo cp ./resources/vendor/fonts/materialdesignicons-webfont.ttf /usr/share/fonts/truetype/materialdesignicons_webfont.ttf

Font files should have the permission of 644

    sudo chmod 644 /usr/share/fonts/truetype/materialdesignicons_webfont.ttf

## first run

Run skeleton with default settings

    <your miniconda binpath>/python skeleton.py
    
or open spyder to edit and run skeleton

    <your miniconda binpath>/spyder

# additional informations

## run as service on linux ubuntu

Create a new service for skeleton::
    
    sudo nano /lib/systemd/system/skeleton.service

Content of skeleton.service with start after network is ready and group www-data::

    [Unit]
    Description=Python skeleton Service
    After=network.target
    
    [Service]
    Type=simple
    ExecStart=<your miniconda binpath>/python <your skeleton location>/skeleton.py --webserver
    WorkingDirectory=<your skeleton location>/
    Group=www-data
    StandardInput=tty-force
    
    [Install]
    WantedBy=multi-user.target

start/restart/stop your service

   sudo systemctl start skeleton.service
   sudo systemctl restart skeleton.service
   sudo systemctl stop skeleton.service

activate your service on system start::
   
   sudo systemctl enable skeleton.service

## install additional packages

Be sure that the new packages are compatible with the program

To install the latest version of a package

    <your miniconda binpath>/pip install <packagename>

To install a specific version, type the package name followed by the required version

    <your miniconda binpath>/pip install <packagename>==<version>
 
Update requirements.txt with additional packages by using `pigar` just this project in current directory:

Update requirements.txt

    <your miniconda binpath>/pigar --without-referenced-comments

Update requirements_upgrade.txt

    <your miniconda binpath>/pigar --without-referenced-comments -o '>=' -p ./requirements_upgrade.txt

## Update

Be sure that the new versions are compatible with the program

Update pip if necessary

    <your miniconda binpath>/pip install --upgrade pip
    
List outdated packages

    <your miniconda binpath>/pip list --outdated --format columns 
 
To upgrade an already installed package to the latest

    <your miniconda binpath>/pip install --upgrade sphinx
 
Upgrade everything from requirements_upgrade.txt by using

    <your miniconda binpath>/pip install -r requirements_upgrade.txt --upgrade

If you have a problem with a certain package stalling the upgrade (NumPy sometimes),  
just go to the directory ($), comment out the name (add a # before it) and run the upgrade again.  
You can later uncomment that section back. This is also great for copying Python global environments.


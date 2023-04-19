# Installation

We use the following installation on Ubuntu-Linux to ensure that all modules are working properly.

## Pre-Installation

Install [Miniconda3-py39_4.10.3](https://repo.anaconda.com/miniconda/) includes python `version 3.10.9` by following script.

    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh -O ./Miniconda3-py39_4.10.3-Linux-x86_64.sh

Check checksum sha:  https://docs.conda.io/en/latest/miniconda_hashes.html for Miniconda3-py39_4.10.3-Linux-x86_64.sh **1ea2f885b4dbc3098662845560bc64271eb17085387a70c2ba3f29fff6f8d52f**

    sha256sum ./Miniconda3-py39_4.10.3-Linux-x86_64.sh
    
if the checksum is correct make the file executable

    chmod +x ./Miniconda3-py39_4.10.3-Linux-x86_64.sh

start Miniconda installation
   
    ./Miniconda3-py39_4.10.3-Linux-x86_64.sh
   
* View and accept the license terms.
* Leave installation location at the default `~/miniconda3` or change it to `~/miniconda3-py310`
* Do you wish the installer to initialize Miniconda3 by running conda init? no  
  (**no** means that bin path of the installation is not included in the system search path)

check installation (location=~/miniconda3)::

    ~/miniconda3/bin/python --version
    > Python 3.10.9 
    ~/miniconda3/bin/pip  --version
    > pip 22.3.1 or higher
 
> **⚠ NOTE**  
> Do all of the following **pip / python / pipreqs / spyder3** calls with your installation location in front **~/miniconda3/bin/**  
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
  
With installation script download Javascript / CSS and Fonts to resources/vendor for weasyprint and offline using.

    <your miniconda binpath>/python install-resources.py

Make materialdesignicons-webfont.ttf to be usable in your system

    sudo cp ./resources/vendor/fonts/materialdesignicons-webfont.ttf /usr/share/fonts/truetype/materialdesignicons_webfont.ttf

Font files should have the permission of 644

    sudo chmod 644 /usr/share/fonts/truetype/materialdesignicons_webfont.ttf

## first run

Run skeleton with default settings

    <your miniconda binpath>/python skeleton.py
    
or open spyder to edit and run skeleton

    <your miniconda binpath>/spyder

On default installaton open [App-Skeleton](http://127.0.0.1:5000/) with your Webbrowser.
    
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
 
Update requirements.txt with additional packages by using `pipreqs` just this project in current directory:

Update requirements.txt

    <your miniconda binpath>/pipreqs --force

Update requirements_upgrade.txt

    <your miniconda binpath>/pipreqs --force --mode gt  --savepath requirements_upgrade.txt

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


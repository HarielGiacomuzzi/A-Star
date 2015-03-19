#!/bin/bash

cd ~

# Install python 2.7.3
wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz
tar vxzf Python-2.7.3.tgz
cd Python-2.7.3
PREFIX=$HOME/local/python-2.7.3
export LD_RUN_PATH=$PREFIX/lib
./configure --prefix=$PREFIX --enable-shared
make
make install

cd ~

export PATH=~/local/python-2.7.3/bin/:$PATH
echo "export PATH=~/local/python-2.7.3/bin/:$PATH" >> ~/.bash_profile
echo "export PATH=~/local/python-2.7.3/bin/:$PATH" >> ~/.bashrc

#/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:/usr/games:/facin/arm/bin:/facin/derby/bin

# Download SDL 1.2
apt-get download libsdl1.2-dev
ar p libsdl1.2-dev*.deb data.tar.xz | xz -d | tar x
wget -c https://github.com/pb82/sdl4racket/raw/master/lib/linux64/libSDL-1.2.so.0.11.4
mv libSDL-1.2.so.0.11.4 ~/usr/lib/x86_64-linux-gnu/

# Finally build and install pygame

#export PATH=$PATH:~/.local/share/bin
export PATH=$PATH:~/usr/bin
export LOCALBASE=~/usr
export LIBRARY_PATH=${LIBRARY_PATH}:~/usr/lib
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:~/usr/include/SDL
export CPLUS_INCLUDE_PATH=${CPLUS_INCLUDE_PATH}:~/usr/include/SDL/
export C_INCLUDE_PATH=${C_INCLUDE_PATH}:~/usr/include/SDL/
export CFLAGS="-L~/usr/lib"

hg clone https://bitbucket.org/pygame/pygame

cd pygame
python setup.py build
python setup.py install

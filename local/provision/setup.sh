#!/bin/bash

# host環境のセットアップ用shell

sudo apt update
sudo apt upgrade -y

sudo sudo timedatectl set-timezone Asia/Tokyo

echo 'install modules'
sudo apt install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
 "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
 $(lsb_release -cs) \
 stable"

sudo apt update

echo 'install docker'
sudo apt install -y docker-ce
sudo usermod -aG docker $USER
sudo curl -sL https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker network create prt_common

echo 'npm install start'
sudo apt install curl
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install npm@latest -g
sudo npm version

echo 'python install start'
sudo apt install -y python3-pip
python3 -V
sudo pip3 install luigi redis

echo 'redis install start'
sudo apt install -y redis
sudo apt install -y redis-tools

# hostマシンがWindowsなら--no-bin-linksが必要
# sudo npm install

# sudo reboot

echo 'setup.sh finished'
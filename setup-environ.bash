#!/bin/bash
set -e

sudo apt-get update
sudo apt-get install -y python-virtualenv python-dev libzmq-dev
virtualenv env
echo "source ~/env/bin/activate" >> .bashrc
source ~/env/bin/activate
pip install ipython[notebook]

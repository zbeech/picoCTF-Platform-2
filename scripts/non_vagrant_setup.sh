#!/bin/bash

# cd to the picoCTF-Platform-2 directory
# (This assumes this script is in picoCTF-Platform-2/scripts)
cd `dirname "$(readlink -f "$0")"`
cd ..

# Configure PICOCTF_HOME for subsequent invocations of devploy script
echo "export PICOCTF_HOME=`pwd`" >> /etc/profile

PICOCTF_HOME=`pwd` scripts/vagrant_setup.sh

#!/bin/bash
set -e
ROLE=$1

sudo apt-get update

sudo apt-get install apt-file build-essential -y
sudo apt-get install git -y

# vmachine
if [ ${ROLE} = "vmachine" ] ; then
  echo "virtual machine provisioning"



fi

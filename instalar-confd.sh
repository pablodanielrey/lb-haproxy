#!/bin/bash
wget https://github.com/kelseyhightower/confd/releases/download/v0.13.0/confd-0.13.0-linux-amd64
mv confd-0.13.0-linux-amd64 confd/confd
chmod +x confd/confd
#export PATH="$PATH:/opt/confd/bin"


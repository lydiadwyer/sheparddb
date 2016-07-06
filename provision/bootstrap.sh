#!/bin/bash

# set the session to be noninteractive
export DEBIAN_FRONTEND="noninteractive"

## Update the Aptitude cache
apt-get update



## Disable unneeded services
echo "INFO: Shutting down unused services..."
service rpcbind stop
service puppet stop
service chef-client stop

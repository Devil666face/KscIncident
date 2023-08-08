#!/bin/bash
# # sudo ln -s /usr/lib/x86_64-linux-gnu/libffi.so.8 /usr/lib/x86_64-linux-gnu/libffi.so.6
# VERSION=$(openssl version)
# SSL=$(echo $VERSION | awk '{print $2}')
# TGZ_NAME=""
# if [[ $SSL == "3.0.2" ]]
# then
# 	TGZ_NAME="py-3.11.4-openssl-3.0.2.tgz"
# else
# 	TGZ_NAME="py-3.11.4-openssl-1.1.1.tgz"
# fi
# echo $SSL $TGZ_NAME
# tar -xf .dev/$TGZ_NAME
# ./python/bin/python3.11 -m venv venv
tar -xf .dev/python-3.10.8-debian10.tgz
./python/bin/python3.10 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/pip install --no-index .dev/KlAkOAPI-1.0.0.0.tar.gz

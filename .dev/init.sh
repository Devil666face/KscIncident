#!/bin/bash
# sudo ln -s /usr/lib/x86_64-linux-gnu/libffi.so.8 /usr/lib/x86_64-linux-gnu/libffi.so.6
VERSION=$(openssl version)
SSL=$(echo $VERSION | awk '{print $2}')
TGZ_NAME="py-3.11.4-openssl-"
if [ "$SSL"="3.0.2" ]; then
	TGZ_NAME="$TGZ_NAME$SSL.tgz"
else
	TGZ_NAME=$(echo $TGZ_NAME"1.1.1.tgz")
fi
tar -xf .dev/$TGZ_NAME
./python/bin/python3.11 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/pip install --no-index .dev/KlAkOAPI-1.0.0.0.tar.gz

#!/bin/bash
tar -xf .dev/py-3.11.4-openssl-1.1.1.tgz
./python/bin/python3.11 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/pip install --no-index .dev/KlAkOAPI-1.0.0.0.tar.gz

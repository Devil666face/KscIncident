#!/bin/bash
./venv/bin/python -m nuitka \
--onefile \
--standalone \
--follow-imports \
main.py
ARCHIVE_NAME="${PWD##*/}.tgz"
tar -cvzf $ARCHIVE_NAME main.bin config.yaml.sample
mkdir -p ./dist && mv $ARCHIVE_NAME ./dist
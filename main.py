#!./venv/bin/python
from pathlib import Path
from os import (
    getcwd,
)
from api.server import KscServer
from utils.config import Config


BASE_DIR = Path(getcwd()).resolve()

if __name__ == "__main__":
    config = Config(BASE_DIR)
    for ip, username, password in zip(config.ip, config.username, config.password):
        server = KscServer(ip, username, password)
        server.events

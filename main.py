#!./venv/bin/python
from pathlib import Path
from os import (
    getcwd,
    path,
    getenv,
)
from api.server import KscServer
from dotenv import load_dotenv

BASE_DIR = Path(getcwd()).resolve()
load_dotenv(path.join(BASE_DIR, ".env"))

IP = getenv("KSC_SERVER_IP", "127.0.0.1")
USERNAME = getenv("KSC_USERNAME", "")
PASSWORD = getenv("KSC_PASSWORD", "")


if __name__ == "__main__":
    server = KscServer(ip=IP, username=USERNAME, password=PASSWORD)
    server.events

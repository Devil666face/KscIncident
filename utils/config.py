import yaml
from os import path
from typing import Any
from pathlib import Path
from utils.logger import logger as l


class Config:
    def __init__(self, BASE_DIR: Path, config_file_path: str = "config.yaml"):
        __file_path = path.join(BASE_DIR, config_file_path)
        self.config = self.__read_conf(__file_path)
        self.__parse_section("servers")

    def __read_conf(self, file_path) -> Any:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def __parse_section(self, section_name):
        for key, value in zip(
            self.config[section_name], self.config[section_name].values()
        ):
            setattr(self, key, value)
            if key != "password":
                l.debug(f"{key}:{value}")
        return self.config[section_name]

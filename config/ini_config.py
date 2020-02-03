#!/usr/bin/env python3.7

import configparser
import os

CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))

conf_parser = configparser.ConfigParser()
with open(os.path.join(CONFIG_PATH, 'config.ini'), 'r', encoding="utf-8") as cfg:
    conf_parser.read_file(cfg)


class Config:
    def __init__(self):
        for tag, dic in conf_parser.sections.items():
            for key, val in dic.items():
                self.__setattr__(key.upper(), val)


if __name__ == '__main__':
    config = Config()
    print(config.__dict__)


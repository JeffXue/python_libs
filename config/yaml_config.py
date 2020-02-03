#!/usr/bin/env python3.7

# Requirement：
# PyYAML==5.3

import yaml

CONFIG_PATH = './config.yml'

config = yaml.safe_load(open(CONFIG_PATH))


if __name__ == '__main__':
    import json
    print('config.yaml:', json.dumps(config, indent=4))



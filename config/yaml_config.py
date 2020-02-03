#!/usr/bin/env python3.7

# Requirement：
# PyYAML==5.3

import yaml

CONFIG_FILE = './config.yml'

config = yaml.safe_load(open(CONFIG_FILE))


if __name__ == '__main__':
    import json
    print('config.yaml:', json.dumps(config, indent=4))



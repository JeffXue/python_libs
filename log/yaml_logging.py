#!/usr/bin/env python3.7

# Requirement：
# PyYAML==5.3

import os
import logging.config

import yaml


def setup_logging(default_path='logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """设置logging配置，可以通过LOG_CFG变量指定配置文件
    如： LOG_CFG=my_logging.yaml python my_server.py
    """
    target_path = default_path
    env_yaml_path = os.getenv(env_key, None)
    if env_yaml_path:
        target_path = env_yaml_path
    if os.path.exists(target_path):
        with open(target_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == '__main__':

    setup_logging(default_level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    logger.debug('Debug Work!')
    logger.info('Info Work!')

    # 用于捕获异常
    try:
        open('/path/to/does/not/exist', 'rb')
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception as e:
        # logger.error('Failed to open file', exc_info=True)
        logger.exception('Failed to open file')

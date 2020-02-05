#!/usr/bin/env python3.7

import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s %(filename)s[%(funcName)s:%(lineno)d] %(levelname)-8s %(message)s'
LOG_FILE = 'debug.log'

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# 可通过 baseConfig 的方式添加配置
# logging.basicConfig(level=LOG_LEVEL,
#                     format=LOG_FORMAT,
#                     filename=LOG_FILE,
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filemode='a')

# 若不使用 baseConfig 的方式，也可以手动添加 FileHandler
# 若需要设置日志轮询，使用 RotatingFileHandler 或者 TimedRotatingFileHandler 替换 FileHandler
# file_handler = TimedRotatingFileHandler(LOG_FILE, when='D', backupCount=10)
# file_handler = RotatingFileHandler(LOG_FILE, maxBytes=10*1024*1024*1024, backupCount=10)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(file_handler)

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(console_handler)


if __name__ == '__main__':
    # 记录不同级别的日志
    logger.info('Start reading database')
    logger.debug('Update database records')

    # 用于捕获异常
    try:
        open('/path/to/does/not/exist', 'rb')
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception as e:
        logger.error('Failed to open file', exc_info=True)

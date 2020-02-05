#!/usr/bin/env python3.7

import logging


# 将logger封装成类，便于更灵活的使用不同的logger
class Logger:

    def __init__(self, filename, level):
        self.logger = logging.getLogger()
        if level == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        if level == 'INFO':
            self.logger.setLevel(logging.INFO)
        if level == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        if level == 'ERROR':
            self.logger.setLevel(logging.ERROR)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s '
                                      '-%(filename)s[%(funcName)s:%(lineno)d] '
                                      '- %(levelname)-8s '
                                      '- %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


def test():
    test_logger = Logger('test.log', 'WARNING')
    test_logger.logger.warning('testing')


if __name__ == '__main__':
    test()

#!/usr/bin/env python3.7

# Requirement：
# records==0.5.3
# 采用第三库 records 可快速对mysql进行查询，若只有查询数据库操作，采用 records 库是较好的选择
import os

import records

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOSTS = os.getenv('MYSQL_HOSTS')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

db = records.Database(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTS}/{MYSQL_DATABASE}?charset=utf8')


if __name__ == '__main__':
    rows = db.query("select * from names")



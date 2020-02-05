#!/usr/bin/env python3.7

# Requirement：
# PyMySQL==0.9.3

import pymysql


class MySQLConnector:
    """
    提供mysql数据库相关sql操作方法： query, insert, update
    对于采用sql的方式操作更加便捷
    注意：需要手工关闭数据库
    """

    def __init__(self, host, user, password, database, port):
        self.db = pymysql.connect(host, user, password, database, port,
                                  charset="utf8")
        self.host = host
        self.username = user
        self.password = password
        self.database = database

    def reconnect(self):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database,
                                  charset="utf8")

    def close(self):
        self.db.close()

    def query(self, sql):
        result = []
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except (AttributeError, pymysql.OperationalError):
            self.reconnect()
            cursor = self.db.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            self.db.rollback()
        finally:
            cursor.close()
        return result

    def insert(self, sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except (AttributeError, pymysql.OperationalError):
            self.reconnect()
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
        finally:
            cursor.close()

    def update(self, sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except (AttributeError, pymysql.OperationalError):
            self.reconnect()
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
        finally:
            cursor.close()

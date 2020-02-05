#!/usr/bin/env python3.7

# Requirement：
# SQLAlchemy==1.3.13

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOSTS = os.getenv('MYSQL_HOSTS')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')


# max_overflow: 超过连接池大小之后，允许最大扩展连接数
# pool_size: 连接池大小
engine = create_engine(
    f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTS}/{MYSQL_DATABASE}?charset=utf8',
    max_overflow=2,
    pool_size=5)

DBSession = sessionmaker(bind=engine)


if __name__ == '__main__':
    from sqlalchemy import Column, String
    from sqlalchemy.ext.declarative import declarative_base

    # 创建对象的基类:
    Base = declarative_base()

    class User(Base):

        __tablename__ = 'user'

        # 表的结构:
        id = Column(String(20), primary_key=True)
        name = Column(String(20))

    session = DBSession()
    new_user = User(id='5', name='Bob')
    session.add(new_user)
    session.commit()

    user = session.query(User).filter(User.id == '5').one()
    user.name = 'new name'
    session.commit()

    session.delete(user)
    session.commit()

    session.close()



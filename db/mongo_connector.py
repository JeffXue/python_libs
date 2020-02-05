#!/usr/bin/env python3.7

# Requirement：
# mongoengine==0.19.1

import os

from mongoengine import connect
from mongoengine import Document, StringField, BooleanField, DictField, ListField


connect(host=os.getenv('MONGO_HOST', 'localhost'),
        port=int(os.getenv('MONGO_PORT', 27017)),
        db=os.getenv('MONGO_DATABASE', 'test'))


if __name__ == '__main__':
    class TestDemo(Document):
        meta = {
            'collection': 'test',
            'db_alias': 'db.test',
        }

        name = StringField(required=True, help_text='名称')
        status = BooleanField(required=True, help_text='用例状态')
        detail = DictField()
        logs = ListField()

    data = TestDemo.objects(name='test').first()
    data.status = True
    data.update()

    new_data = TestDemo(name='new record', status=False)

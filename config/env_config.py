#!/usr/bin/env python3.7

# Requirement：
# django-environ==0.4.5

import os

from environ import Env


env = Env()

# 通过环境变量获取到配置文件名
env_file = f'env.{env.str("PROJECT_ENV")}'

# 通过环境变量获取配置路径，并加载配置
if 'CONFIG_PATH' in env:
    env_file_path = os.path.join(env.get_value('CONFIG_PATH'), env_file)
    assert os.path.exists(env_file_path), f'{env_file_path} do not exists'
    env.read_env(env_file_path)
else:
    env_file_path = env_file
    env.read_env(env_file_path)

if __name__ == '__main__':
    print(env.str('agent_user'))
    print(env.str('corp_user'))


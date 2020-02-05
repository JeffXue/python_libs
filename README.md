# python 工具库
python的脚本，每个脚本包括一个或多个方法，实现相关的功能

# 约定
在每个脚本的开始会包括说明依赖的python版本和其他工具库版本

```
#!/usr/bin/env python3.7

# 依赖版本说明
# requests==2.22.0

import requests

def example_function(param1, param2):
    """
    reST风格注释

    :param1: 第一个参数
    :param2: 第二个参数描述
    :returns: 返回值描述
    :raises keyError: 异常描述
    """

    pass


```

---

# 隔离环境：虚拟环境
virtualenv 是一个创建隔绝的Python环境的 工具。virtualenv创建一个包含所有必要的可执行文件的文件夹，用来使用Python工程所需的包

若对于本地集中式管理python虚拟环境，可以使用conda: [Create virtual environments for python with conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
```
# 安装virtualenv
pip install virtualenv

# 创建一个虚拟环境
cd your_project_folder
virtualenv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖包
pip install requests

# 记录环境依赖，能帮助确保安装、部署和开发之间的一致性
pip freeze > requirements.txt

# 退出虚拟环境
deactivate

```

---

# 库说明

- `structure`: 包括常规了目录结构样式
- `config`: 包括ini、环境变量、yaml三种配置方式
- `log`: 包括logging模块常规使用方式和yaml配置日志方式
- `db`: 包括了mysql（pymysql、records、sqlalchemy）和mongodb的连接方式
- `time_utils.py`: 常用的一些时间操作方法
- `sys_utils.py`: 常用的操作系统操作方法
- `calculate_utils.py`: 常用的计算方法
- `whyemail.py`: 发送邮件

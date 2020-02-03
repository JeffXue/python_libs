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
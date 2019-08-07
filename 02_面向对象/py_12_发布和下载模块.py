# -----------------------------------知识点------------------------------------------
'''
1.发布模块
    1) 在包下创建 setup.py文件

        from distutils.core import setup

        setup(name="hm_message",  # 包名
              version="1.0",  # 版本
              description="itheima's 发送和接收消息模块",  # 描述信息
              long_description="完整的发送和接收消息模块",  # 完整描述信息
              author="itheima",  # 作者
              author_email="itheima@itheima.com",  # 作者邮箱
              url="www.itheima.com",  # 主页
              py_modules=["hm_message.send_message",
                          "hm_message.receive_message"])

        有关字典参数的详细信息，可以参阅官方网站：
        https://docs.python.org/2/distutils/apiref.html

    2) 构建模块(在终端中执行-->windows下还不清楚)
    $ python3 setup.py build

    3) 生成发布压缩包
    $ python3 setup.py sdist

    注意：要制作哪个版本的模块，就使用哪个版本的解释器执行！

3,安装和卸载模块
    安装:
    $ tar -zxvf hm_message-1.0.tar.gz
    $ sudo python3 setup.py install

    卸载:
    直接从安装目录下，把安装模块的目录删除就可以
    $ cd /usr/local/lib/python3.5/dist-packages/
    $ sudo rm -r hm_message*

3.pip 安装第三方模块

        第三方模块 通常是指由 知名的第三方团队 开发的 并且被 程序员广泛使用 的 Python 包 / 模块
            例如 pygame 就是一套非常成熟的 游戏开发模块
            pip 是一个现代的，通用的 Python 包管理工具
            提供了对 Python 包的查找、下载、安装、卸载等功能

    安装和卸载命令如下：
                    pip install 模块名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com    -->(国内地址 )
    # 将模块安装到 Python 2.x 环境
    $  pip install pygame
    $  pip uninstall pygame

    # 将模块安装到 Python 3.x 环境
    $  pip3 install pygame
    $  pip3 uninstall pygame

'''
print("看了看 什么也没有")
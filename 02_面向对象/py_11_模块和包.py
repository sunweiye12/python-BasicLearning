# -----------------------------------知识点-------------------------------------------
'''
1.模块的概念
    1>.每一个以扩展名 py 结尾的文件都是一个模块
    2>.模块名 同样也是一个标识符，需要符合标识符的命名规则
    3>.在模块中定义的 全局变量 、函数、类 都是提供给外界直接使用的工具
    4>.模块就好比是工具包，要想使用这个工具包中的工具，就需要先导入这个模块
    导入方式:
        import 模块名1, 模块名2
        或:
        import 模块名1      --->    每个导入应该独占一行
        import 模块名2
        import 模块名1 as 模块别名    ---->    模块别名应该符合:大驼峰命名法
            # 从模块导入某一个工具(这样导入后直接 方法. 调用)  --> (不推荐使用,因为重名时没有提示)
        from 模块名1 import 工具名

    导入后使用(全局变量、函数、类等工具):

        一般直接  模块名.变量/函数/类   来使用
        ***注意: 1.如果两个模块，存在同名的函数，那么后导入模块的函数，会覆盖掉先导入的函数 --重要
                 2.开发时 import 代码应该统一写在代码的顶部，更容易及时发现冲突
                 3.一旦发现冲突，可以使用 as 关键字给其中一个工具起一个别名

        模块搜索顺序:搜索当前目录指定模块名的文件，如果有就直接导入,如果没有，再搜索系统目录

        一个 独立的 Python 文件 就是一个 模块
        在导入文件时，文件中所有没有任何缩进的代码都会被执行一遍！

    **__name__ 属性

        __name__ 属性可以做到，测试模块的代码 只在测试情况下被运行，而在 被导入时不会被执行！
        __name__ 是 Python 的一个内置属性，记录着一个字符串
            如果是被其他文件导入的，其内部__name__ 显示的是 模块名
            如果是当前执行的程序 __name__ 显示的是 __main__   --->   用来做测试(可以解决,都执行的问题)
            # 导入模块
            # 定义全局变量
            # 定义类
            # 定义函数

            # 在代码的最下方
            def main():
                # ...
                pass

            # 根据 __name__ 判断是否执行下方代码
            if __name__ == "__main__":
                main()


2.包的概念
    1>.包是一个包含多个模块的特殊目录,
    2>.目录下有一个 特殊的文件 __init__.py(目前需要自己建立)  -->  创建一个python Package就可以
    3>.包名的命名方式和变量名一致，小写字母加 _
    要求:__init__.py
        要在外界使用包中的模块，需要在 __init__.py 中指定 对外界提供的模块列表
          例如:  # 从当前目录导入模块列表
                from . import send_message
                from . import receive_message


    包的调用: 报名.模块名.方法名

    好处: 使用 import 包名可以一次性导入包中所有的模块

3.发布模块
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

4,安装和卸载模块
    安装:
    $ tar -zxvf hm_message-1.0.tar.gz
    $ sudo python3 setup.py install

    卸载:
    直接从安装目录下，把安装模块的目录删除就可以
    $ cd /usr/local/lib/python3.5/dist-packages/
    $ sudo rm -r hm_message*






'''
# -----------------------------------练习-------------------------------------------
print("# ----------------------------模块导入------------------------------------")
from random import randint

print(randint(20, 30))

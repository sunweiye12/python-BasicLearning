# -----------------------------------知识点-------------------------------------------
'''
********
单例设计模式
    目的 :让类创建的对象，在系统中只有唯一的一个实例
          每一次执行 类名() 返回的对象，内存地址是相同的
单例模式的实现:
    1.定义一个类属性，初始值是 None，用于记录单例对象的引用
    2.重写 __new__ 方法
    3.如果 类属性 is None，调用父类方法分配空间，并在类属性中记录结果
    4.返回 类属性 中记录的 对象引用



    在每次使用 类名() 创建对象时，Python 的解释器都会自动调用两个方法：
        __new__ 分配空间
        __init__ 对象初始化
    但在单例模式中 __new__ 方法改造之后，每次都会得到 第一次被创建对象的引用
    但是：初始化方法还会被再次调用 --->  那么如何让让 初始化动作只被执行一次???

解决办法:
    1.定义一个类属性 init_flag 标记是否执行过初始化动作，初始值为 False
    2.在 __init__ 方法中，判断 init_flag，如果为 False 就执行初始化动作
    3.然后将 init_flag 设置为 True
    4.这样，再次自动 调用 __init__ 方法时，初始化动作就不会被再次执行 了


********

'''
# -----------------------------------练习-------------------------------------------
print("-----------------------------------单例模式-------------------------------------------")


class MusicPlayer(object):

    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance

print("-----------------------------------初始化一次-------------------------------------------")


class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        '''重写创建方法'''

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        '''重写初始化方法'''

        if not MusicPlayer.init_flag:
            print("初始化音乐播放器")

            MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


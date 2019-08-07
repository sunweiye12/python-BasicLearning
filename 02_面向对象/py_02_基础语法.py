# -----------------------------------知识点-------------------------------------------
"""
1.内置函数( __方法名__ 格式的方法是 Python 提供的 内置方法 / 属性):一下是常用的内置方法
        01 	__new__ 	方法 	创建对象时，会被 自动 调用
        02 	__init__ 	方法 	对象被初始化时，会被 自动 调用
        03 	__del__ 	方法 	对象被从内存中销毁前，会被 自动 调用
        04 	__str__ 	方法 	返回对象的描述信息，print 函数输出使用(类似于 toString 函数)
2.定义简单的类
        1.类名的命名规则要符合大驼峰命名法
        2.方法格式和之前学习的函数一样,区别在于第一个参数必须是 self(***)
        格式如下:
            class 类名:
                def 方法1(self, 参数列表):
                    pass
                def 方法2(self, 参数列表):
                    pass

        3.方法中的self参数
            在类封装的方法内部，self 就表示当前调用方法的这个对象(就相当于this)

        4.初始化方法( __init__) ---> 属性的定义
            1>.使用类名()创建对象时，会自动执行初始方法,并对象在内存中分配空间
            2>.在初始化方法内部定义属性
            格式如下:
            class Cat:
                def __init__(self, name):
                    print("初始化方法 %s" % name)
                    self.name = name

            tom = Cat("Tom")

            lazy_cat = Cat("大懒猫")

        5.创建对象     格式:
                对象变量 = 类名()
                对象变量 = 类名(arge)  参数自动传递到初始方法中(****ß)
"""
# -----------------------------------练习-------------------------------------------
print("-----------------------------------类的定义(方法)-------------------------------------------")


#  定义一个类
class Cat:

    #    name = None                 #  设置类的属性(在初始化方法中定义了name 属性,因此此处可以省去声明)

    def __init__(self, name=""):  # 内置方法,在创建对象的时候自动调用
        print("初始化方法")
        self.name = name  # 设置类的属性

    def eat(self):  # 设置类的方法
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

    def __str__(self):  # 相当于toString的方法
        return "我是小猫：%s" % self.name


# Cat.name = "tom123" #  在类的外面给类添加字段(非常不推荐在类的外部给对象增加属性 )

# 创建猫1对象
tom = Cat("tom")
# tom.name = "tom"
tom.eat()
tom.drink()
print(tom)

# 创建猫2对象
rose = Cat()
rose.name = "rose"
rose.eat()
rose.drink()
print(rose)

print("-----------------------------------类的定义(属性)-------------------------------------------")


class Cat:
    def __init__(self, name=""):  # 相当于构造方法(每个参数都设置初始值,保证在创建对象的时候不传参数也可以)
        print("初始化方法 %s" % name)
        self.name = name

    def drink(self):
        print("%s 要喝水" % self.name)


# 生成对象
tom = Cat("Tom")    # 传递传递参数  Tom
lazy_cat = Cat("大懒猫")   # 传递参数  大懒猫
rose = Cat()    # 没有传递参数    默认为 ""

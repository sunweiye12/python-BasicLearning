# -----------------------------------知识点-------------------------------------------
"""
    封装是面向对象编程的一大特点
    1.面向对象编程的第一步 —— 将 属性和方法 封装 到一个抽象的 类 中
    2.外界使用类创建对象，然后让对象调用方法
    3.对象方法的细节都被封装在 类的内部
"""
# -----------------------------------练习-------------------------------------------
'''
需求
    小明 体重 75.0 公斤
    小明每次 跑步 会减肥 0.5 公斤
    小明每次 吃东西 体重增加 1 公斤
'''


class Person:
    """定义类对象Person"""

    def __init__(self, name="", weight=0):  # 定义属性的过程中提供默认值
        """定义属性"""
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        """跑步"""
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃东西"""
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)

xiaoming.run()
xiaoming.eat()
xiaoming.eat()

print(xiaoming)

print("----------------分界线-----------------")

xiaomei = Person("小美", 45)

xiaomei.run()
xiaomei.run()
xiaomei.eat()
xiaomei.run()
xiaomei.run()

print(xiaomei)
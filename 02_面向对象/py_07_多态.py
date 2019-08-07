# -----------------------------------知识点-------------------------------------------
"""
多态的设计目的:不同的子类对象调用相同的父类方法，产生不同的执行结果(不同对象执行的时候,结果不同)
多态(增加代码的灵活度)
    1.要有继承关系
    2.要有方法的重写
    3.调用父类的方法(若子类中重写了此方法,当传入子类对象时,会执行子类的方法)
"""


class Animal(object):
    """设计父类"""

    def __init__(self, name=None):
        self.name = name    # 定义一个属性

    def game(self):
        """定义一个方法"""
        print("动物玩耍")


class Dog(Animal):
    """子类Dog,并重写方法"""
    def game(self):
        print("狗吃骨头玩")


class Cat(Animal):
    """子类Cat,并重写方法"""
    def game(self):
        print("猫吃鱼玩")


class Person(object):
    """定义一个类,里面存在的方法来调用父类方法"""
    def __init__(self, name=None):
        self.name = name

    def game_with_animal(self, animal):
        animal.game()


def play(animal):
    """定义一个方法,调用父类方法"""
    animal.game()

if __name__ == '__main__':

    # 1.创建对象
    animal = Animal()
    dog = Dog()
    cat = Cat()

    # 2. 创建一个小明对象
    xiaoming = Person("小明")

    # 3. 让小明调用和动物玩的方法
    xiaoming.game_with_animal(animal)
    xiaoming.game_with_animal(dog)
    xiaoming.game_with_animal(cat)
    print("-" * 50)
    play(animal)
    play(dog)
    play(cat)

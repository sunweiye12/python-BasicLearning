# -----------------------------------知识点-------------------------------------------
"""
创建出来的 对象 叫做 类 的 实例
创建对象的 动作 叫做 实例化
对象的属性 叫做 实例属性
对象调用的方法 叫做 实例方法
(*****
    每一个对象都有自己独立的内存空间，保存各自不同的属性
    多个对象的方法，在内存中只有一份，在调用方法时，需要把对象的引用传递到方法内部
*****)
1.类属性(**相当于是静态变量**)
    类属性就是给类定义的属性,通常用来记录与这个类相关的特征类,不会用于记录具体对象的特征
    定义方法:
        直接在类下定义 count = 0
    调用方法:
        类名.类属性名          ----> 见例子
        对象.类属性名          (查询顺序:首先在=对象中查找属性-->如果没有就查找类的属性)
        注意:如果使用 对象.类属性名 = 值 赋值语句，只会给对象添加一个属性(如果原来有这个属性就赋值)，而不会影响到类属性的值

2.实例属性(**是指在在 __init__方法中定义的属性 **)
    创建实例的时候通过,初始化方法 __init__ 为对象初始化(并创建实例属性)  -->  创建出来的实例都拥有
    也可以通过,对象.属性名 = 值  为此对象添加属性   ----->  只有此实例拥有

3.类方法(**用于调用类的方法和属性**)
    类方法就是针对对象定义的方法,在类方法内部可以直接访问 类属性(不可以访问实例属性) 也可以调用其他的类方法
    语法如下:
        @classmethod              类方法需要用修饰器 @classmethod 来标识，告诉解释器这是一个类方法
        def 类方法名(cls):          类方法的第一个参数应该是 cls 相当于 self  (惯使用cls 其他名称也可以)
            pass

    调用方法:
        类名. 调用   类方法，调用方法时，不需要传递 cls 参数
        在方法内部可以通过 cls. 访问类的属性,也可以通过 cls. 调用其他的类方法

4. 静态方法
    如果需要在类中封装一个方法，这个方法：
        既不需要访问实例属性或者调用实例方法
        也不需要访问类属性或者调用类方法

    语法如下:
        @staticmethod          需要用 修饰器 @staticmethod 来标识，告诉解释器这是一个静态方法,静态方法不能被调用,只能被继承
        def 静态方法名():        通过 类名. 调用 静态方法
            pass
"""

# -----------------------------------练习-------------------------------------------
import random
print("-----------------------------------类属性-------------------------------------------")


class Tool(object):
    # 使用赋值语句，定义类属性，记录创建对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        # 针对类属性做一个计数+1
        Tool.count += 1  # 必须通过 类名.属性名 来进行调用类属性


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

tool1.age = 10  # 可以在外面给对象增加一个属性
print(tool1.age)

# 知道使用 Tool 类到底创建了多少个对象?
print("现在创建了 %d 个工具" % Tool.count)

print("-----------------------------------类方法-------------------------------------------")


class Cat(object):
    # 猫对象计数
    cat_count = 0

    @classmethod
    def run(cls):
        # 不能访问实例属性只能访问类属性的方法
        print("%d 只猫在跑..." % cls.cat_count)

    def __init__(self, name):
        self.name = name  # 定义实例属性
        Cat.cat_count += 1  # 调用类属性,使得数量加1


# 创建一个实例
cat = Cat("仙茅")
cat = Cat("仙茅1")

# 调用类方法
Cat.run()

print("-----------------------------------静态方法-------------------------------------------")


class Dog(object):
    # 狗对象计数
    dog_count = 0

    @staticmethod   # 实际使用中很少,和对象方法差异不大
    def run():
        # 不需要访问实例属性也不需要访问类属性的方法
        print("狗在跑...")

    def __init__(self, name):
        self.name = name


# 调用静态方法
Dog.run()

'''
需求
    设计一个 Game 类
    属性：
        定义一个 类属性 top_score 记录游戏的 历史最高分
        定义一个 实例属性 player_name 记录 当前游戏的玩家姓名
    方法：
        静态方法 show_help 显示游戏帮助信息
        类方法 show_top_score 显示历史最高分
        实例方法 start_game 开始当前玩家的游戏
    主程序步骤
        1) 查看帮助信息
        2) 查看历史最高分
        3) 创建游戏对象，开始游戏
'''
print("-----------------------------------综合实例-------------------------------------------")


class Game(object):
    # 游戏最高分，类属性
    top_score = 0

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸走进房间")

    @classmethod
    def show_top_score(cls):
        # print(cls.player_name)
        print("游戏最高分是 %d" % cls.top_score)

    def __init__(self, player_name = ""):
        """初始化方法,定义对象属性"""
        self.player_name = player_name

    def start_game(self):
        """对象方法"""
        print("[%s] 开始游戏..." % self.player_name)

        # 使用类名.修改历史最高分(随机获得)
        Game.top_score = random.randint(80, 100)


class Game1(Game):
    """创建一个子类"""
    def pep(self):
        pass


game = Game1()

# 1. 查看游戏帮助 (调用静态方法)
Game.show_help()

# 2. 查看游戏最高分(**调用的是类方法,因为需要访问,类属性**)
Game.show_top_score()

# 3. 创建游戏对象，开始游戏
game = Game("小明")

game.start_game()

# 4. 游戏结束，查看游戏最高分
Game.show_top_score()

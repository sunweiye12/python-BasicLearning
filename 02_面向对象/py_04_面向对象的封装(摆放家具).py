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
    1.房子(House) 有 户型、总面积 和 家具名称列表
        新房子没有任何的家具
    2.家具(HouseItem) 有 名字 和 占地面积，其中
        席梦思(bed) 占地 4 平米
        衣柜(chest) 占地 2 平米
        餐桌(table) 占地 1.5 平米
    3.将以上三件 家具 添加 到 房子 中
    4.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
'''
'''
应该先开发家具类
    1.家具简单
    2.房子要使用到家具，被使用的类，通常应该先开发
'''
'''
家具类
    属性 name area
    方法 _str_
'''


class HouseItem:
    """创建家具的类"""
    def __init__(self, name=None, area=None):  # 设置属性参数并添加默认值
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 的占地面积为: %.1f平方米" % (self.name, self.area)


# 1. 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

'''
房子类
    属性 house_type area free_area item_list
    方法 add_item() _str_  _init_
'''


class House:
    """创建房子类"""
    def __init__(self, house_type=None, area=None):
        self.house_type = house_type
        self.area = area
        self.free_area = area   # 定义了四个属性 --> 此处为空闲面积,初始化空闲面积就为户型的面积
        self.item_list = []     # 初始化家具列表

    def add_item(self, item):   # 定义一个添加家具的方法
        self.free_area -= item.area
        self.item_list.append(item.name)

    def __str__(self):
        print("-" * 50)
        return "房子的类型为:%s\n房子的总面积为:%.1f\n房子的剩余面积为:%.1f\n房子中的家具有:%s\n\t" \
               % (self.house_type, self.area, self.free_area, self.item_list)


house = House("两室一厅", 90)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
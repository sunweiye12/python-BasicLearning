# -*- coding: UTF-8 -*-
# ----------------------------------------知识点------------------------------------------------------
"""
返回值:
    1.函数返回多个值是以元组的方式返回
参数:
    1.在函数内部，针对参数使用赋值语句，不会影响调用函数时传递的实参变量(无论可变还是不可变 )--->重点是 赋值语句
    2.如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据---->重点是 方法
    3.缺省参数
        可以给某个参数指定一个默认值(如果没有传入此值,就会执行默认值)
    4.多值参数
        有时可能需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用 多值参数
        参数名前增加 一个 * 可以接收 元组    *args
        参数名前增加 两个 * 可以接收 字典    **kwargs      方法名 def demo(num, *args, **kwargs):
    5.元组和字典的拆包
        - 在 元组变量前，增加 一个 *   (详见练习)
        - 在 字典变量前，增加 两个 *

函数的递归
    一个函数内部调用自己(参数满足一个条件时，函数不再执行.这个非常重要，通常被称为递归的出口，否则会出现死循环！)
"""

if __name__ == '__main__':

    # -------------------------------------练习:返回值-------------------------------------------
    print("-----------------------------------返回值---------------------------------------------------------")

    def measure():
        """返回当前的温度"""
        print("开始测量...")
        temp: int = 39
        wetness: int = 10
        print("测量结束...")

        return temp, wetness
        # return (temp, wetness)  # 如果一个函数返回的是元组，括号可以省略(如上所示)


    # - 在 Python 中，可以 将一个元组 使用 赋值语句 同时赋值给 多个变量
    # - 注意：变量的数量需要和元组中的元素数量保持一致

    result = measure()  # 第一种接受返回值的方式
    temp, wetness = measure()  # 第二种接受返回值的方式

    print(result)
    print(temp)
    print(wetness)

    # --------------------------------------------------------------------------------------------
    # 在函数内部，针对参数使用赋值语句，不会影响调用函数时传递的实参变量(无论可变还是不可变 )(使用赋值语句)
    print("------------------------------------------参数--------------------------------------------------")


    def demo(num, num_list):
        print("函数内部")
        # 赋值语句
        num = 200
        num_list = [1, 2, 3]
        print(num)
        print(num_list)
        print("函数代码完成")


    gl_num = 99
    gl_list = [4, 5, 6]
    demo(gl_num, gl_list)
    print(gl_num)
    print(gl_list)

    # --------------------------------------------------------------------------------------------
    # 如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据(使用方法)
    print("--------------------------------------------------------------------------------------------")


    def mutable(num_list):
        # num_list = [1, 2, 3]
        num_list.extend([1, 2, 3])
        print(num_list)


    gl_list = [6, 7, 8]
    mutable(gl_list)
    print(gl_list)

    # --------------------------------------------------------------------------------------------
    print("-----------------------------------缺省参数---------------------------------------------------------")


    def print_info(name, title="", gender=True):  # 此处title默认为空 gender默认为True
        """
        :param title: 职位
        :param name: 班上同学的姓名
        :param gender: True 男生 False 女生
        """

        gender_text = "男生"

        if not gender:
            gender_text = "女生"

        print("%s %s 是 %s" % (name, title, gender_text))


    # 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
    print_info("小明")
    print_info("老王", title="班长")
    print_info("小美", gender=False)
    # --------------------------------------------------------------------------------------------
    print("-----------------------------------多值参数---------------------------------------------------------")


    def demo(num, *args, **kwargs):
        print(num)
        print(args)
        print(kwargs)


    demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)  # 调用函数

    '''
    1. 定义一个函数 sum_numbers，可以接收的 任意多个整数
    2. 功能要求：将传递的 所有数字累加 并且返回累加结果
    '''
    print("-------------------------------------")


    def sum_numbers(*args):
        num = 0
        # 遍历 args 元组顺序求和
        for n in args:
            num += n

        return num


    print(sum_numbers(1, 2, 3, 7, 1, 1))

    # --------------------------------------------------------------------------------------------
    print("-----------------------------------元组和字典的拆包---------------------------------------------------")


    def demo(*args, **kwargs):
        print(args)
        print(kwargs)

    # 需要将一个元组变量/字典变量传递给函数对应的参数
    gl_nums = (1, 2, 3)
    gl_xiao_ming = {"name": "小明", "age": 18}

    # 如果这样写会把 gl_nums 和 gl_xiaoming 作为元组传递给第一个元素 args  (会认为传递的是元组包含了这两个元素)
    demo(gl_nums, gl_xiao_ming)
    demo(*gl_nums, **gl_xiao_ming)  # 这样证明了gl_nums是传递给第一个元组  gl_xiaoming为了传递给第一个字典(!!!要注意!!!!)


    # --------------------------------------------------------------------------------------------
    print("-----------------------------------函数递归---------------------------------------------------------")
    '''
    需求
    1. 定义一个函数 sum_numbers
    2. 能够接收一个 num 的整数参数
    3. 计算 1 + 2 + ... num 的结果
    '''


    def sum_numbers(num):
        if num == 1:
            return 1

        # 假设sum_numbers能够完成num - 1的累加
        # temp = sum_numbers(num - 1)

        # 函数内部的核心算法就是两个数字的相加
        # return num + temp
        return num + sum_numbers(num - 1)  # 上面两个算法的结合
    print(sum_numbers(3))

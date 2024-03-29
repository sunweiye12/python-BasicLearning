# -*- coding: UTF-8 -*-
# ----------------------------------------练习 -->  名片管理系统------------------------------------------------------
"""
系统需求

- 1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单

    **************************************************
    欢迎使用【名片管理系统】V1.0

    1. 新建名片
    2. 显示全部
    3. 查询名片

    0. 退出系统
    **************************************************

- 2. 用户用数字选择不同的功能
- 3. 根据功能选择，执行不同的功能
- 4. 用户名片需要记录用户的 姓名、电话、QQ、邮件
- 5. 如果查询到指定的名片，用户可以选择 修改 或者 删除 名片

"""
# ----------------------------------------------------------欢迎界面------------------------------------------------------------


def show_menu():
    """
        展示主页信息
        :return:null
        """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0\n\t")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片\n\t")
    print("0. 退出系统")
    print("*" * 50)


# ----------------------------------------------------------创建名片------------------------------------------------------------


def new_card(cards):
    """
    创建一个名片信息
    :return:cards
    1.所有名片存放到一个list列表中,每一个名片是一个字典,list中每一个字典元素的名字是字典元素中name的名字
    2.获取卡包(卡包在程序开始的时候就已经创建)
    3.设置字典中包含的字段
    4.生成一个名为name值的字典,将每个字段添加到字典中
    5.判断列表中是否存在此字典,如果不存在,将字典保存到list中,如果存在,提示一下是否覆盖
    """
    print("-" * 20 + "欢迎新建名片" + "-" * 20)
    # 输入需求字段
    print("创建一个新名片:")
    姓名 = input("姓名:")
    name = 姓名
    电话 = input("电话:")
    QQ = input("QQ:")
    邮件 = input("邮件:")
    # 创建字典
    姓名 = {}
    姓名["姓名"] = name
    姓名["电话"] = 电话
    姓名["QQ"] = QQ
    姓名["邮件"] = 邮件

    # 将字典存到list中
    if cards.count(姓名) == 0:
        cards.append(姓名)
        print("保存成功!!!")
        return cards
    else:
        while True:
            num_repeat = cards.count(姓名)
            # TODO 在此处应该保留一个重新修改的选项
            num = input("名片中已存在此人,是否覆盖:(1:继续保存 2:覆盖)")
            if num in ["1", "2"]:
                if num == "1":
                    # 继续保存有重复名字的名片
                    cards.append(姓名)
                    print("继续保存成功,现在有%d个此名片!!!" % (num_repeat + 1))
                    return cards
                    break
                else:
                    # 删除所有重名的名片,只保留刚添加的名片
                    i1 = 0
                    while i1 <= cards.count(姓名):
                        cards.remove(姓名)
                        i1 += 1
                    cards.append(姓名)
                    print("覆盖成功%d个名片!!!" % num_repeat)
                    return cards
                    break
            else:
                print("输入有误!")


# ----------------------------------------------------------显示全部------------------------------------------------------------


def show_all(cards):
    """
    展示所有的名片
    1.获取卡包
    2.获取卡包中的每一个元素
    3.按格式打印每一个字典中的信息
    :param cards:
    :return:
    """
    print("-" * 20 + "所有名片如下" + "-" * 20)
    print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
    for card in cards:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (
            card["姓名"],
            card["电话"],
            card["QQ"],
            card["邮件"]))

    print("-" * 50)


# ----------------------------------------------------------查询名片------------------------------------------------------------


def search_card(cards):
    """
    1.获取卡包
    2.输入要查找的姓名
    3.在卡包中查找字典的名字
    4.将这个字典按照格式来这输出
    :param cards:
    :return:
    """
    print("-" * 20 + "查询名片" + "-" * 20)

    names = []  # 创建一个names列表将所有名字装进去
    for tem in cards:
        names.append(tem["姓名"])

    while True:
        name = input("请输入要查找的姓名:")
        if name in names:  # 如果名片夹中有此名字进行查询
            print("-" * 20 + "查询结果如下" + "-" * 20)
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            for card in cards:
                if card["姓名"] == name:
                    print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (
                        card["姓名"],
                        card["电话"],
                        card["QQ"],
                        card["邮件"]))
            print("-" * 50)
            break
        else:  # todo 否则就提示错误,重新输入名字(应该添加一个返回主界面选项)
            print("输入有误!")


# ----------------------------------------------------------主程序------------------------------------------------------------

if __name__ == '__main__':
    # 执行程序前创建卡包
    cards = []

    while True:
        # 展示首页信息
        show_menu()  # 只可以调用上面写的函数

        action = int(input("请选择操作的功能:"))

        # print(action)

        if action in [0, 1, 2, 3]:
            print(action)

            if action == 1:
                # 新建名片
                cards = new_card(cards)
                # print(cards)
                input()

            elif action == 2:
                # print("显示全部")
                # TODO show_all()
                show_all(cards)
                input()

            elif action == 3:
                print("查询名片")
                # TODO search_card()
                search_card(cards)
                input()

            elif action == 0:
                print("退出系统")
                break
        else:
            print("您输入的信息有误,请重新输入:")

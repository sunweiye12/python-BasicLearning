# -*- coding: UTF-8 -*-
# ----------------------------------------知识点------------------------------------------------------
"""
1 Python 内置函数
    Python 包含了以下内置函数：
    len(item)       计算容器中元素个数
    del(item)       删除变量                  del 有两种方式
    max(item)       返回容器中元素最大值      如果是字典，只针对 key 比较
    min(item)       返回容器中元素最小值      如果是字典，只针对 key 比较
    cmp(item1, item2)       比较两个值，-1 小于/0 相等/1 大于       Python 3.x 取消了 cmp 函数
    (*****字符串比较符合以下规则："0" < "A" < "a"*****)
2 切片
    例如:"0123456789"[::-2]  -->  "97531"    支持:字符串、列表、元组
3 运算符
    +               [1, 2] + [3, 4]--->[1, 2, 3, 4]                 字符串、列表、元组
    *               ["Hi!"] * 4--->['Hi!', 'Hi!', 'Hi!', 'Hi!']     字符串、列表、元组
    in              3 in (1, 2, 3)--->True                          字符串、列表、元组、字典
    not in          4 not in (1, 2, 3)--->True                      字符串、列表、元组、字典
    > >= == < <=    (1, 2, 3) < (2, 2, 3)--->True                   字符串、列表、元组
        (- in 在对 字典操作时，判断的是字典的键- in 和 not in 被称为成员运算符)
4 完整的 for 循环语法(**for循环只可以用来遍历**)
    语法如下：
    for 变量 in 集合:
        循环体代码
    else:
        没有通过 break 退出循环，循环结束后，会执行的代码

"""
# ----------------------------------------练习------------------------------------------------------
'''
需求：要判断 某一个字典中 是否存在 指定的 值
- 如果 存在，提示并且退出循环
- 如果 不存在，在 循环整体结束 后，希望 得到一个统一的提示

'''
students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

find_name = input("请输入您要找的名字:")

for stu_dict in students:

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:
        print(stu_dict)
        print("找到了")

        # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
        break

else:       # 此处的 else 只有在所有循环结束都没有进入 if 条件时才会执行
    print("没有找到")

print("循环结束")

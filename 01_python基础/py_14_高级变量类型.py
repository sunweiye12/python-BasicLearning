# -*- coding: UTF-8 -*-
# ----------------------------------------知识点------------------------------------------------------
"""
非数字型
    - 字符串
    - 列表
    - 元组
    - 字典

01. 列表  (数组)
    1.1 列表的定义
        - List（列表） 是 Python 中使用最频繁的数据类型，在其他语言中通常叫做数组
        - 专门用于存储一串信息(一般存储数据类型相同的数据)
        - 列表用 [] 定义，数据之间使用 , 分隔    ----> name_list = ["zhangsan", "lisi", "wangwu"]
        - 列表的索引 从 0 开始(注意：从列表中取值时，如果 超出索引范围，程序会报错)
    2.1 列表方法详见图解

        | 1 | 增加
            列表.insert(索引, 数据)	   在指定位置插入数据
            列表.append(数据)           在末尾追加数据
            列表.extend(列表2)          将列表2 的数据追加到列表
        | 2 | 修改
            列表[索引] = 数据            修改指定索引的数据
        | 3 | 删除
            del 列表[索引]               删除指定索引的数据
            列表.remove[数据]            删除第一个出现的指定数据
            列表.pop                     删除末尾数据
            列表.pop(索引)               删除指定索引数据
            列表.clear                   清空列表
        | 4 | 统计
            len(列表)                    列表长度
            列表.count(数据)             数据在列表中出现的次数
        | 5 | 排序
            列表.sort()                   升序排序
            列表.sort(reverse=True)       降序排序
            列表.reverse()                逆序、反转

    3.1 循环遍历

        - 在 Python 中为了提高列表的遍历效率，专门提供的迭代 iteration 遍历
        - 使用 for 就能够实现迭代遍历
        格式:
        for name in name_list:
            print(name)

02. 元组

    2.1 元组的定义
        - Tuple（元组）与列表类似，不同之处在于元组的元素不能修改(与集合类似)
          - 元组表示多个元素组成的序列
        - 用于存储一串信息，数据之间使用 , 分隔
        - 元组用 () 定义
        - 元组的索引从 0 开始(索引就是数据在元组中的位置编号)
        例如:info_tuple = ("zambian", 18, 1.75)
            info_tuple = ()         创建空元组
            info_tuple = (50, )     元组中只包含一个元素时，需要在元素后面添加逗号
    2.1 元组方法详见图解
    2.3 循环遍历
        for item in info:
            循环内部针对元组元素进行操作
            print(item)
    2.4 元组和列表之间的转换
        - 使用 list 函数可以把元组转换成列表
            list(元组)
        - 使用 tuple 函数可以把列表转换成元组
            tuple(列表)

03. 字典

    3.1 字典的定义
        - dictionary（字典）是除 列表以外Python 之中最灵活的数据类型
        - 和列表的区别
              - 列表是有序的对象集合
              - 字典是无序的对象集合
        - 字典使用键值对存储数据，键值对之间使用 , 分隔
          - 键 key 是索引,值 value 是数据,键 和 值 之间使用 : 分隔
          - 键必须是唯一的
          - 值可以取任何数据类型，但键只能使用字符串、数字类型或元组(****这些都不可变****)
            xiaoming = {"name": "小明",
                        "age": 18,
                        "gender": True,
                        "height": 1.75}
    3.2 字典方法详见图解
    3.3 循环遍历
    # for 循环内部使用的 `key 的变量` in 字典

        for k in xiaoming:
            print("%s: %s" % (k, xiaoming[k]))

        - 遍历 就是 依次 从 字典 中获取所有键值对
        提示：在实际开发中，由于字典中每一个键值对保存数据的类型是不同的，所以针对字典的循环遍历需求并不是很多

04. 字符串

    4.1 字符串的定义
        - 字符串 就是一串字符，是编程语言中表示文本的数据类型
        - 在 Python 中可以使用一对双引号 " 或者一对单引号 ' 定义一个字符串(大多数编程语言都是用 " 来定义字符串)
        - 可以使用索引获取一个字符串中指定位置的字符，索引计数从 0 开始
        - 也可以使用 for 循环遍历 字符串中每一个字符

     4.1 字符串的常用方法
        1) 判断类型
        string.isspace()    中只包含空格，则返回 True
        string.isalnum()    至少有一个字符并且所有字符都是字母或数字则返回 True
        string.isalpha()    至少有一个字符并且所有字符都是字母则返回 True
        string.isdecimal()  只包含数字则返回 True，全角数字
        string.isdigit()    只包含数字则返回 True，全角数字、⑴、\u00b2
        string.isnumeric()  只包含数字则返回 True，全角数字，汉字数字
        string.istitle()    是标题化的(每个单词的首字母大写)则返回 True
        string.islower()    中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回 True
        string.isupper()    中包含至少一个区分大小写的字符，并且所有这些字符都是大写，则返回 True
        2) 查找和替换
        string.startswith(str)  检查字符串是否是以 str 开头，是则返回 True
        string.endswith(str)    检查字符串是否是以 str 结束，是则返回 True
        string.find(str, start=0, end=len(string))  检测 str 是否包含在 string 中，start 和 end 指定范围，如果是返回开始的索引值，否则返回 -1
        string.rfind(str, start=0, end=len(string)) 类似于 find()，不过是从右边开始查找
        string.index(str, start=0, end=len(string)) 跟 find() 方法类似，不过如果 str 不在 string 会报错
        string.rindex(str, start=0, end=len(string))    类似于 index()，不过是从右边开始
        string.replace(old_str, new_str, num=string.count(old)) 把 string 中的 old_str 替换成 new_str，如果 num 指定，则替换不超过 num 次
        3) 大小写转换
        string.capitalize()  把字符串的第一个字符大写
        string.title()       把字符串的每个单词首字母大写
        string.lower()       转换 string 中所有大写字符为小写
        string.upper()       转换 string 中的小写字母为大写
        string.swapcase()    翻转 string 中的大小写
        4) 文本对齐
        string.ljust(width)     返回一个原字符串左对齐，并使用空格填充至长度 width 的新字符串
        string.rjust(width)     返回一个原字符串右对齐，并使用空格填充至长度 width 的新字符串
        string.center(width)    返回一个原字符串居中，并使用空格填充至长度 width 的新字符串
        5) 去除空白字符
        string.lstrip()     截掉 string 左边（开始）的空白字符
        string.rstrip()     截掉 string 右边（末尾）的空白字符
        string.strip()      截掉 string 左右两边的空白字符
        6) 拆分和连接
        string.partition(str)       把字符串 string 分成一个3元素的元组 (str前面, str, str后面) 例如:("he","ll","o")   str="ll"
        string.rpartition(str)      类似于 partition() 方法，不过是从右边开始查找
        string.split(str="", num)   以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格
        string.splitlines()     按照行('\r', '\n', '\r\n')分隔，返回一个包含各行作为元素的列表
        string.join(seq)        以 string 作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串

    4.3 字符串的切片
        **切片 方法适用于 字符串、列表、元组
        切片使用索引值来限定范围，从一个大的字符串中切出小的字符串
        格式为:字符串[开始索引:结束索引:步长]  (详细见练习)
        注意：
            1. 指定的区间属于 左闭右开 型 [开始索引,  结束索引) => 开始索引 >= 范围 < 结束索引,从起始位开始，到结束位的前一位结束（不包含结束位本身)
            2. 从头开始，开始索引 数字可以省略，冒号不能省略
            3. 到末尾结束，结束索引 数字可以省略，冒号不能省略
            4. 步长默认为 1，如果连续切片，数字和冒号都可以省略
             在 Python 中不仅支持顺序索引，同时还支持 倒序索引,所谓倒序索引就是从右向左计算索引,
             最右边的索引值是-1，依次递减



"""

if __name__ == '__main__':

    # ----------------------------------------练习列表------------------------------------------------------
    print("----------------练习列表-----------------------")
    # 方法练习
    name_list = ["zhangsan", "lisi", "wangwu"]

    del name_list[0]
    name_list.pop(1)
    print(len(name_list))

    print("-------------------------------------------------------------")

    # 遍历的练习
    name_list = ["zhangsan", "lisi", "wangwu"]  # 定义列表

    for name in name_list:  # 遍历列表
        print(name)

    # ----------------------------------------练习元组------------------------------------------------------
    print("----------------练习元组-----------------------")
    # 遍历元组
    info_tuple = (1, 2, 3)

    for item in info_tuple:
        print(item)

    # 元组的基本应用
    info = ("张三", 18)
    print("%s 的年龄是 %d" % info)

    # 元组和列表的转换

    info_tu = (1, 2, 3)  # 使用 list 函数可以把元组转换成列表
    print(type(info_tu))
    print(type(list(info_tu)))

    list_tu = [1, 2, 3]  # 使用 list 函数可以把元组转换成列表
    print(type(list_tu))
    print(type(tuple(list_tu)))
    # ----------------------------------------练习字典------------------------------------------------------
    print("----------------练习字典-----------------------")

    # 创建字典
    xiaoming = {"name": "小明",
                "age": 18,
                "gender": True,
                "height": 1.75}

    # for 循环内部使用的 `key 的变量` in 字典
    for k in xiaoming:
        print("%s: %s" % (k, xiaoming[k]))

    # ----------------------------------------练习字符串------------------------------------------------------
    print("----------------练习字符串-----------------------")

    string = "Hello Python"

    for c in string:
        print(c)

    # print(string.isalnum())   #判断是否都为字母或数字

    # i = string.index("ll", start=0, end=len(string))

    print(string.partition("ll"))  # ('He', 'll', 'o Python')

    # ----------------------------------------练习切片------------------------------------------------------
    print("----------------练习切片-----------------------")
    '''
    演练需求
    - 1. 截取从 2 ~ 5 位置 的字符串
    - 2. 截取从 2 ~ 末尾 的字符串
    - 3. 截取从 开始 ~ 5 位置 的字符串
    - 4. 截取完整的字符串
    - 5. 从开始位置，每隔一个字符截取字符串
    - 6. 从索引 1 开始，每隔一个取一个
    - 7. 截取从 2 ~ 末尾 - 1 的字符串
    - 8. 截取字符串末尾两个字符
    - 9. 字符串的逆序（面试题）
    '''
    num_str = "0123456789"

    # 1. 截取从 2 ~ 5 位置 的字符串(左闭右开)
    print(num_str[2:6])

    # 2. 截取从 2 到末尾` 的字符串
    print(num_str[2:])

    # 3. 截取从 开始`到5 位置 的字符串
    print(num_str[:6])

    # 4. 截取完整的字符串
    print(num_str[:])

    # 5. 从开始位置，每隔一个字符截取字符串
    print(num_str[::2])

    # 6. 从索引 1 开始，每隔一个取一个
    print(num_str[1::2])

    # 倒序切片
    # -1 表示倒数第一个字符
    print(num_str[-1])

    # 7. 截取从 2 到末尾 - 1` 的字符串
    print(num_str[2:-1])

    # 8. 截取字符串末尾两个字符
    print(num_str[-2:])

    # 9. 字符串的逆序（面试题）
    print(num_str[::-1])

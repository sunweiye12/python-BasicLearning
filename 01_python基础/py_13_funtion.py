# -*- coding: UTF-8 -*-

# 在此模块定义一个变量
sun = 100

def chengfa_99():  # 在此模块定义一个名叫99乘法表的函数

    row = 1  # 定义第二个乘数

    while row <= 9:

        col = 1  # 定义第一个乘数
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="    ")    #打印完成后不换行,用空格代替
            col += 1
        print("")
        row += 1


# 在同一页面中调用函数,直接写函数名就可以
if __name__ == '__main__':
    chengfa_99()

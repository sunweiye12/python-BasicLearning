'''
1、input输入

    input输入很简单，就是获得用户的输入，一般是在控制台界面。
'''
# word=input('please input one or more word\n')
# print (word)

'''
2、sys.stdin 输入

    第一他也可以实现和input一样的功能，比如
'''
# import sys
# print('please input one or more word\n')
# word=sys.stdin.readline()
# print (word)

'''
    但是，他更常见的是另外一种使用方式，可以直接使用文件作为整体的输入，可以很简洁。
'''
# import sys
# for line in sys.stdin.readlines():
#     if not line:
#         break
#     else:
#         print(line)

'''
上述主要是进行标准化输入的获取，这一部分要和参数传递分清楚，其实Python最常用的就是参数传递也就是argpares模块和sys模块
'''

'''
argv 是 argument variable 参数变量的简写形式，在命令行调用的时候，有系统传递给程序。
Run > Configuration > Script parameters 里面写入默认的参数
'''
# import sys
# print('打印第 2 到第 5 个元素：', sys.argv[1:5])
# print('打印所有参数：', sys.argv[:])
# for i in sys.argv:
#     print(i)

'''
这个方法，调用的就是 file 对象的 write 方法，区别是 file 对象的 write 方法吧字符写入到文件中，
sys.stdout.write 方法把字符写入到标准输出中，也就是控制台。
stdout.write 默认不换行，print 默认换行
stdout.write 配合 \n 换行符，可以实现换行的功能。
sys.stdout.write('str \n')
print 也可以实行不换行
print('str', end='')
'''
# import sys
# print('print 默认换行')
# sys.stdout.write('stdout.write 默认不换行')
# print('+++++++++')

'''
从控制台重定向到文件
stdout 和 print 可以结合使用的案例。
'''
# import sys
# file = sys.stdout                                   # 存储原始的输出对象
# sys.stdout = open('1.txt', 'w')                   # 重定向所有的print内容到 1.txt 文件
# print('Citizen_Wang')                             # 写入到 1.txt 文件中
# print('Always fall in love with neighbours')   # 继续写入到文件中
# sys.stdout.close()                                  # 其实就是 open 文件之后的关闭
# sys.stdout = file                                   # 将 print 命令的结果返回给控制台
# print('输出信息返回在控制台')                     # 该信息会在控制台也显示

'''
同时重定向到控制台和文件(将输入的信息存放到文件中)
sys.stdin
sys.stdin 和 input
'''
import sys
print('Plase input your name: ')
name = sys.stdin.readline()
file = sys.stdout                                   # 存储原始的输出对象
sys.stdout = open('2.txt', 'w')                   # 重定向所有的print内容到 1.txt 文件
print(name)
sys.stdout.close()                                  # 其实就是 open 文件之后的关闭
sys.stdout = file
print('Hello ', name)









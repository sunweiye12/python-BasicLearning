# -----------------------------------知识点------------------------------------------
'''
在 Python 中，如果希望通过程序实现上述功能，需要导入 os 模块

文件操作
    序号 	方法名 	说明 	        示例
    01 	    rename 	重命名文件   	os.rename(源文件名, 目标文件名)
    02 	    remove 	删除文件 	    os.remove(文件名)
目录操作
    序号 	方法名 	    说明 	        示例
    01 	    listdir 	目录列表 	    os.listdir(目录名)
    02 	    mkdir 	    创建目录 	    os.mkdir(目录名)
    03 	    rmdir 	    删除目录 	    os.rmdir(目录名)
    04 	    getcwd 	    获取当前目录 	os.getcwd()
    05 	    chdir 	    修改工作目录 	os.chdir(目标目录)
    06 	    path.isdir 	判断是否是文件 	os.path.isdir(文件路径)

    文件或者目录操作都支持 相对路径 和 绝对路径
'''
import os

# 重命名文件
# os.rename("README[复件1]", "README[复件2]")
# 删除文件
# os.remove("README[复件2]")

# 目录列表
print(os.listdir("C://Users//Administrator//Desktop"))
# 创建目录
# os.mkdir("C://Users//Administrator//Desktop//scr//python//python基础//README[复件1]")
# 删除目录
# os.rmdir("README[复件1]")
# os.rmdir("C://Users//Administrator//Desktop//scr//python//python基础//README[复件1]")
# 获取当前目录
print(os.getcwd())
# 修改工作目录
os.chdir(".")
# 判断是否是文件夹
print(os.path.isdir("README"))
print(os.path.isdir("README[复件1]"))


# 1.打开一个文件
file_read = open("README[复件1]//README")                  # 默认只读
file_write = open("README[复件1]//README[复件3]","w")     # 只写
# 2.读取并写入文件
while True:
    f = file_read.readline()

    if not f:       # 如果此行是末尾就跳出,如果不是就写入复制文件
        break
    else:
        file_write.write(f)
# 3.关闭文件
file_read.close()
file_write.close()

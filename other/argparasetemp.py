#coding:utf-8
import argparse

##好像和参数有关

# paras = argparse.ArgumentParser()
# paras.parse_args()


# parser1 = argparse.ArgumentParser('this is a textbox')
# parser1.parse_args()
##创建一个解释器对象
# parser2 = argparse.ArgumentParser()
# parser2.add_argument('echo',help='echo the string you use here')
# args = parser2.parse_args()
# print args.echo


## 读写文件爱你操作一般的步骤   打开open()  读取read() 写入write()

filter_object_read = open('OUTPUT.txt', 'r')
try:
    filterobj = filter_object_read.read()
finally:
    filter_object_read.close()


## 写入文件
filtr_object_write = open('output.txt', 'w')
try:

    filtr_object_write.write(filterobj)
finally:
    filtr_object_write.close()


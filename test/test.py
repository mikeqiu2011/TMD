# import socket
#
# print(socket.gethostname())

# import configparser
# config = configparser.ConfigParser()
# config.read('file_details.ini')
# print(config.get(section='file', option='root_dir'))

# nlist = [i for i in range(11) if i%2 != 0]
# print(nlist)

# ndict = {x:x*2 for x in range(10)}
# print(ndict)
# import operator
# x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# sorted_x = sorted(x, key=operator.itemgetter('age'), reverse=True)
# print(sorted_x)

# import commands
# mount = commands.getoutput('df -h')
# lines = mount.split('\n')
# print(lines)
# points = map(lambda line: line.split()[-1], lines[1:])
# # print(type(mount_points))
# print(points)
# points.remove('/')
# print(points)
#
# path = '/'
#
# def get_mount(path, mount_list):
#     for mount_point in mount_list:
#         if path.startswith(mount_point):
#             return mount_point
#     return '/'
#
# mp = get_mount(path, points)
# print(mp)

# func = lambda x:x*2
#
# print(func(4))

# add = lambda x,y: x/y if y!=0 else x
#
# print(add(5,0))

# list1 = [3,5,-4,-1,0,-2,-6]
# list2 = sorted(map(lambda x:abs(x), list1),reverse=True)
# print(list2)
# nlist = sorted(list1,key=lambda x:abs(x))
# print(nlist)

# def get_y(a, b):
#     return lambda x: a*x + b
#
#
# y2 = get_y(2, 2)
# print(y2(3))

# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
def run(fn):
  #fn: 函数参数是数据列表的一个元素
  time.sleep(1)
  print(fn*fn)

if __name__ == "__main__":
  testFL = [1,2,3,4,5,6]
  print ('shunxu:') #顺序执行(也就是串行执行，单进程)
  s = time.time()
  for fn in testFL:
    run(fn)
  t1 = time.time()
  print ("顺序执行时间：", int(t1 - s))

  print ('concurrent:') #创建多个进程，并行执行
  pool = Pool(10)  #创建拥有10个进程数量的进程池
  #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
  pool.map(run, testFL)
  pool.close()#关闭进程池，不再接受新的进程
  pool.join()#主进程阻塞等待子进程的退出
  t2 = time.time()
  print ("并行执行时间：", int(t2-t1))

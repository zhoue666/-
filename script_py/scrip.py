#读取test.c3d的修改时间
#在testEMG1_10.txt文件的基础上，更新第一列时间坐标---->格林尼治绝对时间
#更新完毕的坐标数据，更新在newEMG.txt文件中

import os
from datetime import datetime
import time
import numpy as np

statinfo=os.stat(r'test.c3d')
time1=statinfo.st_mtime          # st_atime (访问时间), st_mtime (修改时间), st_ctime（创建时间）
print('test文件修改日期的时间戳是：\n\t',time1)
d=datetime.fromtimestamp(time1)
str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
print('test文件修改日期的时间格式是：\n\t',str1)
robust_time=str1[11:]
print('',robust_time)
timestamp=float('%.4f'%time1)
print(timestamp)
print('------------look-----------')

# a = np.loadtxt('testEMG1_10.txt') 
# print('数据长度：',a.shape)   #数据的长度  a.dtype是数据类型  默认都是float64
# value=a[-1,0]    #最后一列的相对时间 float
# a[:,0]=a[:,0]+timestamp-value
# print(a)
# np.set_printoptions(suppress=True)  #科学计数法
# np.savetxt('EMG_time.txt',a,fmt='%.04f')
# print('生成文件已完成')
# print("-----时间戳转化已完毕，现在转时间格式-----")

b = np.loadtxt('EMG_time.txt')   # <class 'numpy.ndarray'>
b_arry=b[:,0]                  # <class 'numpy.ndarray'>
b_list=b_arry.tolist()         #时间戳的list
New_list=list(map(lambda x:datetime.fromtimestamp(x).strftime("%Y-%m-%d %H:%M:%S.%f"),b_list))
New_list1='\n'.join(New_list)                #时间格式的array
print(type(New_list1))
with open('accurcy_time.txt','w') as f:
    f.write(New_list1)


#-------------------生成绝对时间戳的文件-------------------------------------------
# a = np.loadtxt('testEMG1_10.txt') 
# # a.dtype='float64'
# print(a.shape)   #数据的长度  a.dtype是数据类型  默认都是float64
# value=a[-1,0]     #最后一列的相对时间
# print(value)

# a[:,0]=a[:,0]+time_label-value

# f'{np.mean([2, 3.4567]): .3f}'
# print(a)
# # np.set_printoptions(suppress=True)

# np.savetxt('NewEMG.txt',a,fmt='%.05f')
# print('生成文件已完成')


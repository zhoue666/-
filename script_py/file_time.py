#读取文件的修改时间和创建时间mtime ctime 精确到ms
#读取文件的修改时间--->时间戳----->转化为标准时间格式---->提取需要的时间片段
import os
from datetime import datetime
import time


# st_atime (访问时间), st_mtime (修改时间), st_ctime（创建时间）
point=1200036
statinfo=os.stat(r'D:\A_data\A_gitee\speech-signal-processing\script_py\test.c3d')  #文件路径你要改
time1=statinfo.st_ctime
time2=statinfo.st_mtime
print('------创建日期是-------')
print('绝对时间是：',time1)
d1=datetime.fromtimestamp(time1)
str1 = d1.strftime("%Y-%m-%d %H:%M:%S.%f")
print('修改时间是：',str1)
print('------修改日期是-------')
print('绝对时间是：',time2)
d2=datetime.fromtimestamp(time2)
str2 = d2.strftime("%Y-%m-%d %H:%M:%S.%f")
print('修改时间是：',str2)
print('---采样频率为----------')
fs=(point-1)/(time2-time1)
print(fs)
print('时间差:',time2-time1)
print('点的个数为：',point)


# #时间格式--->时间戳个位数为秒，保留六位小数~
# print('-------------------')
# str_time='2019-02-26 13:04:41.111111'
# print(type(str_time))
# timestr='2019-02-26 13:04:41.111111'
# datetime_obj=datetime.strptime(timestr,'%Y-%m-%d %H:%M:%S.%f')
# print(datetime_obj.timetuple())
# print(datetime_obj.microsecond)
# ret_stamp=float(time.mktime(datetime_obj.timetuple())+datetime_obj.microsecond/1000000.0)
# print(ret_stamp)



# 2021-10-23 01:16:41.220333
# 01:16:41.220333   修改时间

# 2021-10-23 01:16:41.220333
# 01:16:41.220333   下一个文件的创建时间
# 2021-10-23 01:26:41.243118
# 01:26:41.243118   下一个文件的修改时间



#循环读取文件夹中所有文件的修改时间
# path = u"C:\\Users\\Zhoue\\Documents\\10.23"
# for root, dir, files in os.walk(path):
#     for file in files:
#         full_path = os.path.join(root, file)
#         #print(full_path)
#         #print(file)
#         mtime = os.stat(full_path).st_mtime
#         file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
#         print("{0} 修改时间是: {1}".format(full_path,file_modify_time))
        
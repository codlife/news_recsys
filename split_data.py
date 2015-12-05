#!encoding=utf-8
import sys

raw_input='user_click_data.txt'
part_raw_output='part_raw_output.txt'
fpin=open(raw_input,'r',encoding='utf-8')
lines=fpin.readlines(10000000)
#读取 前10000条记录
result=[]
for line in lines:
	result.append(line)
fpin.close()
fpout=open(part_raw_output,'w',encoding='utf-8')
fpout.writelines(result)
fpout.close()
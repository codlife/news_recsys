import sys
import jieba
import jieba.analyse
inputfile="part_raw_output.txt"
outputfile='part_fenci.txt'
fpin=open(inputfile,'r',encoding='utf-8')
lines=fpin.readlines()
result=[]
for line in lines:
	datas=line.split('\t')
	
	#print(datas[1],datas[3])
	#fenci=jieba.cut(datas[3])
	#fenci计算速度挺慢的，不要随便计算 本次计算cost 137s
	fenci=jieba.analyse.extract_tags(datas[4],withWeight=True)
	temp=datas[1]
	for item in fenci:
		temp=temp+'\t'+item[0]+'\t'+str(item[1])
	temp=temp+'\n'
	result.append(temp)

fpin.close()
fpout=open(outputfile,'w',encoding='utf-8')
fpout.writelines(result)
fpout.close()
print(len(result))
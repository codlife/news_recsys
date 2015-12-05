import sys
import jieba
import jieba.analyse
inputfile="part_fenci.txt"
outputsim='part_similarity.txt'
fpin=open(inputfile,'r',encoding='utf-8')
lines=fpin.readlines()
fpin.close()
similarity=[]
# 1e8 次计算大概耗时 7s，如果 调用了len，时间会增加 至少三倍以上
# 下面这行代码，要不然会调用很多次len 函数
length=len(lines)
print("start.....")
#
for i in range(length//10):
	if(lines[i]=='NULL'):
		continue
	da=lines[i].split('\t')
	lena=len(da)
	if(lena<3):
		continue
	tempsim=da[0]
	unsort=[]
	if(i%100==0):
		print(i)
	for j in range(i+1,length//10):
		# 计算相似度
		sim=0.0
		db=lines[j].split('\t')
		lenb=len(db)
		if(lenb<3):
			continue
		for i in range(1,lena,2):
			for j in range(1,lenb,2):
				if(da[i]==db[j]):
					sim+=float(da[i+1])*float(db[j+1])
		if(sim<0.1):
			continue
		unsort.append((db[0],sim))
	unsort=sorted(unsort,key=lambda x:(x[1]),reverse=True)
	 
	lensort=len(unsort)
	#截取前 20 篇
	if(lensort>20):
		lensort=20
	for k in range(lensort):
		tempsim+='\t'+unsort[k][0]+'\t'+str(unsort[k][1])
	tempsim+='\n'

	similarity.append(tempsim)
fpout=open(outputsim,'w',encoding='utf-8')
fpout.writelines(similarity)
fpout.close()
print(len(similarity))
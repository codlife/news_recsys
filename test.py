#!encoding=utf-8
import sys
import jieba
import jieba.analyse
# #matrix=[[0 for col in range(10000) ] for row in range(50000)]
# # count=0 
# # seg_list = jieba.analyse.extract_tags("财新网（实习记者葛菁）据新华社消息，马来西亚航空公司表示，与一架由吉隆坡飞往北京的客机失去联系，机上载有来自13个国家的239名乘客和机组人员，包括153名中国公民。该架航班号为MH370的班机于北京时间00：42分起飞，原定于北京时间6点30分到达。目前该机一直未与中国管制部门建立联络或进入空管情报区，首都机场已将该航班列为失踪。　　财新记者从瑞典实时航空交通跟踪网站Flightrader网站看到，在今晨01：21分,MH370班机航向为25度，高度还在3.5万英尺，之后突然变成航向40度，接着高度变成0，该网站显示，MH370最后在有信号的地点在位于距马来西亚东北部的KualaTerengganu东北方向150公里处，在马来西亚和越南之间的海域，在高度变成0之后失去信号。据航空人士告诉财新记者，这样的情况有可能是空中解体。　　据马航公开发布的消息，今日凌晨01:20左右，在胡志明管制区同管制部门失去通讯联络，同时失去雷达信号，位于吉隆坡的管制台于今天凌晨2点40分证实，该航班已经失去联系。　　一位自述为首都机场塔台的工作人员早前发微博称，据三亚区调值班管制员透露，“飞机是在新加坡和越南交界点突然消失，之后差不多凌晨一点，越南人问有没有该航班，我说没有，他就挂了，差不多凌晨两点他才跟我说飞机不见了，然后凌晨三点多跟我说，他们公司说这架飞机还在飞，然后我让香港帮我喊喊，什么都没有。”该微博已被删除。　　此前曾传出消息，失联的MH370航班因雷达故障，降落在一个叫做Nanming的机场。据《中国经营报》记者核实，南宁机场管理集团表示没有该航班降落的消息。　　马航副总裁在接受CNN采访时表示，该架波音777-200号客机航班起飞时运载航油可供7小时飞行，截至失联消息公布之时，燃油已经耗尽。该次航班使用的波音777机龄接近12年，是全球最大的，也是较受国际航空公司欢迎的双引擎客机，三级舱布置的载客量283到368人。　　去年7月6日在旧金山着陆时坠毁的韩亚航空亦使用波音777-200机型，该次事故造成两名中国籍乘客死亡，也是波音777投入商运后首次有乘客在营运商中丧生。这次马航失联事件或会成为波音777投入运营以来最严重事故。　　失联的马航客飞机型号为波音777-200，体积较大，曾在浦东机场发生碰擦，机翼受损。CNN称，这架飞机应该是2002年交付马航使用的，马航在运营波音777方面拥有极为丰富的经验。　　据路透社，马航正等待政府许可以更换较旧的空客A330和波音777-200型客机。该公司希望节省燃油费和减少维修成本。彭博社去年11月报告称，马航近两年来经营不善。马航现有15架波音777-200，最老的购于1997年，最新的购于2001年，平均使用年龄达14年",withWeight=True)
# # f=open('just_test.txt','w',encoding='utf-8')
# # ans=["123"]
# # result=""
# # for item in seg_list:
# # 	result=result+"\t"+item[0]+"\t"+str(item[1])
# # result=result+'\n'
# # ans.append(result)
# # print(ans)
# # f.writelines(ans)
# # f.close()
# # a=[(1,'w'),(2,'a')]
# # a=sorted(a,key=lambda x:(x[1]))
# # a.append((1,2))
# # print(a)
# # s=""
# # s+=str(a[0][0])+str(a[0][1])

# def f(A,B,n,T,a,b):
# 	a[0]=0
# 	b[0]=0
# 	T[0]=0
# 	for i in range(1,n):
# 		if(a[i-1]+A[i]<=T[i-1] ):
# 			a[i]=a[i-1]+A[i]
# 			b[i]=b[i-1]
# 			T[i]=T[i-1]
# 		elif(b[i-1]+B[i]<=T[i-1]):
# 			b[i]=b[i-1]+B[i]
# 			a[i]=a[i-1]
# 			T[i]=T[i-1]
# 		elif(a[i-1]+A[i]<b[i-1]+B[i]):
# 			a[i]=a[i-1]+A[i]
# 			b[i]=b[i-1]
# 			T[i]=a[i]
# 		else:
# 			b[i]=b[i-1]+B[i]
# 			a[i]=a[i-1]
# 			T[i]=b[i]
# 	#print 调度信息
# 	for i in range(1,n):
# 		if(a[i-1]+A[i]<b[i-1]+B[i]):
# 			print("A机器调度作业"+str(i))
# 		else:
# 			print("B机器调度作业"+str(i))
# 	print(T[n-1])
# #W[i][j]=min{W[i][k]+W[k][j]+dik+djk+aij}     {i<k<j }
# def polygon(w,s,e,d,a,n):
#  	for i in range(1,n+1):
#  		w[i][i]=0
#  	for k in range(2,n+1):
#  		for i in range(1,n+1-k,k):
#  			j=i+k
#  			w[i][j]=1<<31
#  			for r in range(i,j+1):
#  				if(w[i][j]>w[i][r]+w[r+1][j]+d[i-1][r]+d[j][r]+a[i-1][j]):
#  					w[i][j]=w[i][r]+w[r+1][j]+d[i-1][r]+d[j][r]+a[i-1][j]
# #多学习算法，能使人变聪明
# x=[0]*5 
# w=[1,2,4,3,5]
# M=10
# w=sorted(w)

# def subset_sum(s,k,r):
# 	x[k]=1
# 	if(s+w[k]==M):
# 		print(x)
# 	elif(s+w[k]+w[k+1]<=M):
# 		subset_sum(s+w[k], k+1, r-w[k])
# 	# 这里就是 输入已经排序的目的，这里的剪枝非常好。
# 	#因为 w 递增排序，所以 如果 s+w[k+1]>M 那么直接剪掉。
# 	if(s+r-w[k]>=M and s+w[k+1]<=M):
# 		x[k]=0
# 		subset_sum(s, k+1, r-w[k])

#latin 方问题
#注意下面这种写法，避免直接写[[0]*4]*4 存在前拷贝问题
n=6
m=[[0 for x in range(n)] for y in range(n)]
m[0]=[x for x in range(1,n+1)]
print(m)
def place(k,i):
	while(m[k][i]<n):
		m[k][i]+=1
		j=i-1
		jj=k-1
		while(j>=0):
			if(m[k][j]==m[k][i]):
				break
			j-=1
		if(j>=0):
			continue
		while(jj>=0):
			if(m[jj][i]==m[k][i]):
				break
			jj-=1
		if(jj<0):
			return  True	 
	return False
def latin(k):
	while(k>0):
		if(k==n):
			print(m)
			return 	
		i=0
		while(i>=0):
			if(i==n):
				k+=1
				break
			if (place(k,i)==False):
				m[k][i]=0
				i-=1
			else:
				i+=1
		if(i<0):
			k-=1
#latin(1)
n=12
x=[0 for i in range(n+1)]

countt=0
def pla(k):
	i=1
	while(i<k):
		if(x[i]==x[k] or abs(x[k]-x[i])==abs(k-i)):
			return False
		else:
			i+=1
	return True
def queen(k):
	k=1
	x[k]=0
	while(k>0):
		x[k]=x[k]+1
		while(x[k]<=n and pla(k)==False):
			x[k]=x[k]+1
		if(x[k]<=n):
			if(k==n):
				#print(x)
				# 注意这里 单个变量 必须声明才能修改，但是数组之类的不需要
				global countt
				countt=countt+1
			else:
				k+=1
				x[k]=0
		else:
			k-=1
#queen(1)
#8皇后 92组解
w=[1,2,3,4]
v=[2,1,2,3]
T=10
n=4
import queue
myqueue=queue.Queue()
myqueue.put(-1)
print(myqueue.get())
def one_zore(k,bv,tv):
	k=1
	myqueue.put(-1)
	tv=0
	bv=0
	while(k>0):
		if(tv+w[k]<=c):
			myqueue.put(w[k])
			if(k==n):
				if(tv+v[k]>bv):
					bv=tv+v[k]
		myqueue.put(0)
		item=myqueue.get()
		if(item==-1):
			if(k==n):
				return bv
			myqueue.put(-1)
			k+=1














#-----------------------------------------------------------#
# Input:                                                    #
# filename                                                  #
# Number of atoms that appear before O and O                #
# Number of Outputs                                         #
#-----------------------------------------------------------#

import sys
import random

class RandVacGenerator:
	def __init__(self,filename,rank):
		self.input=filename
		self.rand=[]
		self.rank=rank
		f=open(filename)
		for line in range(7):
			numline=f.readline()
		alist=numline.split(' ')
		self.numList=[]
		for item in alist:
			if item != '':
				self.numList.append(int(item)) 
		f.close()

	def testRand(self,range):
		num=random.randint(1,range)
		if num in self.rand:
			return self.testRand(range)
		else:
			self.rand.append(num)
			return num
		
	def randomDelete(self,output):
		f=open(self.input)
		g=open(output,'w')
		beforeO=0
	        for i in self.numList[:self.rank-1]:
			beforeO+=i
		O=self.numList[self.rank-1]
		for line in range(6):
			a=f.readline()
			g.write(a)
		numline=''
		for i in range(len(self.numList)):
			if i != self.rank-1:
				numline+=str(self.numList[i])+'  '
			else:
				numline+=str(self.numList[i]-1)+'  '
		numline+='\n'
		f.readline()
		g.write(numline)
		a=f.readline()
		g.write(a)
		vac=self.testRand(O)
		d=beforeO+vac # delete dth row in the coordinates
		count=0
		while a:
			count+=1
			a=f.readline()
			if count != d:
				g.write(a)
		f.close()
		g.close()
		return None

	def multiFiles(self,N):
		for i in range(N):
			output='output'+str(i+1)
			self.randomDelete(output)

filename=sys.argv[1]
Orank=int(sys.argv[2])
N=int(sys.argv[3])
app=RandVacGenerator(filename,Orank)
app.multiFiles(N)

#find all configurations when doping 2 Y and 1 vacancy
import math
import sys

class find:

  def __init__(self,nx,ny,nz,l0):
      self.nx=nx
      self.ny=ny
      self.nz=nz
      self.l0=l0
  def Zrpos(self):#number of primitive unit cells and lattice constant of primitive cell
    Zr=[]
    for i in range(self.nx):
        for j in range(self.ny):
            for k in range(self.nz):
                Zr.append((i*self.l0,j*self.l0,k*self.l0))
    return Zr

  def Bapos(self):
    Ba=[]
    for i in range(self.nx):
        for j in range(self.ny):
            for k in range(self.nz):
               Ba.append((self.l0*(i+0.5),self.l0*(j+0.5),self.l0*(k+0.5)))
    return Ba

  def Opos(self):
    O=[]
    for i in range(self.nx):
        for j in range(self.ny):
            for k in range(self.nz):
                O.append((self.l0*(i+0.5),self.l0*j,self.l0*k))
                O.append((self.l0*i,self.l0*(j+0.5),self.l0*k))
                O.append((self.l0*i,self.l0*j,self.l0*(k+0.5)))
    return O

  def Ypos(self): # return 2 Y's positions 
    Zr=self.Zrpos()
    N=len(Zr)
    index=[]
    for i in range(N):
        j=i+1
        while j<N:
            index.append((i,j))
            j=j+1
    comb=[]
    for i in range(len(index)):
          comb.append((Zr[index[i][0]],Zr[index[i][1]]))
    return comb

  def distance(self,atom1,atom2):
    dx=(atom1[0]-atom2[0])%(self.nx*self.l0)
    dy=(atom1[1]-atom2[1])%(self.ny*self.l0)
    dz=(atom1[2]-atom2[2])%(self.nz*self.l0)
    if abs(dx)>self.l0*self.nx/2:
       dx=self.nx*self.l0-abs(dx)
    if abs(dy)>self.l0*self.ny/2:
       dy=self.ny*self.l0-abs(dy)
    if abs(dz)>self.l0*self.nz/2:
       dz=self.nz*self.l0-abs(dz)
    distance=math.sqrt(dx**2+dy**2+dz**2)
    return distance


  def order(self,a,b,c):#a is YY distance, b and c are YO distances
    if b>=c:
     return (a,b,c)
    else:
     return (a,c,b)
  
  def equal(self,a,b,epsilon):
     if len(a) != len(b):
            print "Error! Can't compare"
            return None
     num=0
     for i in range(len(a)):
         if abs(a[i]-b[i]) < epsilon:
           num+=0
         else:
           num+=1
     if num == 0 :
           return True
     else:
           return False 

  def writelist(self):
     Y=self.Ypos()
     O=self.Opos()
     yNum=len(Y)
     oNum=len(O)
     aList=[]
     length=[]
     for i in range(yNum):
        for j in range(oNum):
            aList.append((Y[i][0],Y[i][1],O[j]))
            a=self.distance(Y[i][0],Y[i][1])
            b=self.distance(Y[i][0],O[j])
            c=self.distance(Y[i][1],O[j])
            length.append(self.order(a,b,c))
     return aList, length
            


  def reducelist(self):
      aList=self.writelist()[0]
      length=self.writelist()[1]
      N=len(aList)
      reduce=[0] # store index of aList
      e=0.001 # epsilon
      for i in range(N):
          count=0
          for j in reduce:
               if self.equal(length[i],length[j],e):
                    count+=1
               else:
                    count+=0
          if count == 0:
             reduce.append(i) 
      return reduce 


def main():
	input=[]
	for i in range(4):
   	     input.append(sys.argv[i+1])
	app=find(int(input[0]),int(input[1]),int(input[2]),float(input[3])) # nx,ny,nz,l0
	aList=app.writelist()[0]
	length=app.writelist()[1]
	reduce=app.reducelist()
	num=1
        print '\t\t Y1 \t \t Y2 \t \t O \t d(Y1Y2),d(Y1O),d(Y2O)'
	for i in reduce:
 	   print num,'\t',
           for l in range(3):
              print '%.2f'%aList[i][0][l],
           print '\t',
           for m in range(3):
              print '%.2f'%aList[i][1][m],
           print '\t',
           for n in range(3):
              print '%.2f'%aList[i][2][n],
           print '\t',
           for j in range(3):
              print '%.2f'%length[i][j],
           print '\n'
	   num+=1
      
main()

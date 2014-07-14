#--------------------------------------------------------------------#
#randomly find n proton positions in a nx*ny*nz supercell            #
#all the coordinates are fractions                                   #
#vacancies are in a list, and around the vacancies there's no proton #
#vacancies' coordinates are formed by assuming the lengths of unit   #
#cell are 1                                                          #
#--------------------------------------------------------------------#
import random
import sys
def FindProton(nx,ny,nz,Vo):
    lx=1/float(nx)
    ly=1/float(ny)
    lz=1/float(nz) #unit cell parameters in fractional number
    hx=lx/4
    hy=ly/4
    hz=lz/4  #O-H bond length
    oxyproton={} # for each oxygen there're 4 proton positions around it
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                   oxy1=(lx*(i+0.5),j*ly,k*lz)
                   oxy2=(i*lx,ly*(j+0.5),k*lz)
                   oxy3=(i*lx,j*ly,lz*(k+0.5)) #oxygens
                   oxyproton[oxy1]=[(oxy1[0],oxy1[1]+hy,oxy1[2]),(oxy1[0],oxy1[1]-hy,oxy1[2]),(oxy1[0],oxy1[1],oxy1[2]+hz),(oxy1[0],oxy1[1],oxy1[2]-hz)]
                   oxyproton[oxy2]=[(oxy2[0]+hx,oxy2[1],oxy2[2]),(oxy2[0]-hx,oxy2[1],oxy2[2]),(oxy2[0],oxy2[1],oxy2[2]+hz),(oxy2[0],oxy2[1],oxy2[2]-hz)]
                   oxyproton[oxy3]=[(oxy3[0],oxy3[1]+hy,oxy3[2]),(oxy3[0],oxy3[1]-hy,oxy3[2]),(oxy3[0]+hx,oxy3[1],oxy3[2]),(oxy3[0]-hx,oxy3[1],oxy3[2])]
    for item in Vo:
        new=(item[0]*lx,item[1]*ly,item[2]*lz)
        if new in oxyproton.keys():
           del oxyproton[new]
        else:
           print( str(new)+' is not an oxygen position!')
    return oxyproton

def selectProton(protondic,n):
    oxy=protondic.keys()
    Oselected=random.sample(oxy,n)
    proton=[]
    for i in range(n):
        p=random.sample(protondic[Oselected[i]],1)
        proton.append(p[0])
    return proton
 
    
#var1=input("nx,ny,nz (use ',' to separate numbers): ")
#x=var1[0]
#y=var1[1]
#z=var1[2]
#var2=input("vacancies (x1,y1,z1,x2,y2,z2...): ")
#nvac=len(var2)/3
#if nvac == 0:
#   print ("not enough coordinates!")
#else:
#   vac=[]
#   i=0
#   for n in range(nvac):
#        vac.append((var2[i],var2[i+1],var2[i+2]))
#        i=i+3
#var3=raw_input("output filename: ")
#adic=FindProton(x,y,z,vac)
#f=open(var3,'w')
#for item in adic.values():
#     for i in item:
#         a=str(i[0])+'   '+str(i[1])+'   '+str(i[2])+'\n'
#         f.write(a)
nx=int(sys.argv[1])
ny=int(sys.argv[2])
nz=int(sys.argv[3])
v=sys.argv[4]
va=v.split(",")
nvac=len(va)/3
if nvac == 0:
   print ("not enough coordinates!")
else:
    vac=[]
    i=0
    for n in range(nvac):
        vac.append((float(va[i]),float(va[i+1]),float(va[i+2]))) 
        i=i+3
num=int(sys.argv[5])
protondic=FindProton(nx,ny,nz,vac)
proton=selectProton(protondic,num)
for pos in proton:
    print pos[0],'\t', pos[1],'\t', pos[2] 

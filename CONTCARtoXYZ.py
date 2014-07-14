#-----------------------------------------------#
#Convert a CONTCAR or POSCAR file to a xyz file #
#nx,ny,nz are the number of unit cells in x,y,z #
#ratio is the a factor from 0-1 to modify atoms #
#into the same super cell, 0 means no           #
#modification                                   #
#type in filename,nx,ny,nz in order             #
#-----------------------------------------------#
def ContcarToXyz(filename,nx,ny,nz):
    ratio=0.85
    f=open(filename)
    comment=f.readline().replace('\n',"")
    l0=float(f.readline())
    a1=f.readline().split()
    a2=f.readline().split()
    a3=f.readline().split()
    lx=l0*(float(a1[0])+float(a2[0])+float(a3[0]))
    ly=l0*(float(a1[1])+float(a2[1])+float(a3[1]))
    lz=l0*(float(a1[2])+float(a2[2])+float(a3[2]))
    elem=f.readline().split()
    num=f.readline().split()
    mode=f.readline().split()
    if mode[0][0].lower() == 's': #selective dynamics
          f.readline()
    if len(elem)!=len(num):
       print "elements and numbers are different!"
       return None
    else:
       total=0
       coordinates=[]
       for n in num:
           total=total+int(n)
       print total*nx*ny*nz
       print total*nx*ny*nz
       for j in range(len(elem)):
            for k in range(int(num[j])):
                  aList=f.readline().split()
                  temp=[]
                  for i in range(3):
                         temp.append(aList[i])
                  x=l0*(float(temp[0])*float(a1[0])+float(temp[1])*float(a2[0])+float(temp[2])*float(a3[0]))
                  y=l0*(float(temp[0])*float(a1[1])+float(temp[1])*float(a2[1])+float(temp[2])*float(a3[1]))
                  z=l0*(float(temp[0])*float(a1[2])+float(temp[1])*float(a2[2])+float(temp[2])*float(a3[2]))
                  if ratio != 0:
                         if x>ratio*lx:
                              x=x-lx
                         if y>ratio*ly:
                              y=y-ly
                         if z>ratio*lz:
                              z=z-lz         
                  coordinates.append((elem[j],x,y,z))                  
                  k=k+1               
            j=j+1
 
    f.close()
    multicells=[]
    for atom in range(total):
       for i in range(nx):
          for j in range(ny):
             for k in range(nz):
                      x=coordinates[atom][1]+i*float(a1[0])*l0+j*float(a2[0])*l0+k*float(a3[0])*l0
                      y=coordinates[atom][2]+i*float(a1[1])*l0+j*float(a2[1])*l0+k*float(a3[1])*l0
                      z=coordinates[atom][3]+i*float(a1[2])*l0+j*float(a2[2])*l0+k*float(a3[2])*l0
                      multicells.append((coordinates[atom][0],x,y,z))
                      k=k+1
             j=j+1 
          i=i+1
       atom=atom+1    

    for i in range(total*nx*ny*nz):
        print multicells[i][0],'\t','%.10f'%multicells[i][1],'\t','%.10f'%multicells[i][2],'\t','%.10f'%multicells[i][3]  

import sys
filename=sys.argv[1]
nx=int(sys.argv[2])
ny=int(sys.argv[3])
nz=int(sys.argv[4])
ContcarToXyz(filename,nx,ny,nz)

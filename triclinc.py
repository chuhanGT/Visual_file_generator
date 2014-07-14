#   triclinic BZ with the same ion positions as in high symmetric structure
#------------------------------------------------------------------------------

import math
def vector(a,b,c,alpha,beta,gamma): # lattice constants and angles, return lattice vectors in cartisian coordiantes
    if a <= 0 or b<=0 or c<=0 or alpha<=0 or beta <=0 or gamma<=0:
         print 'Parameters error!'
         return None
    
    if alpha + beta <= gamma or alpha + gamma <= beta or gamma+beta <=alpha:
         print 'structure not exists!'
         return None
    Alpha=math.radians(alpha)
    Beta=math.radians(beta)
    Gamma=math.radians(gamma)
    x=[a,0,0]
    y=[0,0,0]
    z=[0,0,0]
    y[0]=b*math.cos(Gamma)
    y[1]=b*math.sin(Gamma)
    z[0]=c*math.cos(Beta)
    z[1]=c*(math.cos(Alpha)/(math.sin(Gamma))**2-math.cos(Beta)*math.cos(Gamma)/math.sin(Gamma))
    cz2=(c*math.sin(Alpha))**2-(z[0]-c*math.cos(Alpha)*math.cos(Gamma))**2-(z[1]-c*math.cos(Alpha)*math.sin(Gamma))**2
    z[2]=math.sqrt(cz2)
    return x,y,z

def position(nx,ny,nz): # fractional positions the same as cubic one
    lx=1.0/nx
    ly=1.0/ny
    lz=1.0/nz
    Ba=[]
    Zr=[]
    O=[]
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                 x1=0.5*lx+i*lx
                 y1=0.5*ly+j*ly
                 z1=0.5*lz+k*lz
                 Ba.append((x1,y1,z1))
                 x2=i*lx
                 y2=j*ly
                 z2=k*lz
                 Zr.append((x2,y2,z2))
                 O.append((x1,y2,z2))
                 O.append((x2,y1,z2))
                 O.append((x2,y2,z1))
    for i in Ba:
        print '%.8f'%i[0], '%.8f'%i[1],'%.8f'%i[2]
    for i in Zr:
        print '%.8f'%i[0], '%.8f'%i[1],'%.8f'%i[2]
    for i in O:
        print '%.8f'%i[0], '%.8f'%i[1],'%.8f'%i[2]

import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
alpha=float(sys.argv[4])
beta=float(sys.argv[5])
gamma=float(sys.argv[6])
nx=int(sys.argv[7])
ny=int(sys.argv[8])
nz=int(sys.argv[9])
v=vector(a,b,c,alpha,beta,gamma)
if v!=None:
  print 'supercell ',nx,ny,nz
  print '1.00000000'
  for i in v:
    print '%.8f'%(i[0]*nx), '%.8f'%(i[1]*ny),'%.8f'%(i[2]*nz)
  print 'Ba     Zr     O  '
  print nx**3 ,ny**3, 3*nz**3
  print 'Direct'
  position(nx,ny,nz)

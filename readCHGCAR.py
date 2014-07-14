# can be used to read both CHGCAR and LOCPOT  ##
##____________________________________________##

import sys
filename=sys.argv[1]
f=open(filename)
#first line should be 3 integers indicating 
#x y z indexes
first=f.readline()
x=int(first.split()[0])
y=int(first.split()[1])
z=int(first.split()[2])

zchg=[] # average charge density along z, contains z numbers
a=f.readline()
cx=1
cy=1
cz=1
while a:
  for i in a.split():
     print cx, cy, cz, i
     if cx < x:
        cx+=1
     else:
        cx=1
        if cy < y:
           cy+=1
        else:
           cy=1
           cz+=1
  a=f.readline()

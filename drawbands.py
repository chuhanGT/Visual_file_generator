import math
import sys
def readfile(filename): #reading bands parts from OUTCAR and return a list of all the bands
        f=open(filename)
        allbands=f.readlines()
        result=[]
        for item in allbands:
                if 'k-point' not in item and 'band' not in item and '--' not in item:
                        temp=item.split(' ')
                        energy=[]
                        for i in temp:
                                if i != '':
                                        energy.append(i)
                        result.append(float(energy[1]))
                elif 'k-point' in item:
                        result.append(item)
        f.close()
        return result

def ReadBands(alist,bNum): #bNum is the total number of bands at each k-point, reutrn a dictionary of bands cooresponding to their k-points
        pN=int(len(alist)/(bNum+1))
        allbands={}
        for point in range(pN):
                kpoint=()
                try:
                        temp=alist[point*(bNum+1)].split(' ')
                        temp2=[]
                        for item in temp:
                                if item != '':
                                        temp2.append(item)
                        kpoint=(float(temp2[-3]),float(temp2[-2]),float(temp2[-1]))
                except:
                        print ("error!")
                        return None
                if kpoint in allbands.keys():
                        pass
                else:
                        allbands[kpoint]=[]
                        for band in range(bNum):
                                allbands[kpoint].append(alist[point*(bNum+1)+band+1])
                        allbands[kpoint].sort()
        return allbands

def floatEqual(f1,f2):
        epsilon=0.005
        return abs(f1-f2)<epsilon

def findline(StartPt,EndPt,adic):
        if StartPt == EndPt:
                print ("The same points!")
                return None
        vector=(EndPt[0]-StartPt[0],EndPt[1]-StartPt[1],EndPt[2]-StartPt[2])
        zero=[]
        for i in range(3):
                if floatEqual(vector[i],0.0):
                        zero.append(i)
        aline={}
        for item in list(adic.keys()):
                newvector=(item[0]-StartPt[0],item[1]-StartPt[1],item[2]-StartPt[2])
                newzero=[]
                for i in range(3):
                        if newvector[i]==0:
                                newzero.append(i)
                if len(zero) == len(newzero):
                        if len(zero) == 0:
                                r=vector[0]/newvector[0]
                                if floatEqual(r*newvector[1],vector[1]) and floatEqual(r*newvector[2],vector[2]):
                                    aline[item]=adic[item]
                        elif len(zero)==1:
                                key=zero[0]
                                keys=[0,1,2]
                                index=keys.index(key)
                                del keys[index]
                                if newvector[key]==0:
                                        r=vector[keys[0]]/newvector[keys[0]]
                                        if floatEqual(r*newvector[keys[1]],vector[keys[1]]):
                                                aline[item]=adic[item]
                        elif len(zero) ==2:
                                k1=zero[0]
                                k2=zero[1]
                                if newvector[k1]==0 and newvector[k2]==0:
                                        aline[item]=adic[item]
        aline[StartPt]=adic[StartPt]
        return aline

def distance(a,b):
        return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

def drawline(StartPt,EndPt,basis,adic,band): #put the kpoints in one-dimensional and start with basis, return (k-point,energy of bandth band)
        aline=findline(StartPt,EndPt,adic)
        newdic={}
        for item in aline.keys():
                dis=math.sqrt((item[0]-StartPt[0])**2+(item[1]-StartPt[1])**2+(item[2]-StartPt[2])**2)
                newdic[dis]=aline[item][band-1]
        kpoints=list(newdic.keys())
        smallest=min(kpoints)
        result=[]
        for k in kpoints:
                result.append((round(basis+k-smallest,5),newdic[k]))
        result.sort()
        return result

        
                        
        
                        
file=sys.argv[1]
nbands=int(sys.argv[2])
start=int(sys.argv[3])
end=int(sys.argv[4])
alist=readfile(file)
adic=ReadBands(alist,nbands)
G=(0.000,0.000,0.000)
X=(0.000,0.500,0.500)
W=(0.250,0.500,0.750)
U=(0.250,0.625,0.625)
L=(0.500,0.500,0.500)
K=(0.375,0.375,0.750)
for band in range(start,end+1):
        f=open(str(band),"w")
        basis=0
        seg1=drawline(G,X,basis,adic,band)
        basis=basis+distance(G,X)
        seg2=drawline(X,W,basis,adic,band)
        basis=basis+distance(X,W)
        seg3=drawline(W,K,basis,adic,band)
        basis=basis+distance(W,K)
        seg4=drawline(K,G,basis,adic,band)
        basis=basis+distance(K,G)
        seg5=drawline(G,L,basis,adic,band)
        basis=basis+distance(G,L)
        seg6=drawline(L,U,basis,adic,band)
        basis=basis+distance(L,U)
	seg7=drawline(U,W,basis,adic,band)
        basis=basis+distance(U,W)
	seg8=drawline(W,L,basis,adic,band)
        basis=basis+distance(W,L)
	seg9=drawline(L,K,basis,adic,band)
        data=seg1+seg2[1:]+seg3[1:]+seg4[1:]+seg5[1:]+seg6[1:]+seg7[1:]+seg8[1:]+seg9[1:]
        for item in data:
                line=str(item[0])+"  "+str(item[1])+"\n"
                f.write(line)
        f.close()
        



                        

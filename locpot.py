# calculating local potentials by using information in LOCPOT #
# deleting all lines before the x,y,z grid numbers (line 102) #
#-------------------------------------------------------------#

import sys

class LOCPOT:

	def __init__(self,file):
              self.filename=file
              f=open(file)
              self.grid=f.readline().split() # string type
              f.close()

	def XYavg(self):
 	      f=open(self.filename)
              f.readline()
              totplane = int(self.grid[0])*int(self.grid[1])
              count = 0
              plane = 0
              pot=[]
              a=f.readline()
              while a:
                 for i in a.split():
                     plane += float(i)
                     count += 1
                     if count == totplane:
                        count = 0
                        pot.append(plane/totplane)
                        plane = 0 
                 a=f.readline()
              f.close()
              if count == 0 and plane == 0:
                 return pot
              else:
                  print ("error!")
                  return None

filename=sys.argv[1]
app=LOCPOT(filename)
zpot=app.XYavg()
for i in zpot:
   print i
 

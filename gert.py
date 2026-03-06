import math
class GERT:
 def __init__(self):self.G,self.E,self.R=0,0,0.1
 def control(self,e):
  g=0.95*(self.G+self.R*self.E+e)
  e=0.5*(self.E+math.tanh(g))
  r=0.1*max(min(g/max(e,1e-8),1),-1)
  self.G,self.E,self.R=g,e,r
  return self.G*0.236

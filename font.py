# - font plugin for gizmocad
from gcutils import interp
from fontsecession import fontdata as letter
from cgi import CGI
from bezier import Bezier
from line import Line
class Font():
	def __init__(self,cgi,keys):
		self.name='font'
		self.drawable=False
		keys['f']=self.name
		self.debug=False
	def event(self,pg,cgi,event,state,layer):
		if event.type==pg.KEYDOWN and event.key==pg.K_f:
			#                      [center[x,y],radius]
			#cgi.data[layer]['bezier'].append([[0,0],[0,10],[10,10],[10,0]])
			#cgi.selection[layer]['bezier'].append(False)
			#glyph(r,l)
			#for i in range(len(letter))
			#	move(self.glyph(1,i,cgi),(i*10,0))
			self.glyph(1,14,cgi)
			return True
		else:
			return False
	def move(self,cgi):
		for layer in cgi.data.keys():
			for oType in cgi.data[layer].keys() :
				for dat in cgi.data[layer][oType]:
					cgi.data[layer][oType].append(dat)
	def generate(self,char,cgi=False):
		if not cgi:
			cgi=CGI()
		Bezier(cgi,{})
		Font(cgi,{})
		self.glyph(1,char,cgi)
		return cgi
	def draw(self,pg,win,clr,dat,zoom,panx,pany):
		pass
	def box(self,dat):
		return (0,0,0,0)
	def move(self,dat,vec):
		vx,vy=vec
		out=[]
		for pnt in dat:
			x,y=pnt
			out.append([x+vx,y+vy])
		return out
	def ip(self,x,xs,xe,ys,ye):
		return ys+(x-xs)*((ye-ys)/(xe-xs))
	def ip2d(self,x,xs,xe,ys,ye):
		if self.debug:print('font.ip2d',ys,ye)
		if self.debug:print('font.ip2d ys',ys[0])
		if self.debug:print('font.ip2d ys',ye[0])
		if self.debug:print('font.ip2d',ys[0],ye[0])
		out=[self.ip(x,xs,xe,ys[0],ye[0]),self.ip(x,xs,xe,ys[1],ye[1])]
		if self.debug:print('font.ip2d out',out)
		return out
	def typePoint(self,l,i,n):
		if len(letter[l][letter[l][i][n][0]-1])==2:
			return self.linePoint(l,i,n)
		else:
			return self.bzPoint(l,i,n)
	def linePoint(self,l,i,n):
		return self.ip2d(letter[l][i][n][1],0,1,
			self.safePoint(l,letter[l][i][n][0]-1,0),
			self.safePoint(l,letter[l][i][n][0]-1,1))
	def bzPoint(self,l,i,n):
		return self.ip2d(letter[l][i][n][1],0,1,
			self.ip2d(letter[l][i][n][1],0,1,
				self.safePoint(l,letter[l][i][n][0]-1,0),
				self.safePoint(l,letter[l][i][n][0]-1,1)),
			self.ip2d(letter[l][i][n][1],0,1,
				self.safePoint(l,letter[l][i][n][0]-1,1),
				self.safePoint(l,letter[l][i][n][0]-1,2))
		)
	def isPoint(self,l,i,n):
		if letter[l][i][n][0]:
			return self.typePoint(l,i,n)
		else:
			return letter[l][i][n][1]
	def safePoint(self,l,i,n):
		if letter[l][i][0]:
			return self.isPoint(l,i,n)
		else:
			return letter[l][i][n][1]
	def snapStroke(self,l,i,r,cgi):
		if self.debug:print("font.snapStroke(i)",i)
		if len(letter[l][i])==2:
			return self.stroke(self.safePoint(l,i,0),self.safePoint(l,i,1),r,cgi)
		else:
			if self.debug:print("font.snapStroke len(letter[i])<>2")
			return self.strokeBz(self.safePoint(l,i,0),self.safePoint(l,i,1),self.safePoint(l,i,2),r,cgi)
	def glyph(self,r,l,cgi):
		print("len(letter)",len(letter))
		for i in range(len(letter[l])):
			self.snapStroke(l,i,r,cgi)
	def stroke(self,start,end,r,cgi):#create line (end points)
		cgi.addEntity('line',[start,end])
	def strokeBz(self,start,mid,end,r,cgi):#create bezier curve (control&end points)
		cgi.addEntity('bezier',[start,mid,end,end])

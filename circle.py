# - circle plugin for gizmocad
from gcutils import worldToScreen
from cgi import CGI
class Circle():
	def __init__(self,cgi,keys):
		self.name='circle'
		self.drawable=True
		
		#self.data=     {'0':{'lines':[]}}
		#self.selection={'0':{'lines':[]}}
		self.addTypeCgi(cgi)
		keys['c']=self.name
	def addTypeCgi(self,cgi):
		for layer in cgi.data.keys():
			cgi.data[layer]['circle']=[]
			cgi.selection[layer]['circle']=[]
	def event(self,pg,cgi,event,state,layer):
		if event.type==pg.KEYDOWN and event.key==pg.K_c:
			#                      [center[x,y],radius]
			cgi.data[layer]['circle'].append([[0,0],10])
			cgi.selection[layer]['circle'].append(False)
			return True
		else:
			return False
	def generate(self,pnt,rad,cgi):
		cgi.addEntity('circle',[pnt,rad])
		return cgi
	def draw(self,pg,win,clr,dat,zoom,panx,pany):
		cnt,rad=dat
		x,y=cnt
		sx,sy=worldToScreen(x,y,zoom,panx,pany)
		r,t=worldToScreen(rad,0,zoom,0,0)
		pg.draw.circle(win,clr,(sx,sy),r,1)
	def unpack(self,dat):
		p,r=dat
		x,y=p
		return x,y,r
	def box(self,dat):
		cnt,rad=dat
		x,y=cnt
		return (x-rad,y-rad,x+rad,y+rad)
	def move(self,dat,vec):
		xa,ya=dat[0]
		xv,yv=vec
		return [[xa+xv,ya+yv],dat[1]]
	def scale(self,dat,sc):
		xa,ya=dat[0]
		return [[xa*sc,ya*sc],dat[1]*sc]
	def rotate(self,dat,c):
		return [rotatePnt(dat[0],c),dat[1]]

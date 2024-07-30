# - besier curves plugin for gizmocad
from gcutils import interp,worldToScreen,rotatePnt
class Bezier():
	def __init__(self,cgi,keys):
		self.name='bezier'
		self.drawable=True
		self.iterations=100
		#self.data=     {'0':{'bezier':[[[0,0],[0,10],[10,10],[10,0]]]}}
		#self.selection={'0':{'bezier':[False]}}
		self.prime(cgi)
		keys['c']=self.name
		self.debug=False
	def prime(self,cgi):
		for layer in cgi.data.keys():
			cgi.data[layer]['bezier']=[]
			cgi.selection[layer]['bezier']=[]
	def event(self,pg,cgi,event,state,layer):
		if event.type==pg.KEYDOWN and event.key==pg.K_b:
			#                      [center[x,y],radius]
			cgi.data[layer]['bezier'].append([[0,0],[0,10],[10,10],[10,0]])
			cgi.selection[layer]['bezier'].append(False)
			return True
		else:
			return False
	def draw(self,pg,win,clr,dat,zoom,panx,pany):
		#xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(dat)
		pntsa=[]
		for pnt in dat:
			x,y=pnt
			if self.debug:print('besier draw xy',x,y)
			pntsa.append(worldToScreen(x,y,zoom,panx,pany))
		if self.debug:print('besier draw pntsa',pntsa)
		pntsb=[]
		xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(pntsa)
		for i in range(self.iterations+1):
			#efg
			#hj
			#interp(xm,xa,xb,ya,yb)
			xe=interp(i,0,self.iterations,xa,xb)
			ye=interp(i,0,self.iterations,ya,yb)
			xf=interp(i,0,self.iterations,xb,xc)
			yf=interp(i,0,self.iterations,yb,yc)
			xg=interp(i,0,self.iterations,xc,xd)
			yg=interp(i,0,self.iterations,yc,yd)
			xh=interp(i,0,self.iterations,xe,xf)
			yh=interp(i,0,self.iterations,ye,yf)
			xj=interp(i,0,self.iterations,xf,xg)
			yj=interp(i,0,self.iterations,yf,yg)
			xk=interp(i,0,self.iterations,xh,xj)
			yk=interp(i,0,self.iterations,yh,yj)
			pntsb.append([xk,yk])
		for i in range(len(pntsb)-1):
			pg.draw.line(win,clr,pntsb[i],pntsb[i+1])
	def unpack(self,dat):
		a,b,c,d=dat
		xa,ya=a
		xb,yb=b
		xc,yc=c
		xd,yd=d
		return xa,ya,xb,yb,xc,yc,xd,yd
	def box(self,dat):
		xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(dat)
		xs=[xa,xb,xc,xd]
		ys=[ya,yb,yc,yd]
		#return (x-rad,y-rad,x+rad,y+rad)
		return (min(xs),min(ys),max(xs),max(ys))
	def move(self,dat,vec):
		xv,yv=vec
		xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(dat)
		return [[xa+xv,ya+yv],[xb+xv,yb+yv],[xc+xv,yc+yv],[xd+xv,yd+yv]]
	def scale(self,dat,sc):
		xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(dat)
		return [[xa*sc,ya*sc],[xb*sc,yb*sc],[xc*sc,yc*sc],[xc*sc,yc*sc]]
	def rotate(self,dat,e):
		a,b,c,d=dat
		return [rotatePnt(a,e),rotatePnt(b,e),rotatePnt(c,e),rotatePnt(d,e)]

# - besier curves plugin for gizmocad
from gcutils import interp,worldToScreen,rotatePnt
from cgi import CGI
class Line():
	def __init__(self,cgi,keys):
		self.name='Line'
		self.drawable=True
		self.tmppnt=[0,0]
		self.state='init'
		#self.data=     {'0':{'lines':[]}}
		#self.selection={'0':{'lines':[]}}
		self.prime(cgi)
		keys['l']=self.name
		self.debug=True
	def prime(self,cgi):
		for layer in cgi.data.keys():
			cgi.data[layer]['line']=[]
			cgi.selection[layer]['line']=[]
	def event(self,pg,cgi,event,state,layer):
		cmdMsg=''
		if self.state=='inactive':
			if event.type==pg.KEYDOWN and event.key==pg.K_l:
				self.state=='expectPntA'
				cmdMsg='Click to make first point'#command message
		elif self.state=='expectPntA':
			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.state=='expectPntB'
					cmdMsg='Click to make second point'#command message
					cgi.addEntity(layer,'line',[tmppnt,[mwx,mwy]])
					sax,say=worldToScreen(tmppnt[0],tmppnt[1],zoom,panx,pany)
					pg.draw.line(win,YELLOW,(sax,say),(msx,msy))
			#                      [center[x,y],radius]
			cgi.addEntity(layer,'line',[[0,0],[0,10]])
			#cgi.data[layer]['bezier'].append([[0,0],[0,10],[10,10],[10,0]])
			#cgi.selection[layer]['bezier'].append(False)
			return True
		else:
			return False
	def generate(self,pnta,pntb,cgi=CGI()):
		if self.debug:print('generate (o)',cgi.data)
		cgi.addEntity('line',[pnta,pntb])
		if self.debug:print('generate (o)(o)',cgi.data)
		return cgi
	def draw(self,pg,win,clr,dat,zoom,panx,pany):
		#xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(dat)
		pntsa=[]
		for pnt in dat:
			x,y=pnt
			if self.debug:print('line draw xy',x,y)
			pntsa.append(worldToScreen(x,y,zoom,panx,pany))
		if self.debug:print('line draw pntsa',pntsa)
		pntsb=[]
		xa,ya,xb,yb=self.unpack(pntsa)
		pg.draw.line(win,clr,(xa,ya),(xb,yb))
	def unpack(self,dat):
		if self.debug:print('lin.unpack.dat',dat)
		a,b=dat
		xa,ya=a
		xb,yb=b
		return xa,ya,xb,yb
	def box(self,dat):
		xa,ya,xb,yb,xc,yc,xd,yd=self.unpack(dat)
		xs=[xa,xb,xc,xd]
		ys=[ya,yb,yc,yd]
		#return (x-rad,y-rad,x+rad,y+rad)
		return (min(xs),min(ys),max(xs),max(ys))
	def move(self,dat,vec):
		xv,yv=vec
		xa,ya,xb,yb=self.unpack(dat)
		return [[xa+xv,ya+yv],[xb+xv,yb+yv]]
	def scale(self,dat,sc):
		xa,ya,xb,yb=self.unpack(dat)
		return [[xa*sc,ya*sc],[xb*sc,yb*sc]]
	def rotate(self,dat,c):
		a,b=dat
		return [rotatePnt(a,c),rotatePnt(b,c)]

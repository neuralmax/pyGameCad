# - besier curves plugin for gizmocad
from gcutils import interp,worldToScreen
from font import Font
from bezier import Bezier
from circle import Circle
from line import Line
from cgi import CGI
from fontsecession import fontdata
from math import atan2,degrees
class Parametric():
	def __init__(self,cgi,keys,plugins):
		self.name='Parametric'
		self.drawable=False
		self.state='init'
		self.plugins=plugins
		self.debug=True
		#self.data=     {'0':{'lines':[]}}
		#self.selection={'0':{'lines':[]}}
		keys['p']=self.name
	def move(self,cgi,vec):
		for layer in cgi.data.keys():
			for oType in cgi.data[layer].keys():
				for i,dat in enumerate(cgi.data[layer][oType]):
					cgi.data[layer][oType][i]=self.plugins[oType].move(dat,vec)
	def scale(self,cgi,sc):
		for layer in cgi.data.keys():
			for oType in cgi.data[layer].keys():
				for i,dat in enumerate(cgi.data[layer][oType]):
					cgi.data[layer][oType][i]=self.plugins[oType].scale(dat,sc)
	def rotate(self,cgi,ang):
		for layer in cgi.data.keys():
			for oType in cgi.data[layer].keys():
				for i,dat in enumerate(cgi.data[layer][oType]):
					cgi.data[layer][oType][i]=self.plugins[oType].rotate(dat,ang)
	def square(self,pnt,center=False):
		tx,ty=pnt
		if center:
			sx=-tx/2
			sy=-ty/2
			fx=tx/2
			fy=ty/2
		else:
			sx=0
			sy=0
			fx=tx
			fy=ty
		cgisq=CGI()
		cgitl=CGI()
		line=Line(cgisq,{})
		cgitl=line.generate((sx,sy),(sx,fy))
		cgisq=cgisq+cgitl
		cgitl=line.generate((sx,sy),(fx,sy))
		cgisq=cgisq+cgitl
		cgitl=line.generate((sx,fy),(fx,fy))
		cgisq=cgisq+cgitl
		cgitl=line.generate((fx,sy),(fx,fy))
		cgisq=cgisq+cgitl
		return cgisq
	def demoTexInLine(self,cgi):
		for i,charname in enumerate(fontdata.keys()):
			#charname='a'
			if self.debug:print('parametric.charname',charname,i)
			cgit=CGI()
			font=Font(cgit,{})
			line=Line(cgit,{})
			cgit=font.generate(charname)
			if self.debug:print('parametric.event.move')
			self.move(cgit,[i*110,0])
			if self.debug:print('parametric.event.add')
			cgi=cgi+cgit
	def textOnCurve(self,cgi,text,s,r,top):
		step=degrees(atan2(s,r))*1.2
		#step=atan2(r,s)
		font=Font(cgi,{})
		line=Line(cgi,{})
		if self.debug:print('parametric.demoTextOnCurve.step r s',step,r,s)
		if top:
			r=-r
		for i,ch in enumerate(text):
			if self.debug:print('parametric.demoTextOnCurve.i',i,ch)
			cgit=CGI()
			font=Font(cgit,{})
			line=Line(cgit,{})
			cgit=font.generate(ch,cgit)
			if top:
				self.move(cgit,[-50,-100])
			else:
				self.move(cgit,[-50,0])
			self.scale(cgit,0.01*s)
			self.move(cgit,[0,r])
			self.rotate(cgit,step*i-step*((len(text)-1)/2))
			cgi=cgi+cgit
		return cgi
	def demoEngravingSpindleTest(self,cgi):
		fx,fy=30,40
		cgit=CGI()
		line=Line(cgit,{})
		cgit=line.generate((-5,-5),(-5,fy),cgit)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=line.generate((-5,-5),(fx,-5),cgit)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=line.generate((-5,fy),(fx,fy),cgit)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=line.generate((fx,-5),(fx,fy),cgit)
		cgi=cgi+cgit
		for i in range(10):
			cgit=CGI()
			line=Line(cgit,{})
			cgit.createLayer(str(i+1),(i*25,0,255-i*25),10+i*10,10)
			#cgit.createLayer(str(i+1),(i*25,0,255-i*25),i*1,10)
			line.generate([0,i*3],[30,i*3],cgit)
			cgi=cgi+cgit
	def demoSingleLineTest(self,cgi):
		fx,fy=30,40
		cgit=CGI()
		line=Line(cgit,{})
		cgit=line.generate((-5,-5),(-5,fy),cgit)
		cgi=cgi+cgit
		del cgit
		#if self.debug:print('parametric.cgit.data a (o)',cgit.data)
		cgit=CGI()
		if self.debug:print('parametric.cgit.data b (o)(o)',cgit.data)
		cgit=line.generate((-5,-5),(55,-5),cgit)
		if self.debug:print('parametric.cgit.data b (o)(o)(o)',cgit.data)
		cgi=cgi+cgit
	def demoTextSizeTest(self,cgi):
		cgit=CGI()
		line=Line(cgit,{})
		cgit=CGI()
		cgit=line.generate((-5,-5),(-5,45),cgit)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=line.generate((-5,-5),(55,-5),cgit)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=line.generate((-5,45),(55,45),cgit)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=line.generate((55,-5),(55,45),cgit)
		cgi=cgi+cgit
		for j,sc in enumerate([3,2.5,2,1.5,1]):
			for i,ch in enumerate('enter the matrix'):
				if self.debug:print('parametric.demoTextSizeTest.i',i,ch)
				cgit=CGI()
				cgit.createLayer('1',(255,255,0),50,10)
				font=Font(cgit,{})
				line=Line(cgit,{})
				cgit=font.generate(ch,cgit)
				self.move(cgit,[110*i,0])
				self.scale(cgit,0.01)
				self.scale(cgit,sc)
				self.move(cgit,[0,j*10])
				cgi=cgi+cgit
	def demoHoleSizeTest(self,cgi):
		cgit=self.square([30,50],center=True)
		self.move(cgit,[0,10])
		cgi=cgi+cgit
		circle=Circle(cgi,{})
		for i,r in enumerate([8,8.1,8.2]):
			if self.debug:print('parametric.demoHoleSizeTest.i',i,r)
			cgit=CGI()
			cgit.createLayer('1',(255,255,0))
			circle=Circle(cgit,{})
			cgit=circle.generate([0,10*i],r/2,cgit)
			if self.debug:print('parametric.demoHoleSizeTest.cgit',cgit)
			cgi=cgi+cgit
			cgis=self.square([1,4],center=True)
			self.move(cgis,[5.5+4,10*i])
			cgi=cgi+cgis
	def demoKeyTest(self,cgi,text):
		cgit=self.square([30,30],center=True)
		cgi=cgi+cgit
		cgit=CGI()
		font=Font(cgi,{})
		line=Line(cgi,{})
		cgit.createLayer('1',(255,255,0))
		circle=Circle(cgit,{})
		cgit=circle.generate([0,0],8.1/2,cgit)
		cgit.createLayer('3',(0,255,0),50,10)#engrave
		cgit=CGI()
		cgit=self.textOnCurve(cgit,'enterthematrix',2,15,True)
		cgi=cgi+cgit
		cgit=CGI()
		cgit=self.textOnCurve(cgit,'1235456',2,18,True)
		cgi=cgi+cgit


	def event(self,pg,cgi,event,state,layer):
		cmdMsg=''
		if event.type==pg.KEYDOWN and event.key==pg.K_p:
			if self.debug:print('parametric.event')
			#self.demoTexInLine(cgi)
			#self.demoTextOnCurve(cgi)
			#self.demoEngravingSpindleTest(cgi)
			#self.demoTextSizeTest(cgi)
			#self.demoSingleLineTest(cgi)

			#self.demoHoleSizeTest(cgi)
			#self.textOnCurve(cgi,'enterthematrix',2,15,True)
			#self.textOnCurve(cgi,'1235456',2,18,True)
			#demoTextOnCurve(self,cgi,text,s,r,top):
			self.demoKeyTest(cgi,'enter')


			#cgi.addEntity(layer,'line',[[0,0],[0,10]])
			#cgi.data[layer]['bezier'].append([[0,0],[0,10],[10,10],[10,0]])
			#cgi.selection[layer]['bezier'].append(False)
			return True
		else:
			return False
	def draw(self,pg,win,clr,dat,zoom,panx,pany):
		pass
	def unpack(self,dat):
		pass
	def box(self,dat):
		pass

# - besier curves plugin for gizmocad
from gcutils import interp,worldToScreen
from font import Font
from bezier import Bezier
from circle import Circle
from line import Line
from cgi import CGI
from fontsecession import fontdata
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
	def demoTextOnCurve(self,cgi):
		for i,ch in enumerate('yyyyyyyyy'):
			if self.debug:print('parametric.demoTextOnCurve.i',i,ch)
			cgit=CGI()
			font=Font(cgit,{})
			line=Line(cgit,{})
			cgit=font.generate(ch)
			self.move(cgit,[-50,-500])
			self.rotate(cgit,i*18)
			cgi=cgi+cgit
	def demoEngravingSpindleTest(self,cgi):
		fx,fy=35,40
		cgit=CGI()
		line=Line(cgit,{})
		cgit=line.generate((-5,-5),(-5,fy))
		cgi=cgi+cgit
		cgit=line.generate((-5,-5),(fx,-5))
		cgi=cgi+cgit
		cgit=line.generate((-5,fy),(fx,fy))
		cgi=cgi+cgit
		cgit=line.generate((fx,-5),(fx,fy))
		cgi=cgi+cgit
		for i in range(10):
			cgit=CGI()
			line=Line(cgit,{})
			cgit.createLayer(str(i+1),(i*25,0,255-i*25),i*10,10)
			line.generate([0,i*3],[30,i*3],cgit)
			cgi=cgi+cgit
	def demoTextSizeTest(self,cgi):
		cgit=CGI()
		line=Line(cgit,{})
		cgit=line.generate((-5,-5),(-5,45))
		cgi=cgi+cgit
		cgit=line.generate((-5,-5),(55,-5))
		cgi=cgi+cgit
		cgit=line.generate((-5,45),(55,45))
		cgi=cgi+cgit
		cgit=line.generate((55,-5),(55,45))
		cgi=cgi+cgit
		for j,sc in enumerate([3,2.5,2,1.5,1]):
			for i,ch in enumerate('enter the matrix'):
				if self.debug:print('parametric.demoTextOnCurve.i',i,ch)
				cgit=CGI()
				cgit.createLayer('1',(255,255,0),10,10)
				font=Font(cgit,{})
				line=Line(cgit,{})
				cgit=font.generate(ch,cgit)
				self.move(cgit,[110*i,0])
				self.scale(cgit,0.01)
				self.scale(cgit,sc)
				self.move(cgit,[0,j*10])
				cgi=cgi+cgit
	def demoHoleSizeTest(self,cgi):
		fx,fy=10,30
		cgit=CGI()
		line=Line(cgit,{})
		cgit=line.generate((-5,-5),(-5,fy))
		cgi=cgi+cgit
		cgit=line.generate((-5,-5),(fx,-5))
		cgi=cgi+cgit
		cgit=line.generate((-5,fy),(fx,fy))
		cgi=cgi+cgit
		cgit=line.generate((fx,-5),(fx,fy))
		cgi=cgi+cgit
		for i,r in enumerate([6,6.1,6.2]):
			if self.debug:print('parametric.demoHoleSizeTest.i',i,r)
			cgit=CGI()
			cgit.createLayer('1',(255,255,0))
			circle=Circle(cgit,{})
			cgit=circle.generate([0,10*i],r/2,cgit)
			if self.debug:print('parametric.demoHoleSizeTest.cgit',cgit)
			cgi=cgi+cgit
	def demoKey(self,cgi):
		for i,ch in enumerate('yyyyyyyyy'):
			if self.debug:print('parametric.demoTextOnCurve.i',i,ch)
			cgit=CGI()
			font=Font(cgit,{})
			line=Line(cgit,{})
			cgit=font.generate(ch)
			self.move(cgit,[-50,-500])
			self.rotate(cgit,i*18)
			cgi=cgi+cgit
	def event(self,pg,cgi,event,state,layer):
		cmdMsg=''
		if event.type==pg.KEYDOWN and event.key==pg.K_p:
			if self.debug:print('parametric.event')
			#self.demoTexInLine(cgi)
			#self.demoTextOnCurve(cgi)
			#self.demoEngravingSpindleTest(cgi)
			#self.demoTextSizeTest(cgi)
			self.demoHoleSizeTest(cgi)


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

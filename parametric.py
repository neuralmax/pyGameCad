# - besier curves plugin for gizmocad
from gcutils import interp,worldToScreen
from font import Font
from bezier import Bezier
from circle import Circle
from line import Line
from cgi import CGI
from fontsecession import fontdata
from math import atan2,degrees
import csv
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
	def square(self,pnt,center=False,layerName='0'):
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
		if layerName!='0':cgisq.createLayer(layerName,(255,255,0))
		line=Line(cgisq,{})
		cgitl=CGI()
		if layerName!='0':cgitl.createLayer(layerName,(255,255,0))
		cgitl=line.generate((sx,sy),(sx,fy),cgitl)
		cgisq=cgisq+cgitl
		cgitl=CGI()
		if layerName!='0':cgitl.createLayer(layerName,(255,255,0))
		cgitl=line.generate((sx,sy),(fx,sy),cgitl)
		cgisq=cgisq+cgitl
		cgitl=CGI()
		if layerName!='0':cgitl.createLayer(layerName,(255,255,0))
		cgitl=line.generate((sx,fy),(fx,fy),cgitl)
		cgisq=cgisq+cgitl
		cgitl=CGI()
		if layerName!='0':cgitl.createLayer(layerName,(255,255,0))
		cgitl=line.generate((fx,sy),(fx,fy),cgitl)
		cgisq=cgisq+cgitl
		return cgisq
	def textInLine(self,cgi,text):
		for i,charname in enumerate(fontdata.keys()):
		#for i,charname in enumerate(text):
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
	def textOnCurve(self,cgi,text,s,r,type='top'):
		curLayer=cgi.curLayer
		step=degrees(atan2(s,r))*1.2
		#step=atan2(r,s)
		font=Font(cgi,{})
		line=Line(cgi,{})
		if self.debug:print('parametric.demoTextOnCurve.step r s',step,r,s)
		if type=='top':
			rx=0
			ry=-r
		elif type=='bottom':
			rx=0
			ry=r
			step=-step
		elif type=='right':
			rx=r
			ry=0
		for i,ch in enumerate(text):
			if self.debug:print('parametric.demoTextOnCurve.i',i,ch)
			cgit=CGI()
			font=Font(cgit,{})
			line=Line(cgit,{})
			cgit=font.generate(ch,cgit)
			if type=='top':
				self.move(cgit,[-50,-100])
			elif type=='bottom':
				self.move(cgit,[-50,0])
			elif type=='right':
				self.move(cgit,[0,-50])
			self.scale(cgit,0.01*s)
			self.move(cgit,[rx,ry])
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
		cgit=CGI()
		cgit=line.generate((fx,-5),(fx,fy),cgit)
		cgi=cgi+cgit
		for i in range(10):
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
			self.move(cgis,[5+4,10*i])
			cgi=cgi+cgis
	def generateKey(self,text,textt,textb,textl,textr,frame=True):
		cgi=CGI()
		cgi.createLayer('0',(255,255,255),feedRate=200)
		font=Font(cgi,{})
		line=Line(cgi,{})
		if frame:
			cgit=CGI()
			cgit=self.square([30,30],center=True)
			cgi=cgi+cgit
		cgit=CGI()
		cgit.createLayer('1',(255,255,0))
		circle=Circle(cgit,{})
		cgit=circle.generate([0,0],8.1/2,cgit)
		cgi=cgi+cgit

		cgis=self.square([1,4],center=True,layerName='1')
		self.move(cgis,[5+4,0])
		self.rotate(cgis,90)
		cgi=cgi+cgis

		arrowCodes=['<|','>|','^|','v|']
		cgit=CGI()
		cgi.createLayer('3',(0,255,0),50,10)#engrave
		if text in arrowCodes:
			cgit=font.generate(text)
			self.move(cgit,[-50,-50])
			self.scale(cgit,0.01*2)
			self.move(cgit,[0,-8])
		else:
			cgit=self.textOnCurve(cgit,text,2,8,'top')
		#cgi=cgi+cgit
		cgi.toLayer(cgit,'3')
		cgit=CGI()
		cgit=self.textOnCurve(cgit,textt,2,11,'top')
		#cgi=cgi+cgit
		cgi.toLayer(cgit,'3')
		cgit=CGI()
		if textb=='cc':
			cgit=font.generate(textb)
			self.move(cgit,[-50,-50])
			self.scale(cgit,0.01*2)
			self.move(cgit,[0,11])
		else:
			cgit=self.textOnCurve(cgit,textb,2,11,'bottom')
		#cgi=cgi+cgit
		cgi.toLayer(cgit,'3')

		cgit=CGI()
		font=Font(cgit,{})
		line=Line(cgit,{})
		cgit=font.generate(textl)
		self.move(cgit,[-50,-50])
		self.scale(cgit,0.01*4)
		self.move(cgit,[-10,0])
		#cgi=cgi+cgit
		cgi.toLayer(cgit,'3')

		symbolCodes=['<=','<>','>=','$$','^|','<|','>|','v|','cc','||']
		cgit=CGI()
		if len(textr)==1 or textr in symbolCodes:
			font=Font(cgit,{})
			line=Line(cgit,{})
			cgit=font.generate(textr)
			self.move(cgit,[-50,-50])
			self.scale(cgit,0.01*4)
			self.move(cgit,[10,0])
		else:
			cgit=self.textOnCurve(cgit,textr,2,11,'right')
		#cgi=cgi+cgit
		cgi.toLayer(cgit,'3')
		return cgi
	def generateKeyboard(self):
		cgi=CGI()
		font=Font(cgi,{})
		line=Line(cgi,{})
		border=5
		cgit=CGI()
		cgit=self.square([30*10+border*2,30*4+border*2],center=False)
		self.move(cgit,[0,-30*4-border*2])
		cgi=cgi+cgit
		#mounting holes
		for x,y in [[0+border,0-border],[30*10+border,0-border],[0+border,-30*4-border],[30*10+border,-30*4-border]]:
			cgit=CGI()
			cgit.createLayer('1',(255,255,0))
			circle=Circle(cgit,{})
			cgit=circle.generate([x,y],4.1/2,cgit)
			cgi=cgi+cgit
		testAxis=False
		if testAxis:
			cgit=CGI()
			cgit=self.square([10,10],center=True)
			cgi=cgi+cgit
		data=[]
		with open('keyboard.csv', newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in reader:
				readrow=[]
				for cell in row:
					readrow.append(str(cell).lower())
				data.append(readrow)
				#print(', '.join(row))
		generateText=True
		if generateText:
			i=1
			for y in range(4):
				for x in range(10):
					d=data[i]
					print('generateKeyboard.d',d)
					# 0   1      2    3     4
					# top toptop left right bottom
					cgit=self.generateKey(d[0],d[1], d[4], d[2], d[3],frame=False)
					#generateKey(self,    text,textt,textb,textl,textr,frame=True):
					self.move(cgit,[30*x+15+border,-30*4+15-border+30*y])
					cgi=cgi+cgit
					i+=1
		return cgi
	def event(self,pg,cgi,event,state,layer):
		cmdMsg=''
		if event.type==pg.KEYDOWN and event.key==pg.K_p:
			if self.debug:print('parametric.event')
			#self.textInLine(cgi,'')
			#self.scale(cgi,0.01*5)
			#self.demoTextOnCurve(cgi)
			#self.demoEngravingSpindleTest(cgi)
			#self.demoTextSizeTest(cgi)
			#self.demoSingleLineTest(cgi)

			#self.demoHoleSizeTest(cgi)
			#self.textOnCurve(cgi,'enterthematrix',2,15,True)
			#self.textOnCurve(cgi,'1235456',2,18,True)
			#self.textOnCurve(cgi,'1235456',2,18,'top')

			#()_<>;=^-+=:?/*,.#[]?~|\{}
			#self.textInLine(cgi,"!@$%&'()[]{}\\/|-+=_<>^#*?~.,;:")
			#             0v   1v   2v   3v   4v   5    6    7v
			#symbolCodes=['<=','<>','>=','$$','^|','<|','>|','v|']
			#font=Font(cgi,{})
			#cgit=font.generate(symbolCodes[6])
			#cgit=font.generate('cc')
			#self.textOnCurve(cgi,'!@$',2,18,'top')

			#--demoTextOnCurve(self,cgi,text,s,r,top):
			#cgit=self.generateKey('top','toptop','bottom','l','r')#cgi,text,textt,textb,textl,textr)
			#cgit=self.generateKey('top','+','+','s','s')#cgi,text,textt,textb,textl,textr)
			#self.move(cgit,[15,-15])
			cgit=self.generateKeyboard()
			cgi=cgi+cgit
			cgi.layers['0']['feedRate']=300
			cgi.layers['1']['feedRate']=300
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

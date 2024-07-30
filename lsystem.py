import sys, pygame, math,copy,random
class turtle:
	def __init__(self,inX=0,inY=0,inAngle=90,inSpeed=10,inDir=270):
		self.pos=[[inX,inY],[inX,inY]]
		#self.lastX=inX
		#self.lastY=inY
		#self.x=inX
		#self.y=inY
		self.speed=inSpeed
		self.dir=inDir
		self.angle=inAngle
		self.stack=[]
		self.pack=[]
	def go(self):
		xb=self.pos[0][0]
		yb=self.pos[0][1]
		xa=xb+cos(self.dir)*self.speed
		ya=yb+sin(self.dir)*self.speed
		del(self.pos)
		self.pos=[[xa,ya],[xb,yb]]
	def turn(self,inDir):
		self.dir+=inDir
		if self.dir<0:self.dir+=360
		if self.dir>360:self.dir-=360
	def bezierTurn(self,inDir):
		xc=self.pos[0][0]
		yc=self.pos[0][1]
		xb=xc+cos(self.dir)*self.speed
		yb=yc+sin(self.dir)*self.speed
		self.turn(inDir)
		xa=xb+cos(self.dir)*self.speed
		ya=yb+sin(self.dir)*self.speed
		del(self.pos)
		self.pos=[[xa,ya],[xb,yb],[xc,yc]]
	def tpush(self):
		self.stack.append([self.pos[0][0],self.pos[0][1],self.dir])
	def tpop(self):
		tmp=self.stack.pop()
		self.pos=[[tmp[0],tmp[1]],[tmp[0],tmp[1]]]
		self.dir=tmp[2]
	def leaf(self):
		tmpSpeed=self.speed
		self.speed/=2
		self.pack=[]
		self.go()
		self.pack.append(self.pos)
		self.turn(self.angle)
		for a in range(2):
			for b in range(2):
				self.go()
				self.pack.append(self.pos)
				self.bezierTurn(-self.angle)
				self.pack.append(self.pos)
			self.go()
			self.pack.append(self.pos)
		self.speed=tmpSpeed
	def setSpeed(self,inSpeed):
		self.speed=inSpeed
	def translate(self,glyph):
		if glyph=='F' or glyph=='G' or glyph=='A' or glyph=='B' or glyph=='1':
			self.go()
			self.pack=[]
		elif glyph=='+':self.turn(self.angle)
		elif glyph=='-':self.turn(-self.angle)
		elif glyph=='<':
			self.bezierTurn(self.angle)
			self.pack=[]
		elif glyph=='>':
			self.bezierTurn(-self.angle)
			self.pack=[]
		elif glyph=='0':self.leaf()
		elif glyph=='[':
			self.tpush()
			self.turn(self.angle/2)
		elif glyph==']':
			self.tpop()
			self.turn(-self.angle/2)
	def getTrace(self):
		return self.pos,self.pack


def sin(a):return math.sin(math.radians(a))
def cos(a):return math.cos(math.radians(a))

def interp(x,xa,xb,ya,yb):
	return ya+(x-xa)*((yb-ya)/(xb-xa*1.0))

def norm2d(x,y):
	m=math.sqrt(x*x+y*y)
	return x/m,y/m

def stroke(ab,n,t,sc):
	diam=3
	a=ab[0]
	b=ab[1]
	ax=(a[0]+t[0])*sc
	ay=(a[1]+t[1])*sc
	bx=(b[0]+t[0])*sc
	by=(b[1]+t[1])*sc
	if len(ab)>2:
		c=ab[2]
		cx=(c[0]+t[0])*sc
		cy=(c[1]+t[1])*sc
	lean=.5
	for i in range(n+1):
		if len(ab)==2:
			x=int(interp(i,0,n,ax,bx))
			y=int(interp(i,0,n,ay,by))
		else:
			dx=int(interp(i,0,n,ax,bx))
			dy=int(interp(i,0,n,ay,by))
			ex=int(interp(i,0,n,bx,cx))
			ey=int(interp(i,0,n,by,cy))
			x=int(interp(i,0,n,dx,ex))
			y=int(interp(i,0,n,dy,ey))
		#size manipulation
		'''dlin=interp(i,0,n,a[2],b[2])
		angl=interp(i,0,n,0,180)
		sinPlane=abs(sin(angl))
		d=int(interp(sinPlane,1,0,lean*dlin,dlin))'''
		#print(m,lean,d,l,o)
		#color manipulation
		cr=interp(i,0,n,255,0)
		cg=interp(i,0,n,0,0)
		cb=interp(i,0,n,0,255)
		clr=cr,cg,cb
		pygame.draw.circle(screen,clr, [x,y],diam)

def trunk(l,v,n):
	pnt=[random.randint(0,width),height,20]
	for i in range(n):
		pntNew=copy.copy(pnt)
		pntNew[1]-=l
		pntNew[1]+=(random.random()-0.5)*v
		pntNew[0]+=(random.random()-0.5)*v
		stroke(pnt,pntNew,100)
		pnt=copy.copy(pntNew)

def lsystem(genome,rules,angle,iter):
	#teo=turtle(width/2, height/2,angle)
	teo=turtle(0,0,angle)#adapt to cad (self,inX=0,inY=0,inAngle=90,inSpeed=10,inDir=270):
	for i in range(iter):
		genomeNext=''
		for g in genome:
			notFoundRule=True
			for r in rules:
				if g==r[0]:
					notFoundRule=False
					genomeNext+=r[1]
			if notFoundRule:genomeNext+=g
		del(genome)
		genome=copy.copy(genomeNext)
		del(genomeNext)
	#print(genome)
	#genome='F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F'
	#genome='1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0'
	trace=[]

	for gen in genome:
		teo.translate(gen)
		pos,pack=teo.getTrace()
		if pack:
			for p in pack:
				trace.append(p)
		else:
			trace.append(pos)
	return genome,trace


if __name__ == "__main__":
	print('running test code')
	pygame.init()
	size = width, height = 1200,800
	black = 0, 0, 0
	white=255,255,255
	red=255,0,0
	blue=0,0,255
	screen = pygame.display.set_mode(size)
	image = pygame.Surface(size, pygame.SRCALPHA, 32)
	image = image.convert_alpha()
	blacka=0,0,0,1
	image.fill(blacka)



	genome,rules,angle='0',[['1','11'],['0','1[0]0']],90#Pythagoras tree
	#genome,rules,angle='F',[['F','F+F-F-F+F']],90#Koch curve besier
	#genome,rules,angle='F',[['F','F<F>F>F<F']],90#Koch curve
	#genome,rules,angle='F-G-G',[['F','F-G+F+G-F'],['G','GG']],120#Sierpinski triangle
	#genome,rules,angle='FX',[['X','X+YF+'],['Y','-FX-Y']],90#Dragon curve
	#genome,rules,angle='X',[['X','F-[[X]+]+F[+FX]-X'],['F','FF']],25#Fractal plant
	#genome,rules,angle='X',[['X','F-[[X]+X]+F[+FX]-X'],['F','FF']],25#Fractal plant


	genome,trace=lsystem(genome,rules,angle)
	print(genome)
	print(len(trace))
	v=0
	vraise=True
	n=0
	lastX,lastY=0,0
	mouseDragging=False
	translate=[0,0]
	counter=0
	scale=1.0
	while 1:
		#counter+=1
		#pygame.display.set_caption('counter: '+str(counter))
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			elif event.type==pygame.MOUSEBUTTONDOWN:
				#pygame.image.save(screen,"screenshot.png")
				#print ("screenshot done")
				#pygame.display.set_caption('done')
				if not mouseDragging and pygame.mouse.get_pressed()[0]:
					lastX,lastY=pygame.mouse.get_pos()
					pygame.display.set_caption('mouseDragging '+str(mouseDragging))
					mouseDragging=True
			elif event.type == pygame.MOUSEWHEEL:
				scale+=event.y*1.1-1
			elif event.type==pygame.MOUSEBUTTONUP:
				mouseDragging=False
				pygame.display.set_caption('mouseUp '+str(mouseDragging))
		if mouseDragging:
			mX, mY = pygame.mouse.get_pos()
			translate[0] -= lastX - mX
			translate[1] -= lastY - mY
			lastX=mX
			lastY = mY
			pygame.display.set_caption('mouseDragging ' + str(translate) + ' ' + str(mouseDragging))
			#print('mouseDragging')
		screen.blit(image, (0,0))
		#pygame.draw.circle(screen, white, [100,100], 10)
		#stroke([width/2,height/2,50],[x,y,10],100)
		#xm,ym=pygame.mouse.get_pos()
		#stroke([width/2,height/2,50],[xm,ym,10],100)

		for step in trace:
			stroke(step,10,translate,scale)

		#trunk(100,100,5)
		pygame.display.flip()
		#n+=1
		#if n>99 and n<200:pygame.image.save(screen,'screen'+str(n-99).zfill(4)+'.png')

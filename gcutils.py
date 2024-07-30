from math import sin as sinr
from math import cos as cosr
from math import radians
def sin(a):
	return sinr(radians(a))
def cos(a):
	return cosr(radians(a))
def rotatePnt(pnt,a):
	x,y=pnt
	return [x*cos(a)-y*sin(a),x*sin(a)+y*cos(a)]
def worldToScreen(wox,woy,zoom,panx,pany):
	return (wox-panx)*zoom,(woy-pany)*zoom
def screenToWorld(scx,scy,zoom,panx,pany):
	return scx/zoom+panx,scy/zoom+pany
def resetLSys(angle,iterations,type):
	cgi=CGI()
	if type==0:
		genome,trace=lsystem('0',[['1','11'],['0','1[0]0']],angle,iterations)#Pythagoras tree
	elif type==1:
		genome,trace=lsystem('F',[['F','F+F-F-F+F']],angle,iterations)#Koch curve besier

	elif type==2:
		genome,trace=lsystem('F',[['F','F<F>F>F<F']],angle,iterations)#Koch curve
	elif type==3:
		genome,trace=lsystem('F-G-G',[['F','F-G+F+G-F'],['G','GG']],angle,iterations)#Sierpinski triangle

	elif type==4:
		genome,trace=lsystem('FX',[['X','X+YF+'],['Y','-FX-Y']],angle,iterations)#Dragon curve

	elif type==5:
		genome,trace=lsystem('X',[['X','F-[[X]+]+F[+FX]-X'],['F','FF']],angle,iterations)#Fractal plant
	elif type==6:
		genome,trace=lsystem('X',[['X','F-[[X]+X]+F[+FX]-X'],['F','FF']],angle,iterations)#Fractal plant

		#genome,rules,angle=,90#Koch curve
		#genome,rules,angle=,120#Sierpinski triangle
		#genome,rules,angle=,90#Dragon curve
		#genome,rules,angle=,25#Fractal plant
		#genome,rules,angle=,25#Fractal plant
	print('lsystem',len(trace),genome)
	print('lsystem',trace[0])
	for lin in trace:
		if len(lin)==2:
			cgi.addEntity('lines',lin)
		elif len(lin)==3:
			cgi.addEntity('lines',[lin[0],lin[1]])
			cgi.addEntity('lines',[lin[1],lin[2]])
		else:
			raise Exception('len(lin) != [2,3]',len(lin))
	return cgi
def interp(xm,xa,xb,ya,yb):
	return ya+(xm-xa)*(yb-ya)/(xb-xa)

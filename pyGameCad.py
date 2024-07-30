# to do
#--- for keyboard project ---
#[ ] generate keyboard
#[ ] export to GCODE
#[V] parametric generate test for spindle speed
#[V] parametric generate test for font size
#[V] cgi create layer
#[V] scale
#[V] rotate
#[V] font on arc
#[V] complete all characters in the font
#[V] fix font looks different than in openscad
#[V] write doc of fonts format
#[V] reverse y axis on font interpreter
#[V] parametric system (cgi mixer)
#[V] remake font to use dict for letter in string:font(letter)
#[V] suppress prints with if debug
#[V] move line to plugin
#[V] circle
#[V] layers
#[V] besier curves
#[V] center line font from openscad
#[V] move line funcionality to plugin
#[V] fix zoom
#---  -------
#[ ] add delete funcion
#[ ] arc
#[ ] snap
#[ ] axis snap
#[ ] join to polyline
#[ ] export to dxf
#[ ]
# done
#[V]line extenter
#[V]load csv with wkt column https://docs.python.org/3/library/csv.html
#[V]convert wkt into cgi Lines
#[V] change functions
#[V] select
#[V] load from json
#[V] safe to json
#[V] draw
#[V] zoom extends [Z]
#[V] pan zoom https://www.youtube.com/watch?v=ZQ8qtAizis4
import pygame as pg
import sys,os
from pygame.locals import RESIZABLE,VIDEORESIZE,HWSURFACE,DOUBLEBUF
from random import randint
from time import sleep
from copy import copy
from lsystem import lsystem
from gcutils import *
from cgi import CGI

debug=False

cgi=CGI()
commands={}
#--- plugins
plugins={}
from circle import Circle
plugins['circle']=Circle(cgi,commands)
from bezier import Bezier
plugins['bezier']=Bezier(cgi,commands)
from font import Font
plugins['font']=Font(cgi,commands)
from line import Line
plugins['line']=Line(cgi,commands)
from parametric import Parametric
plugins['parametric']=Parametric(cgi,commands,plugins)
from exportgcode import ExportGcode
plugins['exportgcode']=ExportGcode(cgi,commands)




def progman(cmd,scp,mod=''):#command manager (commandName,scope)
	#shope ~[evt:event,mbc:mouseButtonClicked]
	global actCmd
	global cmdMsg
	global cmdPhz
	global tmppnt
	global cgi
	global lSystemAngle
	global lSystemIter
	global lSystemType
	#global selection
	if cmd=='select':
		if scp=='evt':
			actCmd='select'
			cmdMsg='Click to select entities'#command message
			cmdPhz=0#command phase
			cgi.selection={'lines':[False for n in cgi.data['lines']]}
		if scp=='mbc':
			tstsrf=pg.Surface(size)
			for i,line in enumerate(cgi.data['lines']):
				if debug:print('line',line)
				a,b=line
				tstsrf.fill(BLACK)
				sax,say=worldToScreen(a[0],a[1])
				sbx,sby=worldToScreen(b[0],b[1])
				pg.draw.line(tstsrf,WHITE,(sax,say),(sbx,sby),3)
				if debug:print('<<tstsrf.get_at((msx,msy))>>',tstsrf.get_at((msx,msy)))
				if tstsrf.get_at((msx,msy))[0]>0:
					cgi.selection['lines'][i]=True
					break
	elif cmd=='delete':
		if scp=='evt':
			actCmd='select'
			cmdMsg='deleted selected entities'#command message
			cmdPhz=0#command phase
			lng=len(cgi.data['line'])
			for i in range(lng):
				if cgi.selection['line'][lng-i-1]:
					cgi.data['line'].pop(lng-i-1)
			cgi.selection={'line':[False for n in cgi.data['line']]}
	elif cmd=='arc':
		if scp=='evt':
			actCmd='arc'
			cmdMsg='Click to make first point'#command message
			cmdPhz=0#command phase
	elif cmd=='polyline':
		if scp=='evt':
			actCmd='polyline'
			cmdMsg='made polyline from selected enitities'#command message
			cmdPhz=0#command phase
	elif cmd=='lsystem':
		if scp=='evt':
			if mod=='':
				actCmd='lsystem'
				cmdMsg='lsystem'#command message
				cmdPhz=0#command phase
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
			elif mod=='up':
				lSystemIter+=1
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
			elif mod=='down':
				lSystemIter-=1
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
			elif mod=='left':
				lSystemAngle-=10
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
			elif mod=='right':
				lSystemAngle+=10
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
			elif mod=='pgup':
				if lSystemType>0:
					lSystemType-=1
				lSystemAngle=lSystemTypeAngle[lSystemType]
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
			elif mod=='pgdown':
				if lSystemType<6:
					lSystemType+=1
				lSystemAngle=lSystemTypeAngle[lSystemType]
				cgi=resetLSys(lSystemAngle,lSystemIter,lSystemType)
		if scp=='drw':
			if cmdPhz==1:
				sax,say=worldToScreen(tmppnt[0],tmppnt[1])
				pg.draw.line(win,YELLOW,(sax,say),(msx,msy))

#--end of progman
def pluginEvent(plugins,event):
	eventConsumed=False
	for plugin in plugins.keys():
		#cgi,event,state,layer
		eventConsumed=plugins[plugin].event(pg,cgi,event,state,cgi.curLayer)
		if eventConsumed:break
	return eventConsumed
#from data import cgi
actCmd='line'#activeCommand
cmdMsg='Click to make first point'#command message
cmdPhz=0#command phase
state=''
lSystemAngle=90
lSystemIter=5
lSystemType=0
lSystemTypeAngle=[90,90,90,120,90,25,25]
#os.environ['SDL_VIDEO_CENTERED']='1'# You have to call this before pygame.init()
#f=open('data.json')
#cgi=json.load(f)
#cgi.loadjson('data.json')

if debug:print('cgi',type(cgi),cgi)
pg.init()
info=pg.display.Info()#You have to call this before pygame.display.set_mode()
sizeFull=info.current_w,info.current_h
size=(sizeFull[0],sizeFull[1]-60)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
win=pg.display.set_mode(size,RESIZABLE)
pg.display.set_caption('hw'+str(size))
panx=0
pany=0
panStartX=0
panStartY=0
zoom=1
zoomfactor=1.5
#actCmd='Select'#activeCommand
actCmd='line'#activeCommand
cmdMsg='Click to make first point'#command message
cmdPhz=0#command phase
tmppnt=[0,0]
#selection={'lines':[False for n in cgi['lines']]}
panning=False
fullScr=False
mainLoop=True
while mainLoop:
	mb1,mb2,mb3=pg.mouse.get_pressed()
	msx,msy=pg.mouse.get_pos()
	mwx,mwy=screenToWorld(msx,msy,zoom,panx,pany)
	#mpx=(msx-panx)/zoom
	#mpy=(msy-pany)/zoom
	for event in pg.event.get():
		if event.type==pg.QUIT:
			mainLoop=False
		elif event.type==VIDEORESIZE:
			size=event.dict['size']
			win=pg.display.set_mode(size,HWSURFACE|DOUBLEBUF|RESIZABLE)
		elif pluginEvent(plugins,event):pass
		elif event.type==pg.KEYDOWN:
			if event.key==pg.K_q:
				mainLoop=False
			if event.key==pg.K_z:
				mxx=-9999
				mxy=-9999
				mnx=9999
				mny=9999
				for layer in cgi.layers.keys():
					for oType in cgi.data[layer].keys():
						for obj in cgi.data[layer][oType]:
							if oType=='line':
								for pnt in line:
									x,y=pnt
									if mxx<x:mxx=x
									if mxy<y:mxy=y
									if mnx>x:mnx=x
									if mny>y:mny=y
							else:
								minx,miny,maxx,maxy=plugins[oType].box(obj)
								if maxx>mxx:mxx=maxx
								if maxy>mxy:mxy=maxy
								if minx<mnx:mnx=minx
								if miny<mny:mny=miny
				panx=-mnx
				pany=-mny
				zoom=size[0]/(mxx-mnx)
				if debug:print('zoom all',size[0],zoom)
			if event.key==pg.K_l:progman('line','evt')
			if event.key==pg.K_s:progman('select','evt')
			if event.key==pg.K_c:progman('select','evt')
			if event.key==pg.K_d:progman('delete','evt')
			if event.key==pg.K_a:progman('arc','evt')
			if event.key==pg.K_p:progman('polyline','evt')
			if event.key==pg.K_y:progman('lsystem','evt')
			if event.key==pg.K_e:progman('extender','evt')
			if event.key==pg.K_UP:progman(actCmd,'evt','up')
			if event.key==pg.K_DOWN:progman(actCmd,'evt','down')
			if event.key==pg.K_LEFT:progman(actCmd,'evt','left')
			if event.key==pg.K_RIGHT:progman(actCmd,'evt','right')
			if event.key==pg.K_PAGEUP:progman(actCmd,'evt','pgup')
			if event.key==pg.K_PAGEDOWN:progman(actCmd,'evt','pgdown')
			if event.key==pg.K_s and pg.key.get_mods() & pg.KMOD_CTRL:
				cgi.safeJson()
			if event.key==pg.K_RETURN and pg.key.get_mods() & pg.KMOD_SHIFT:
				pg.display.set_caption('pressed: SHIFT + A ')
				if debug:print("pressed: SHIFT + K_RETURN")
				if fullScr:
					win=pg.display.set_mode(size, RESIZABLE)
					fullScr=False
				else:
					pg.display.set_mode(sizeFull,pg.FULLwin)
					fullScr=True
				sleep(1)
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				progman(actCmd,'mbc')
			elif event.button == 4:
				mwxo=mwx
				mwyo=mwy
				zoom*=zoomfactor
				mwxn,mwyn=screenToWorld(msx,msy,zoom,panx,pany)
				panx+=(mwxo-mwxn)
				pany+=(mwyo-mwyn)
			elif event.button == 5:
				mwxo=mwx
				mwyo=mwy
				zoom/=zoomfactor
				mwxn,mwyn=screenToWorld(msx,msy,zoom,panx,pany)
				panx+=(mwxo-mwxn)
				pany+=(mwyo-mwyn)
	if mb3:
		if not panning:
			panning=True
		else:
			panx+=(panStartX-msx)/zoom
			pany+=(panStartY-msy)/zoom
		panStartX=msx
		panStartY=msy
	else:
		panning=False
	pg.display.set_caption('gizmocad activeCommand:'+actCmd+' phz:'+str(cmdPhz)+' size:'+str(size)+' coords:'+str(mwx)+','+str(mwy))
	if debug:print('cgi',type(cgi),cgi.data)
	win.fill(BLACK)
	for layer in cgi.data.keys():
		clr=cgi.layers[layer]['color']
		for oType in cgi.data[layer].keys():
			if oType=='line':
				for i,line in enumerate(cgi.data[layer]['line']):
					if debug:print('a,b',line)
					a,b=line
					sax,say=worldToScreen(a[0],a[1],zoom,panx,pany)
					sbx,sby=worldToScreen(b[0],b[1],zoom,panx,pany)
					if cgi.selection[layer]['line'][i]:clr=BLUE
					#else:clr=WHITE
					pg.draw.line(win,clr,(sax,say),(sbx,sby))
			else:
				for plugin in plugins.keys():
					if plugins[plugin].drawable:
						for i,dat in enumerate(cgi.data[layer][plugin]):
							plugins[plugin].draw(pg,win,clr,dat,zoom,panx,pany)
	progman(actCmd,'drw',cmdPhz)
	pg.display.update()
pg.quit()

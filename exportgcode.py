import json
from bezier import Bezier
from line import Line
from circle import Circle
from cgi import CGI
class ExportGcode:
	def __init__(self,cgi,keys):
		#         {layer{objectType[objectData]}}
		self.name='ExportGcode'
		self.drawable=False
		#self.data=     {'0':{'lines':[]}}
		#self.selection={'0':{'lines':[]}}
		keys['g']=self.name
		self.debug=True
	def event(self,pg,cgi,event,state,layer):
		if event.type==pg.KEYDOWN and event.key==pg.K_g:
			if self.debug:print('ExportGcode.event')
			print('ExportGcode.event.cgi.data',cgi.data)
			cgit=CGI()
			line=Line(cgit,{})
			bezier=Bezier(cgit,{})
			circle=Circle(cgit,{})
			data=''
			beginingStart=[
				'%',
				'G21         ; Set units to mm',
				'G90         ; Absolute positioning',
				'G64P0.1Q0.02',
			]
			for l in beginingStart:data+=l+'\n'
			beginingEnd=[
				';',
				'; Operation:    0',
				'; Type:         Mill Cut',
				'; datas:        189',
				'; Direction:    Conventional',
				'; Rapid Z:      0',
				'; Start Z:      0',
				'; End Z:        -1',
				'; Pass Depth:   1',
				'; Plunge rate:  1000 mm/min',
				'; Cut rate:     500 mm/min',
				';',
				'; Retract',
				'G0 Z0.000'
			]
			for l in beginingEnd:data+=l+'\n'
			layerNms=cgi.layers.keys()
			layerNms=sorted(layerNms,reverse=True)
			counter=0

			for layerNm in layerNms:
				data+=';\n'
				data+=';=--(o)(o)--=\n'
				spinsp=cgi.layers[layerNm]['M4']
				data+='M4 S'+str(spinsp)+' ; spindle speed\n'
				power=cgi.layers[layerNm]['power']
				feedRate=cgi.layers[layerNm]['feedRate']
				data+='M68 E0 Q'+str(power)+'; set power of laser\n'
				for oType in cgi.data[layerNm].keys():
					for dat in cgi.data[layerNm][oType]:
						data+='; data '+str(counter)+'\n'
						counter+=1
						data+='\n'
						if oType=='line':
							xa,ya,xb,yb=line.unpack(dat)
							data+='G0 X'+str(xa)+' Y'+str(-ya)+'; Rapid to initial position\n'
							data+='G0 Z0.000\n'
							data+='G1 Z-1.000 F'+str(feedRate)+' ; plunge\n'
							data+='; cut\n'
							data+='G1 X'+str(xb)+' Y'+str(-yb)+' F'+str(feedRate)+'\n'
						elif oType=='circle':
							x,y,r=circle.unpack(dat)
							data+='G0 X'+str(x)+' Y'+str(-y+r)+'; Rapid to initial position\n'
							data+='G0 Z0.000\n'
							data+='G1 Z-1.000 F'+str(feedRate)+' ; plunge\n'
							data+='; cut\n'
							data+='G2 I'+str(0)+' J'+str(-r)+'\n'
						elif oType=='bezier':
							xa,ya,xb,yb,xc,yc,xd,yd=bezier.unpack(dat)
							data+='G0 X'+str(xa)+' Y'+str(-ya)+'; Rapid to initial position\n'
							data+='G0 Z0.000\n'
							data+='G1 Z-1.000 F'+str(feedRate)+' ; plunge\n'
							data+='; cut\n'
							#data+='G5 X'+str(xb-xa)+' Y'+str(-yb-ya)+' I'+str(xc-xa)+' J'+str(-yc+ya)+' P'+str(xd)+' Q'+str(-yd)+'\n'
							data+='G5.1 X'+str(xc)+' Y'+str(-yc)+' I'+str(xb-xa)+' J'+str(-yb+ya)+'\n'
						data+='G0 Z0.000 ; Retract\n'
			data+='M5          ; Switch tool offEnd\n'
			data+='%'
			with open('test.gcode', 'w') as file:
				file.write(data)
			return True
		else:
			return False

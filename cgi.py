import json
class CGI:
	def __init__(self):
		#         {layer{objectType[objectData]}}
		self.plugins=False
		self.data={'0':{'line':[]}}
		self.selection={'0':{'line':[]}}
		self.debug=False
		self.curLayer='0'
		self.layers={'0':{'color':(255,255,255),'M4':1000,'power':80,'feedRate':1000}}
	def loadJson(self,filename):
		f=open(filename)
		self.data=json.load(f)
		for layer in self.data.keys():
			self.selection={'line':[False for n in self.data[layer]['line']]}
	def safeJson():
		jsonObject=json.dumps(cgi.data,indent=4)
		with open('data.json','w') as outfile:
			outfile.write(jsonObject)
		with open('data.csv','w') as outfile:
			outfile.write('WKT,\n')
			for line in cgi.data['line']:
				outfile.write('"'+LineString(line).wkt+'"\n')
	def addEntity(self,oType,dat):
		if self.debug:print('cgi.addEntity',self.data,oType)
		self.data[self.curLayer][oType].append(dat)
		self.selection[self.curLayer][oType].append(False)
	def createLayer(self,lName,color=(255,0,0),m4=1000,power=80,feedRate=1000):
		#{'0':{'line':[]}}
		self.layers[lName]={'color':color,'M4':m4,'power':power,'feedRate':feedRate}
		self.data[lName]={}
		self.selection[lName]={}
		self.curLayer=lName
		for oType in self.data['0'].keys():
			self.data[lName][oType]=[]
			self.selection[lName][oType]=[]
	def __add__(self,other):
		if self.debug:print('cgi.add.self.data.begin -----------------(o)(o)-----')
		if self.debug:print('cgi.add.self.data',self.data)
		if self.debug:print('cgi.add.self.layers',self.layers)
		if self.debug:print('cgi.add.other.data',other.data)
		if self.debug:print('cgi.add.other.layers',other.layers)
		for layer in other.data.keys():
			if self.debug:print('cgi.add.layer',layer)
			if not layer in self.layers:
				self.createLayer(layer,other.layers[layer]['color'],other.layers[layer]['M4'],other.layers[layer]['power'],other.layers[layer]['feedRate'])
			else:
				self.curLayer=layer
			for oType in other.data[layer].keys() :
				if self.debug:print('cgi.add.otype',oType)
				if not oType in self.data[layer].keys():
					self.data[layer][oType]=[]
					self.selection[layer][oType]=[]
				for dat in other.data[layer][oType]:
					if self.debug:print('cgi.add.dat',dat)
					self.addEntity(oType,dat)
					#self.data[layer][oType].append(dat)
					#self.selection[layer][oType].append(False)
		return self
	def toLayer(self,other,targetLayer):
		if self.debug:print('cgi.add.self.data.begin -----------------(o)(o)-----')
		if self.debug:print('cgi.add.self.data',self.data)
		if self.debug:print('cgi.add.self.layers',self.layers)
		if self.debug:print('cgi.add.other.data',other.data)
		if self.debug:print('cgi.add.other.layers',other.layers)
		self.curLayer=targetLayer
		#if not targetLayer in self.layers:
		#	self.createLayer(targetLayer,other.layers[targetLayer]['color'],other.layers[layer]['M4'],other.layers[layer]['power'])
		for layer in other.data.keys():
			if self.debug:print('cgi.add.layer',layer)
			for oType in other.data[layer].keys() :
				if self.debug:print('cgi.add.otype',oType)
				if not oType in self.data[targetLayer].keys():
					self.data[targetLayer][oType]=[]
					self.selection[targetLayer][oType]=[]
				for dat in other.data[layer][oType]:
					if self.debug:print('cgi.add.dat',dat)
					self.addEntity(oType,dat)
					#self.data[layer][oType].append(dat)
					#self.selection[layer][oType].append(False)
		return self
	def getBox(self):#get boundin box
		mxx=-9999
		mxy=-9999
		mnx=9999
		mny=9999
		for layer in self.layers.keys():
			for oType in self.data[layer].keys():
				for obj in self.data[layer][oType]:
					if oType=='line':
						for pnt in obj:
							x,y=pnt
							if mxx<x:mxx=x
							if mxy<y:mxy=y
							if mnx>x:mnx=x
							if mny>y:mny=y
					else:
						minx,miny,maxx,maxy=self.plugins[oType].box(obj)
						if maxx>mxx:mxx=maxx
						if maxy>mxy:mxy=maxy
						if minx<mnx:mnx=minx
						if miny<mny:mny=miny
		return mxx,mxy,mnx,mny
	def getCentroid(self):
		mxx,mxy,mnx,mny=self.getBox()
		return (mxx-mnx)/2+mnx,(mxy-mny)/2+mny

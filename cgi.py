import json
class CGI:
	def __init__(self):
		#         {layer{objectType[objectData]}}
		self.data={'0':{'line':[]}}
		self.selection={'0':{'line':[]}}
		self.debug=True
		self.curLayer='0'
		self.layers={'0':{'color':(255,255,255),'M4':1000,'power':80}}
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
		if self.debug:print('cgi.addEntity',self.data)
		self.data[self.curLayer][oType].append(dat)
		self.selection[self.curLayer][oType].append(False)
	def createLayer(self,lName,color,m4=1000,power=80):
		#{'0':{'line':[]}}
		self.layers[lName]={'color':color,'M4':m4,'power':power}
		self.data[lName]={}
		self.selection[lName]={}
		self.curLayer=lName
		for oType in self.data['0'].keys():
			self.data[lName][oType]=[]
			self.selection[lName][oType]=[]
	def __add__(self,other):
		if self.debug:print('cgi.add.self.data',self.data)
		if self.debug:print('cgi.add.self.layers',self.layers)
		if self.debug:print('cgi.add.other.data',other.data)
		if self.debug:print('cgi.add.other.layers',other.layers)
		for layer in other.data.keys():
			if self.debug:print('cgi.add.layer',layer)
			if not layer in self.layers:
				self.createLayer(layer,other.layers[layer]['color'],other.layers[layer]['M4'],other.layers[layer]['power'])
			else:
				self.curLayer=layer
			for oType in other.data[layer].keys() :
				if self.debug:print('cgi.add.otype',oType)
				for dat in other.data[layer][oType]:
					if self.debug:print('cgi.add.dat',dat)
					self.addEntity(oType,dat)
					#self.data[layer][oType].append(dat)
					#self.selection[layer][oType].append(False)
		return self

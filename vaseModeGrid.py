# mase like solver for space filling grid structure ment to be printed with vase mode
from gcutils import worldToScreen
from cgi import CGI
class VaseModeGrid():
	def __init__(self,cgi,keys):
		self.name='vaseModeGrid'
		self.drawable=False
		self.countTo=1
		#self.data=     {'0':{'lines':[]}}
		#self.selection={'0':{'lines':[]}}
		#self.addTypeCgi(cgi)
		keys['v']=self.name
	def event(self,pg,cgi,event,state,layer):
		if event.type==pg.KEYDOWN and event.key==pg.K_v:
			#                      [center[x,y],radius]
			#cgi.data[layer]['circle'].append([[0,0],10])
			#cgi.selection[layer]['circle'].append(False)
			#test
			#cgi.addEntity('line',[[0,0],[10,10]])
			#cgi.createLayer('tmp')
			#cgi.addEntity('line',[[10,0],[20,10]])
			#cgi.addEntity('circle',[[20,20],10])
			#params
			m=4
			n=4
			#solve
			'''
			data=[#example of hand solution
				[[0,0],[1,0],[3,0],[3,0]],
				[[0,3],[1,2],[1,2],[2,2]],
				[[0,3],[1,3],[2,2],[2,3]],
				[[0,1],[3,1],[3,1],[2,3]],
			]
			'''
			'''
			data=[#example of hand solution
				[[[0,0],[0,0]],[[0,0],[1,0]],[[0,0],[1,1]],[[0,0],[1,1]],],
				[[[1,1],[0,0]],[[0,1],[1,0]],[[0,1],[1,0]],[[0,1],[0,1]],],
				[[[1,1],[0,0]],[[1,0],[1,0]],[[0,1],[1,1]],[[1,1],[0,1]],],
				[[[1,0],[0,0]],[[1,0],[1,1]],[[1,0],[1,1]],[[1,1],[0,1]],]
			]
			'''
			'''
			nbrsa=[
				[ 1, 0, 0],
				[ 1, 1,-1],
				[ 0, 0,-1],
				[-1, 0, 0],
				[ 0,-1,-1],
				[ 1,-1,-1],
			]
			nbrsb=[
				[ 0, 1, 1],
				[ 0, 1, 0],
				[-1, 1, 1],
				[-1, 0, 1],
				[ 0,-1, 0],
				[ 0, 0, 1],
			]'''
			# neighbourhood connections
			# 0 : z=1, d=1 <- horizontal leftwards
			# 1 : z=0, d=1 |v vertical downwards
			# 2 : z=1, d=2 -> horizontal rightwards
			# 3 : z=0, d=2 |^ vertical upwards
			# [ x<mod>, y<mod>, z(vertical/horzontal)<actual>, d(right,left,up,down)<actual> ]
			'''
			nbrs=[[#0
				[ 0,-1,0,1],
				[-1, 0,1,2],
				[ 0, 0,0,0],
			],[#1
				[-1, 1,1,2],
				[ 0, 1,0,2],
				[ 0, 1,1,1],
			],[#2
				[ 1, 1,0,2],
				[ 1, 1,1,1],
				[-1, 1,0,1],
			],[#3
				[ 0, 0,1,1],
				[ 0,-1,0,1],
				[-1, 0,0,1],
			]]
			'''
			#[z][d-1]=nc
			dirs=[[0,2],[1,3]]
			#init matrix
			data=[[[[0,0],[0,0]] for y in range(n)] for x in range(m)]
			front=[]
			#seed matrix with init front
			for i in range(1,n):
				front.append([0  ,i,0,1])
				front.append([m-1,i,0,2])
			for i in range(1,m):
				front.append([i,  0,1,1])
				front.append([i,n-1,1,2])
			#solve
			counter=0#limiting for testing
			self.countTo+=1
			while len(front)>0 and counter<self.countTo:
				counter+=1
				x,y,z,d=front.pop(0)
				endpointFree=True
				print('counter',counter,'dirs[z][d-1]',dirs[z][d-1])
				for nx,ny,nz,nd in nbrs[dirs[z][d-1]]:
					print('nx,ny,nz,nd',nx,ny,nz,nd)
					if x+nx<=0 and x+nx<m-1 and y+ny<=0 and y+ny<n-1:
						print('data[x+nx][y+ny][nz]',data[x+nx][y+ny][nz])
						if data[x+nx][y+ny][nz]!=nd:
							endpointFree=False
							break
				print('endpointFree',endpointFree)
				if endpointFree:
					data[x][y][z]=3
					for nx,ny,nz,nd in nbrs[dirs[z][d-1]]:
						if x+nx<0 and x+nx<m-1 and y+ny<0 and y+ny<n-1:
							if data[x+nx][y+ny][nz]!=0:
								front.append([[x+nx][y+ny][nz][nd]])
			'''
			#generate
			cgi.createLayer('maze',(0,255,0))
			for y,dat in enumerate(data):
				for x,c in enumerate(dat):
					if c[0][0]==1 and c[0][1]==0:
						cgi.addEntity('line',[[x*10,y*10],[x*10+8,y*10]])
					if c[0][0]==0 and c[0][1]==1:
						cgi.addEntity('line',[[x*10+2,y*10],[x*10+10,y*10]])
					if c[0][0]==1 and c[0][1]==1:
						cgi.addEntity('line',[[x*10,y*10],[x*10+10,y*10]])
					if c[1][0]==1 and c[1][1]==0:
						cgi.addEntity('line',[[x*10,y*10],[x*10,y*10+8]])
					if c[1][0]==0 and c[1][1]==1:
						cgi.addEntity('line',[[x*10,y*10+2],[x*10,y*10+10]])
					if c[1][0]==1 and c[1][1]==1:
						cgi.addEntity('line',[[x*10,y*10],[x*10,y*10+10]])
			cgi.createLayer('ends',(255,0,0))
			for y in range(m+1):
				for x in range(n+1):
					cgi.addEntity('circle',[[x*10,y*10],1])
			return True
		else:
			return False

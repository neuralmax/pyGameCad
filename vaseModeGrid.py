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

			n=4#x
			m=4#y
			#solve
			'''
			data=[#example of hand solution
				[[2,2,2,2],[2,2,1,2],[2,2,1,2],[2,2,1,2],[2,2,2,2]],
				[[2,1,2,2],[0,0,1,1],[1,0,1,1],[1,0,0,1],[2,2,2,1]],
				[[2,1,2,2],[0,1,1,1],[1,0,0,0],[1,1,0,1],[2,2,2,1]],
				[[2,1,2,2],[0,1,1,0],[1,1,1,0],[1,1,0,0],[2,2,2,1]],
				[[2,2,2,2],[1,2,2,2],[1,2,2,2],[1,2,2,2],[2,2,2,2]],
			]'''
			data=[[[[0,0],[0,0]] for y in range(n)] for x in range(m)]
			front=[]#[x,y,z]
			dirs=[[0,-1],[1,0],[0,1],[-1,0]]
			opos=[2,3,0,1]
			#seed matrix with dead ends init front
			for x,y in [[0,0],[0,m-1],[n-1,0],[n-1,m-1]]:#corners
				data[y][x]=[2,2,2,2]
			for x in range(1,n-2):#top bottom
				data[0][x]=[2,2,1,2]
				data[n-1][x]=[1,2,2,2]
				front.append([x,0,2])#[x,y,z]
				front.append([x,n-1,0])
			for y in range(1,m-2):#left right
				data[y][0]=[2,1,2,2]
				data[y][m-1]=[2,2,2,1]
				front.append([0,y,1])#[x,y,z]
				front.append([m-1,y,3])
			#solve
			counter=0#limiting for testing
			self.countTo+=1
			while len(front)>0 and counter<self.countTo:
				counter+=1
				x,y,z=front.pop(0)
				data[y][x][z]=1
				nx,ny=dirs[z]
				nz=dirs
				endpointFree=True
				#print('counter',counter,'dirs[z][d-1]',dirs[z][d-1])
				for nx,ny,nz,nd in nbrs[dirs[z][d-1]]:
					#print('nx,ny,nz,nd',nx,ny,nz,nd)
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

			#generate
			cgi.createLayer('maze',(0,255,0))
			for y in range(len(data)-1):
				for x in range(len(data[y])-1):
					for z in [1,2]:
						d=data[y][x][z]
						xn,yn=dirs[z]
						dn=data[y+yn][x+xn][opos[z]]
						#if x+xn>=0 and x+xn<m and y+yn>=0 and y+yn<n:
						strx = 'y='+str(y)
						strx+=' x='+str(x)
						strx+=' z='+str(z)
						strx+=' d='+str(d)
						strx+=' nbrY='+str(y+yn)
						strx+=' nbrX='+str(x+xn)
						strx+=' nbrZ='+str(opos[z])
						strx+=' nbrD='+str(dn)
						print(strx)
						if z==1:
							if d==1 and dn==0:
								cgi.addEntity('line',[[x*10,y*10],[x*10+8,y*10]])
							elif d==1 and dn==1:
								cgi.addEntity('line',[[x*10,y*10],[x*10+10,y*10]])
							elif d==0 and dn==1:
								cgi.addEntity('line',[[x*10+2,y*10],[x*10+10,y*10]])
						if z==2:
							if d==1 and dn==0:
								cgi.addEntity('line',[[x*10,y*10],[x*10,y*10+8]])
							elif d==1 and dn==1:
								cgi.addEntity('line',[[x*10,y*10],[x*10,y*10+10]])
							elif d==0 and dn==1:
								cgi.addEntity('line',[[x*10,y*10+2],[x*10,y*10+10]])
			cgi.createLayer('ends',(255,0,0))
			for y in range(m+1):
				for x in range(n+1):
					cgi.addEntity('circle',[[x*10,y*10],1])
			return True
		else:
			return False

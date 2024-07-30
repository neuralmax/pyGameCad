elif cmd=='extender':
		if scp=='evt':
			newlines=[]
			for pa,pb in cgi.data['line']:
				ax,ay=pa
				bx,by=pb
				pc=[bx+(ax-bx)/2,by+(ay-by)/2]#midpoints
				#move lines center to center of coordinate System
				pa=[ax-pc[0],ay-pc[1]]
				pb=[bx-pc[0],by-pc[1]]
				#scale line
				scl=1.1
				pa=[pa[0]*scl,pa[1]*scl]
				pb=[pb[0]*scl,pb[1]*scl]
				#move line back to its center
				pa=[pa[0]+pc[0],pa[1]+pc[1]]
				pb=[pb[0]+pc[0],pb[1]+pc[1]]

				#pd=[pc[0]+10000,pc[1]]
				#newlines.append([pc,pd])#test lines for midpoints
				newlines.append([pa,pb])
			for line in newlines:
				#cgi.data['lines'].append(line)#test lines for midpoints
				#cgi.selection['lines'].append(0)#test lines for midpoints
				cgi.data['line']=newlines[:]

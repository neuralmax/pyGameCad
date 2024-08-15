# --- data tyoe description ---
# font data is dict, adressed as chars and contains arrays with character caracter data
# caracter data is arrays containing stroke data stored in arrays
# stroke data is composed of points stored in arrays
# if stroke has 2 points it is a line if 3 it is besier curve
# if first member of point data is 0 it is free and folofing member is 2d coordinates of the point stored in array
# if first member of point data is not 0 it indicates index of curve or line it is attached to and folowing member is a place it is attached to ranging from 0 to 1 (float)
# index of strokes starts from 1 because 0 indicates it is not attached


fontdata={
' ':[
	],
'':[
	],
'[':[#[]
		[[0,[0,0]],[0,[0,100]],[0,[100,100]]],
		[[1,0],[0,[100,0]]],
		[[2,1],[1,1]],
		[[1,0],[0,[0,100]]],
	],
'a':[#A
		[[0,[0,100]],[0,[0,0]],[0,[100,0]]],
		[[1,1],[0,[100,100]]],
		[[1,1],[0,[30,0]]],
		[[2,.7],[0,[50,50]],[1,0]]
	],
'b':[#B
		[[0,[0,100]],[0,[50,100]]],
		[[1,1],[0,[170,100]],[0,[0,0]]],
		[[1,0],[2,1]],
		[[2,1],[0,[130,0]],[2,0.7]],
	],
'c':[#C
		[[0,[70,100]],[0,[0,100]],[0,[0,70]]],
		[[0,[0,70]],[0,[0,0]],[0,[100,0]]],
	],
'd':[#D
		[[0,[0,0]],[0,[50,0]]],
		[[1,1],[0,[100,0]],[0,[100,30]]],
		[[2,1],[0,[100,70]],[0,[0,100]]],
		[[3,1],[1,0]],
		#[[2,1],[0,[130,100]],[2,0.7]],
	],
'e':[#E
		[[0,[0,100]],[0,[100,100]]],
		[[1,0],[0,[0,0]],[0,[100,0]]],
		[[2,1],[0,[100,10]]],
		[[2,.2],[0,[70,64]]],
		#[[0,[40,120]],[0,[60,120]]],
	],
'f':[#F
		[[0,[0,100]],[0,[0,0]],[0,[100,0]]],
		[[1,.293],[0,[70,50]]],

	],
'g':[#G
		[[0,[100,0]],[0,[0,0]],[0,[0,30]]],
		[[1,1],[0,[0,100]],[0,[100,100]]],
		[[2,1],[0,[100,30]]],
		[[3,1],[0,[70,30]]],
	],
'h':[#H
		[[0,[0,0]],[0,[0,100]]],
		[[1,1],[0,[0,20]],[0,[70,20]]],
		[[2,1],[0,[100,20]],[0,[100,50]]],
		[[3,1],[0,[100,100]],[0,[70,100]]],
		[[4,1],[0,[100,100]]]
	],
'i':[
		[[0,[0,0]],[0,[100,0]]],
		[[0,[0,100]],[0,[100,100]]],
		[[1,.5],[2,.5]],
	],
'j':[
		[[0,[0,0]],[0,[100,0]]],
		[[1,0],[0,[0,10]]],
		[[1,1],[0,[100,100]],[0,[0,100]]],
	],
'k':[
		[[0,[0,100]],[0,[0,0]]],
		#[[1,1],[0,[100,0]]],
		[[0,[100,0]],[0,[100,80]],[1,.2]],
		[[2,.6],[0,[100,100]]]
	],
'l':[#L
		[[0,[0,100]],[0,[0,0]]],
		[[1,.1],[0,[50,100]],[0,[100,100]]],
		[[2,1],[0,[100,90]]],
	],
'm':[#M
		[[0,[10,100]],[0,[-11,50]],[0,[10,0]]],
		[[0,[90,100]],[0,[111,50]],[0,[90,0]]],
		[[1,1],[0,[50,30]]],
		[[3,1],[2,1]]
	],
'n':[#N
		[[0,[10,100]],[0,[-11,50]],[0,[10,0]]],
		[[0,[90,100]],[0,[111,50]],[0,[90,0]]],
		[[1,1],[2,0]],
	],
'o':[
	[[0,[50,0]],[0,[100,0]],[0,[100,60]]],
	[[1,1],[0,[100,100]],[0,[50,100]]],
	[[2,1],[0,[0,100]],[0,[0,60]]],
	[[3,1],[0,[0,0]],[1,0]],
],
'p':[
		[[0,[0,100]],[0,[0,0]]],
		[[1,1],[0,[100,0]]],
		[[2,1],[0,[100,80]],[1,.2]],
	],
'q':[
	[[0,[50,0]],[0,[100,0]],[0,[100,60]]],
	[[1,1],[0,[100,100]],[0,[50,100]]],
	[[2,1],[0,[0,100]],[0,[0,60]]],
	[[3,1],[0,[0,0]],[1,0]],
	[[0,[70,70]],[0,[100,70]],[0,[100,100]]]
],
'r':[#R
		[[0,[0,100]],[0,[0,0]]],
		[[1,1],[0,[100,0]]],
		[[2,1],[0,[100,80]],[1,.2]],
		[[3,.6],[0,[100,100]]]
	],
's':[#S
	[[0,[100,100]],[0,[50,100]]],
	[[1,1],[0,[0,100]],[0,[0,50]]],
	[[2,1],[0,[0,30]],[0,[50,30]]],
	[[3,1],[0,[40,30]],[0,[100,30]]],
	[[4,1],[0,[100,0]],[0,[50,0]]]
	],
't':[
		[[0,[0,0]],[0,[100,0]]],
		[[1,.4],[0,[0,100]],[0,[100,100]]],
	],
'u':[
		[[0,[30,0]],[0,[0,100]],[0,[50,100]]],
		[[1,1],[0,[100,70]],[0,[100,80]]],
		[[2,1],[0,[100,0]]]
	],
'v':[
		[[0,[0,0]],[0,[0,50]],[0,[50,100]]],
		[[1,1],[0,[100,50]],[0,[100,20]]],
		[[2,1],[0,[100,0]],[0,[80,0]]]
	],
'w':[
		[[0,[0,0]],[0,[0,50]],[0,[30,100]]],
		[[0,[20,0]],[0,[20,50]],[0,[70,100]]],
		[[2,1],[0,[100,50]],[0,[100,20]]],
		[[3,1],[0,[100,0]],[0,[80,0]]],
		[[1,1],[2,.75]],
	],
'x':[
		[[0,[0,0]],[0,[100,50]],[0,[100,100]]],
		[[0,[100,0]],[0,[0,50]],[0,[0,100]]],
	],
'y':[
		[[0,[100,0]],[0,[100,100]],[0,[0,100]]],
		[[1,.5],[0,[0,50]],[0,[0,0]]],
	],
'z':[
		[[0,[0,0]],[0,[100,0]]],
		[[1,1],[0,[0,20]],[0,[0,100]]],
		[[2,1],[0,[100,100]]]
	],
'1':[#1
		[[0,[0,80]],[0,[0,0]],[0,[50,0]]],
		[[1,1],[0,[100,0]]],
		[[1,1],[0,[50,100]]],
		[[0,[0,100]],[0,[100,100]]]
	],
'2':[#2
		[[0,[50,0]],[0,[80,0]]],
		[[1,1],[0,[100,0]],[0,[100,20]]],
		[[2,1],[0,[100,40]],[0,[70,40]]],
		[[3,1],[0,[0,40]],[0,[0,100]]],
		[[4,.9],[0,[50,100]],[0,[100,100]]],
		[[5,1],[0,[100,90]]]
	],
'3':[
		[[0,[0,0]],[0,[100,0]]],
		[[1,1],[0,[0,10]],[0,[0,40]]],
		[[2,1],[0,[100,40]]],
		[[3,1],[0,[100,100]],[0,[0,100]]],

	],
'4':[
		[[0,[80,0]],[0,[80,100]]],
		[[0,[0,80]],[0,[100,80]]],
		[[2,0],[0,[0,0]],[1,0]],
	],
'5':[
		[[0,[100,0]],[0,[20,0]]],
		[[1,1],[0,[0,0]],[0,[0,20]]],
		[[2,1],[0,[0,40]],[0,[30,40]]],
		[[3,1],[0,[100,40]]],
		[[4,1],[0,[100,100]],[0,[0,100]]],
	],
'6':[
		[[0,[100,0]],[0,[0,0]],[0,[0,70]]],
		[[1,1],[0,[0,100]],[0,[50,100]]],
		[[2,1],[0,[100,100]],[0,[100,70]]],
		[[3,1],[0,[100,40]],[1,.7]],
	],
'7':[#7
		[[0,[0,0]],[0,[80,0]]],
		[[1,1],[0,[100,0]],[0,[100,20]]],
		[[2,1],[0,[100,40]],[0,[30,100]]],
		[[3,0.5],[0,[50,40]],[0,[0,40]]],
	],
'8_':[
		[[0,[50,0]],[0,[60,0]],[0,[60,10]]],
		[[1,1],[0,[60,20]],[0,[50,20]]],
		[[2,1],[0,[40,20]],[0,[40,10]]],
		[[3,1],[0,[40,0]],[1,0]],

		[[0,[50,20]],[0,[100,20]],[0,[100,80]]],
		[[5,1],[0,[100,100]],[0,[50,100]]],
		[[6,1],[0,[0,100]],[0,[0,80]]],
		[[7,1],[0,[0,20]],[5,0]],
],
'8':[
		[[0,[50,0]],[0,[70,0]],[0,[70,20]]],
		[[1,1],[0,[70,40]],[0,[50,40]]],
		[[2,1],[0,[30,40]],[0,[30,20]]],
		[[3,1],[0,[30,0]],[1,0]],

		[[0,[50,40]],[0,[100,40]],[0,[100,80]]],
		[[5,1],[0,[100,100]],[0,[50,100]]],
		[[6,1],[0,[0,100]],[0,[0,80]]],
		[[7,1],[0,[0,40]],[5,0]],
],
'9':[
		[[0,[0,100]],[0,[100,100]],[0,[100,30]]],
		[[1,1],[0,[100,0]],[0,[50,0]]],
		[[2,1],[0,[0,0]],[0,[0,30]]],
		[[3,1],[0,[0,60]],[1,.7]],
	],
'0':[
		[[0,[50,0]],[0,[100,0]],[0,[100,60]]],
		[[1,1],[0,[100,100]],[0,[50,100]]],
		[[2,1],[0,[0,100]],[0,[0,60]]],
		[[3,1],[0,[0,0]],[1,0]],
		[[0,[0,100]],[0,[100,0]]]
],
'!':[
		[[0,[50,0]],[0,[30,0]],[0,[50,70]]],
		[[0,[50,80]],[0,[30,100]],[0,[50,100]]],
		[[0,[50,80]],[0,[70,100]],[0,[50,100]]],
],
'@':[
		[[0,[50,80]],[0,[80,80]],[0,[80,60]]],
		[[1,1],[0,[80,20]],[0,[50,20]]],
		[[2,1],[0,[20,20]],[0,[20,60]]],
		[[3,1],[0,[20,80]],[0,[50,80]]],

		[[4,1],[0,[100,80]],[0,[100,60]]],
		[[5,1],[0,[100,0]],[0,[50,0]]],
		[[6,1],[0,[0,0]],[0,[0,60]]],
		[[7,1],[0,[0,100]],[0,[50,100]]],
		[[8,1],[0,[80,100]],[0,[90,95]]],
],
'$':[#S
	[[0,[100,90]],[0,[50,90]]],
	[[1,1],[0,[0,90]],[0,[0,50]]],
	[[2,1],[0,[0,30]],[0,[50,30]]],
	[[3,1],[0,[40,30]],[0,[100,30]]],
	[[4,1],[0,[100,10]],[0,[40,10]]],

	[[0,[50,0]],[0,[50,100]]],
	],

'%':[#S
	[[0,[100,0]],[0,[0,100]]],

	[[0,[10,10]],[0,[20,0]],[0,[50,0]]],
	[[2,1],[0,[80,0]],[0,[45,45]]],
	[[3,1],[0,[0,80]],[0,[0,50]]],
	[[4,1],[0,[0,20]],[2,0]],

	[[0,[90,90]],[0,[80,100]],[0,[50,100]]],
	[[6,1],[0,[20,100]],[0,[55,55]]],
	[[7,1],[0,[100,20]],[0,[100,50]]],
	[[8,1],[0,[100,80]],[6,0]],
	],
'&':[#top
	[[0,[50,0]],[0,[70,0]],[0,[70,20]]],
	[[1,1],[0,[70,40]],[0,[50,40]]],
	[[2,1],[0,[30,40]],[0,[30,20]]],
	[[3,1],[0,[30,0]],[1,0]],
	#bottom
	[[0,[50,40]],[0,[80,40]],[0,[80,80]]],
	[[5,1],[0,[80,100]],[0,[50,100]]],
	[[6,1],[0,[0,100]],[0,[0,80]]],
	[[7,1],[0,[0,40]],[5,0]],
	#ribbon
	[[5,1],[0,[80,60]],[0,[100,60]]],
	[[5,1],[0,[80,100]],[0,[100,100]]],
],
"'":[#S
	[[0,[50,0]],[0,[50,20]]],
],
'||':[#S
	[[0,[40,0]],[0,[40,20]]],
	[[0,[60,0]],[0,[60,20]]],
],
'(':[
	[[0,[50,0]],[0,[20,50]],[0,[50,100]]],
],
')':[
	[[0,[50,0]],[0,[80,50]],[0,[50,100]]],
],
'[':[#top
	[[0,[80,0]],[0,[50,0]],[0,[50,10]]],
	[[0,[80,100]],[0,[50,100]],[0,[50,90]]],
	[[1,1],[2,1]],
],
']':[#top
	[[0,[20,0]],[0,[50,0]],[0,[50,10]]],
	[[0,[20,100]],[0,[50,100]],[0,[50,90]]],
	[[1,1],[2,1]],
],
'{':[#top
	[[0,[80,0]],[0,[50,0]],[0,[50,10]]],
	[[0,[20,50]],[0,[50,50]],[0,[50,10]]],
	[[0,[20,50]],[0,[50,50]],[0,[50,90]]],
	[[0,[80,100]],[0,[50,100]],[0,[50,90]]],
],
'}':[#top
	[[0,[20,0]],[0,[50,0]],[0,[50,10]]],
	[[0,[80,50]],[0,[50,50]],[0,[50,10]]],
	[[0,[80,50]],[0,[50,50]],[0,[50,90]]],
	[[0,[20,100]],[0,[50,100]],[0,[50,90]]],
],
'\\':[#top
	[[0,[0,0]],[0,[100,100]]],
],
'/':[#top
	[[0,[0,100]],[0,[100,0]]],
],
'|':[#top
	[[0,[50,0]],[0,[50,100]]],
],
'-':[#top
	[[0,[0,50]],[0,[100,50]]],
],
'+':[#top
	[[0,[0,50]],[0,[100,50]]],
	[[0,[50,0]],[0,[50,100]]],
],
'=':[#top
	[[0,[0,40]],[0,[100,40]]],
	[[0,[0,60]],[0,[100,60]]],
],
'_':[#top
	[[0,[0,100]],[0,[100,100]]],
],
'<':[#top
	[[0,[25,50]],[0,[75,0]]],
	[[0,[25,50]],[0,[75,100]]],
],
'>':[#top
	[[0,[75,50]],[0,[25,0]]],
	[[0,[75,50]],[0,[25,100]]],
],
'^':[#top
	[[0,[0,50]],[0,[50,0]]],
	[[0,[50,0]],[0,[100,50]]],
],
'#':[#top
	[[0,[0,20]],[0,[100,20]]],
	[[0,[0,80]],[0,[100,80]]],
	[[0,[20,0]],[0,[20,100]]],
	[[0,[80,0]],[0,[80,100]]],
],
'*':[#top
	[[0,[50,0]],[0,[50,100]]],
	[[0,[5,25]],[0,[95,75]]],
	[[0,[5,75]],[0,[95,25]]],
],
'?':[
		[[0,[0,40]],[0,[0,0]],[0,[40,0]]],
		[[1,1],[0,[100,0]],[0,[100,40]]],
		[[2,1],[0,[100,60]],[0,[70,60]]],
		[[3,1],[0,[50,60]],[0,[50,70]]],
		#dot
		[[0,[50,80]],[0,[30,100]],[0,[50,100]]],
		[[0,[50,80]],[0,[70,100]],[0,[50,100]]],
],
'~':[
		[[0,[0,50]],[0,[25,25]],[0,[50,50]]],
		[[1,1],[0,[75,75]],[0,[100,50]]],
],
'.':[
		[[0,[49,100]],[0,[51,100]]],
],
',':[
		[[0,[40,100]],[0,[50,90]]],
],
':':[
		[[0,[49,30]],[0,[51,30]]],
		[[0,[49,70]],[0,[51,70]]],
],
';':[
		[[0,[49,30]],[0,[51,30]]],
		[[0,[40,80]],[0,[50,70]]],
],
'<=':[
	[[0,[25,50]],[0,[75,0]]],
	[[0,[25,50]],[0,[75,100]]],
	[[0,[45,50]],[0,[75,80]]],
],
'>=':[
	[[0,[75,50]],[0,[25,0]]],
	[[0,[75,50]],[0,[25,100]]],
	[[0,[55,50]],[0,[25,80]]],
],
'<>':[
	[[0,[0,50]],[0,[50,0]]],
	[[1,1],[0,[100,50]]],
	[[2,1],[0,[50,100]]],
	[[3,1],[1,0]],
],
'$$':[#$$(pound)
	[[0,[0,100]],[0,[0,0]],[0,[100,0]]],
	[[1,0],[0,[100,100]]],
	[[0,[0,50]],[0,[50,50]]],
],
'^|':[#arrow
	[[0,[50,0]],[0,[50,100]]],
	[[1,0],[0,[50,50]],[0,[0,50]]],
	[[1,0],[0,[50,50]],[0,[100,50]]],
],
'v|':[#arrow
	[[0,[50,100]],[0,[50,0]]],
	[[1,0],[0,[50,50]],[0,[0,50]]],
	[[1,0],[0,[50,50]],[0,[100,50]]],
],
'<|':[#arrow
	[[0,[0,50]],[0,[100,50]]],
	[[1,0],[0,[50,50]],[0,[50,0]]],
	[[1,0],[0,[50,50]],[0,[50,100]]],
],
'>|':[#arrow
	[[0,[100,50]],[0,[0,50]]],
	[[1,0],[0,[50,50]],[0,[50,0]]],
	[[1,0],[0,[50,50]],[0,[50,100]]],
],
'cc':[#c
	[[0,[50,70]],[0,[30,70]],[0,[30,50]]],
	[[0,[30,50]],[0,[30,30]],[0,[70,30]]],
	#o
	[[0,[50,0]],[0,[100,0]],[0,[100,60]]],
	[[3,1],[0,[100,100]],[0,[50,100]]],
	[[4,1],[0,[0,100]],[0,[0,60]]],
	[[5,1],[0,[0,0]],[3,0]],

],
}

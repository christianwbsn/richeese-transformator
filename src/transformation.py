from math import cos, sin, pi, radians
from time import sleep
import copy

def translate(vert,NbVert,dx,dy): #procedure untuk melakukan translasi terhadap vertices sebesar dx dan dy
    for frame in range(400):
        for i in range(0,int(NbVert)):
            vert[i][0]+=float(dx)/400
            vert[i][1]+=float(dy)/400
            sleep(0.001)

def dilate(vert,NbVert,k): #melakukan dilatasi terhadap vertices dengan faktor dilatasi k
	temp = 1.0
	mat=copy.deepcopy(vert)
	rentang = (float(k)-1)/400
	for frame in range(400):
		temp+=rentang
		for i in range(0,int(NbVert)):
			vert[i][0]=mat[i][0]*temp
			vert[i][1]=mat[i][1]*temp
			sleep(0.001)

def rotate(vert,NbVert,deg,a,b): #melakukan rotasi terhadap vertices sebesar degree pada titik (a,b)
	temp=copy.deepcopy(vert)
	derajattemp = radians(float(deg))
	rentang = derajattemp/400
	degree = 0
	for frame in range(400):
		degree += rentang
		for i in range(0,int(NbVert)):
			vert[i][0] = float(a) + (float(temp[i][0])-float(a)) * cos(degree) - (float(temp[i][1])-float(b)) * sin(degree)
			vert[i][1] = float(b) + (float(temp[i][0])-float(a)) * sin(degree) + (float(temp[i][1])-float(b)) * cos(degree)
			sleep(0.001)

def shear(vert,NbVert,axis,k): #melakukan shear terhadap x atau y dengan faktor shear sebesar k

	if(axis=='x'):
		for frame in range(400):
			for i in range(0,int(NbVert)):
				vert[i][0]+=(float(k)*vert[i][1])/400
				sleep(0.001)
	elif(axis=='y'):
		for frame in range(400):
			for i in range(0,int(NbVert)):
				vert[i][1]+=(float(k)*vert[i][0])/400
				sleep(0.001)

def stretch(vert,NbVert,axis,k): #melakukan stretch terhadap x atau y dengan faktor stretch sebesar k
	temp = 1.0
	mat=copy.deepcopy(vert)
	rentang = (float(k)-1)/400
	if(axis=='x'):
		for frame in range(400):
			temp+=rentang
			for i in range(0,int(NbVert)):
				vert[i][0]=mat[i][0]*temp
				sleep(0.001)
	elif(axis=='y'):
		for frame in range(400):
			temp+=rentang
			for i in range(0,int(NbVert)):
				vert[i][1]=mat[i][1]*temp
				sleep(0.001)

def reflect(vert,NbVert,params): #melakukan refleksi terhadap parameter yang sudah disediakan atau terhadap titik (a,b)
	mat=copy.deepcopy(vert)
	if (params=="y"):
		for i in range(0,int(NbVert)):
			mat[i][0]*=-1.00
	elif(params=="x"):
		for i in range(0,int(NbVert)):
			mat[i][1]*=-1.00
	elif(params=="y=x")or(params=="x=y"):
		for i in range(0,int(NbVert)):
			temp=mat[i][0]
			mat[i][0]=mat[i][1]
			mat[i][1]=temp
	elif(params=="y=-x")or(params=="x=-y"):
		for i in range(0,int(NbVert)):
			temp=mat[i][0]
			mat[i][0]=-mat[i][1]
			mat[i][1]=-temp    
	else:
		temp = vert
		newparams = params.replace('(','').replace(')','').split(',')
		for i in range(0,int(NbVert)):
			mat[i][0] = 2*int(newparams[0]) - temp[i][0]
			mat[i][1] = 2*int(newparams[1]) - temp[i][1]
	dx = []
	dy = []
	for i in range(0,int(NbVert)):
		xx = mat[i][0]-vert[i][0]
		yy = mat[i][1]-vert[i][1]
		dx.append(xx)
		dy.append(yy)
	for frame in range(400):
		for i in range(0,int(NbVert)):
			vert[i][0]+=float(dx[i])/400
			vert[i][1]+=float(dy[i])/400
			sleep(0.001)

		
def custom(vert,NbVert,matrix): #melakukan transformasi dengan matrix 2x2 yang nilainya ditentukan user
	temp=copy.deepcopy(vert)
	mat=copy.deepcopy(vert)
	for i in range(0,int(NbVert)):
		mat[i][0]=matrix[0][0]*temp[i][0]+matrix[0][1]*temp[i][1]
		mat[i][1]=matrix[1][0]*temp[i][0]+matrix[1][1]*temp[i][1]
	dx = []
	dy = []
	for i in range(0,int(NbVert)):
		xx = mat[i][0]-vert[i][0]
		yy = mat[i][1]-vert[i][1]
		dx.append(xx)
		dy.append(yy)
	for frame in range(400):
		for i in range(0,int(NbVert)):
			vert[i][0]+=float(dx[i])/400
			vert[i][1]+=float(dy[i])/400
			sleep(0.001)

        
        
        
 

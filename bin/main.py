from __future__ import print_function
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi,sin,cos
import thread
from time import sleep
import copy
import transformation

quited = False
NbVertex = 0
Vertices = []
initVertices=[]

def init_draw2d():
    glPushMatrix() #setup for drawing
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(-600,600,-500,500)
    glDepthFunc(GL_ALWAYS)

def drawPolygon(list_point):
	global NbVertex
	glEnable (GL_BLEND)
	glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glColor4f(0, 0.482 ,0.655,0.7)
	glEnableClientState(GL_VERTEX_ARRAY)
	glVertexPointer(3, GL_FLOAT, 0,list_point)
	glDrawArrays(GL_POLYGON, 0, int(NbVertex))
	glColor4f(0, 0.0 ,0.0, 0.8)
	glDrawArrays(GL_LINE_LOOP, 0, int(NbVertex))
	glDisableClientState(GL_VERTEX_ARRAY)

def uninit_draw2d():
	glDepthFunc(GL_LESS)
	glPopMatrix()
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()

def print_text(str, x, y, r, g, b):
	glColor3f(r,g,b) #set text color
	glRasterPos2f(x,y)
	for i in str:
		glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(i))

def draw_axis():
	glLineWidth(1.5); 
	glColor3f(0, 0, 0)
	glBegin(GL_LINES)
	glVertex3f(-600,0,0) #draw horizontal lines of x
	glVertex3f(600,0,0)
	glEnd()
	glBegin(GL_LINES)
	glVertex3f(0,-600,0) #draw vertical lines of y
	glVertex3f(0,600,0)
	glEnd()
	glBegin(GL_LINES)
	glVertex3f(0,0,-600)
	glVertex3f(0,0,600)
	glEnd()

def init_gl():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(1000, 800)	            #init windows size       
	glutInitWindowPosition(200,0)               #init windows position
	glutCreateWindow("Richeese Transformator")	#add windows title            
	glutDisplayFunc(draw)                       #set displayfunction
	glutIdleFunc(draw)                                   
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glShadeModel(GL_SMOOTH)

def draw_grid():
	glLineWidth(0.25); #set line width
	glColor3f(0.90, 0.90, 0.90)
	glBegin(GL_LINES)
	for i in range(-600,600,20): #draw small grid
		glVertex3f(float(i), -600.0, 0.0)
		glVertex3f(float(i), 600.0, 0.0)
		glVertex3f(-600.0, float(i), 0.0)
		glVertex3f(600.0, float(i), 0.0)
	glEnd()
	glLineWidth(0.5); 
	glColor3f(0.65, 0.65, 0.65)
	glBegin(GL_LINES)
	for i in range(-600,600,100): #draw main grid
		glVertex3f(float(i), -600.0, 0.0)
		glVertex3f(float(i), 600.0, 0.0)
		glVertex3f(-600.0, float(i), 0.0)
		glVertex3f(600.0, float(i), 0.0)
	glEnd()

	for i in range(-500,600,100): # print scale
		if(i==0):
			print_text(str(i),float(i)+5,-20, 0, 0, 0)
		elif(i==500):
			print_text(str(i), float(i)-10,5, 0, 0, 0)
		else:
			print_text(str(i), float(i)-10,5, 0, 0, 0)
			print_text(str(i), 5,float(i)-10, 0, 0, 0)

def draw():
	global quited, triangleVertices, Vertices
	if(quited):
		sys.exit(0)
	glClearColor(1.0,1.0,1.0,0.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glViewport(0, 0, 1000, 800) #set viewport
	init_draw2d()
	draw_grid()
	draw_axis()
	drawPolygon(Vertices)
	print_text('X', 580,10, 0, 0, 0)
	print_text('Y', 10,480, 0, 0, 0)
	uninit_draw2d()
	glutSwapBuffers()

def terminal_display():
	print ("  _______    _____   ______  ____  ____  ________  ________   ______   ________ ")
	print (" |_  ___ \  |_   _|.' ___  ||_   ||   _||_   __  ||_   __  |.' ____ \ |_   __  |")
	print ("  | |__) |    | | / .'   \_|  | |__| |    | |_ \_|  | |_ \_|| (___ \_|  | |_ \_|")
	print ("  |  __ /     | | | |         |  __  |    |  _| _   |  _| _  '.____`.   |  _| _ ")
	print (" _| |  \ \_  _| |_\ `.___.'\ _| |  | |_  _| |__/ | _| |__/ || \____) | _| |__/ |")
	print ("|____| |___||_____|`.____ .'|____||____||________||________| \______.'|________|")
	print (" _+_+_+_+_+_+_+_+_+_+_+_+_+_ LINEAR TRANSFORMATION _+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
	print ("============================ERIC JONATHAN-13516117==============================")
	print ("==========================CHRISTIAN WIBISONO-13516147===========================")

def shape_input():
	global NbVertex
	NbVertex = raw_input('> Insert number of points : ')
	P = []
	global Vertices, initVertices
	for i in range (int(NbVertex)): #accept input for point
		x = float(raw_input("> X"+str((i+1))+" : "))
		y = float(raw_input("> Y"+str((i+1))+" : "))
		z = float(0)
		del P[:]
		P.append(x)
		P.append(y)
		P.append(z)
		print("> Point-{0} : < {1} , {2} >".format(int(i+1),P[0],P[1]))
		Vertices.append(list(P))
		initVertices.append(list(P))	

def command_input():
	global NbVertex, Vertices, initVertices
	initVertices= copy.deepcopy(Vertices)
	while(True):
		temp = raw_input('> Insert command : ')
		command = temp.split(' ')
		#memanggil perintah transformasi yang sesuai dengan input
		if (command[0] == 'translate'):
			transformation.translate(Vertices,NbVertex,command[1],command[2])
		elif (command[0] == 'rotate'):
			transformation.rotate(Vertices,NbVertex,command[1],command[2],command[3])
		elif (command[0] == 'reflect'):
			transformation.reflect(Vertices,NbVertex,command[1])
		elif (command[0] == 'dilate'):
			transformation.dilate(Vertices,NbVertex,command[1])
		elif (command[0] == 'stretch'):
			transformation.stretch(Vertices,NbVertex,command[1],command[2])	
		elif (command[0] == 'shear'):
			transformation.shear(Vertices,NbVertex,command[1],command[2])
		elif (command[0] == 'custom'):	
			TransMatrix=[]
			k=[]
			k.append(float(command[1]))
			k.append(float(command[2]))
			TransMatrix.append(list(k))
			del k[:]
			k.append(float(command[3]))
			k.append(float(command[4]))
			TransMatrix.append(list(k))
			transformation.custom(Vertices,NbVertex,TransMatrix)
		elif (command[0] == 'multiple'):
			multi = []
			for i in range(0,int(command[1])):
				text = raw_input('> ')
				multi.append(text)
			for j in range(0,int(command[1])):
				perintah = multi[j].split(' ')
				if (perintah[0] == 'translate'):
					transformation.translate(Vertices,NbVertex,perintah[1],perintah[2])
				elif (perintah[0] == 'rotate'):
					transformation.rotate(Vertices,NbVertex,perintah[1],perintah[2],perintah[3])
				elif (perintah[0] == 'reflect'):
					transformation.reflect(Vertices,NbVertex,perintah[1])
		
				elif (perintah[0] == 'dilate'):
					transformation.dilate(Vertices,NbVertex,perintah[1])
				elif (perintah[0] == 'stretch'):
					transformation.stretch(Vertices,NbVertex,perintah[1],perintah[2])	
				elif (perintah[0] == 'shear'):
					transformation.shear(Vertices,NbVertex,perintah[1],perintah[2])
				elif (perintah[0] == 'custom'):	
					TransMatrix=[]
					k=[]
					k.append(float(perintah[1]))
					k.append(float(perintah[2]))
					TransMatrix.append(list(k))
					del k[:]
					k.append(float(perintah[3]))
					k.append(float(perintah[4]))
					TransMatrix.append(list(k))
					transformation.custom(Vertices,NbVertex,TransMatrix)
				del perintah[:]
		elif (command[0] == 'reset'):
				dx = []
				dy = []
				for i in range(0,int(NbVertex)):
					xx = initVertices[i][0]-Vertices[i][0]
					yy = initVertices[i][1]-Vertices[i][1]
					dx.append(xx)
					dy.append(yy)
				for frame in range(400):
					for i in range(0,int(NbVertex)):
						Vertices[i][0]+=float(dx[i])/400
						Vertices[i][1]+=float(dy[i])/400
						sleep(0.001)
		elif (command[0] == 'help'):
			print("> Here's some command that can be used")
			print("> translate <dx> <dy> : translate x by dx and y by dy")
			print("> dilate <k> : dilate by k")
			print("> rotate <deg> <a> <b>: rotate by deg")
			print("> reflect <param>: reflect with param")
			print("> shear <param> <k>: shear with param")
			print("> stretch <param> <k>: stretch with param")
			print("> custom <a> <b> <c> <d>: custom transformation")
			print("> multiple <n>: multiple transformation")
			print("> reset: reset everything")
			print("> exit: exit from program")
		elif (command[0] == 'exit'):
			global quited
			quited = True
			print("> Goodbye !")
			sys.exit(0)
		else:
			print("> Type 'help' to see valid command")

terminal_display()							#menampilkan tampilan awal
shape_input() 								#perintah untuk memasukan titik yang akan menjadi bentuk tertentu
thread.start_new_thread(command_input, () )	#perintah untuk memasukan command transformasi
init_gl()									#perintah untuk memunculkan window yang menampilkan bentuk dan hasil transformasi
glutMainLoop()


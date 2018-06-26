Richeese Transformator
=======================
## Description
This repository is a task for IF2123 Algebraic Geometry, Department of Informatics, School of Electrical Engineering and Informatics, Bandung Institute of Technology. Program in CLI-form to calculate and visualize 2D plane linear transformation. Built using Python 2.7 and OpenGL Library (GL,GLU,GLUT). Linear transformation that can be visualized including translation, rotation, reflection, dilation, shear, stretch, and custom transformation matrix.


	  _______    _____   ______  ____  ____  ________  ________   ______   ________ 
	 |_  ___ \  |_   _|.' ___  ||_   ||   _||_   __  ||_   __  |.' ____ \ |_   __  |
	  | |__) |    | | / .'   \_|  | |__| |    | |_ \_|  | |_ \_|| (___ \_|  | |_ \_|
	  |  __ /     | | | |         |  __  |    |  _| _   |  _| _  '.____`.   |  _| _ 
	 _| |  \ \_  _| |_\ `.___.'\ _| |  | |_  _| |__/ | _| |__/ || \____) | _| |__/ |
	|____| |___||_____|`.____ .'|____||____||________||________| \______.'|________|
	 _+_+_+_+_+_+_+_+_+_+_+_+_+_ LINEAR TRANSFORMATION _+_+_+_+_+_+_+_+_+_+_+_+_+_+_
	============================ERIC JONATHAN-13516117==============================
	==========================CHRISTIAN WIBISONO-13516147===========================

			   Copyright Eric Jonathan & Christian Wibisono
## Requirements
* Python 2.7
* OpenGL

## Installation
* Download freeglut.dll and put it in your main.py folder

## How to run
`python main.py`

## Usage
1. Input number of point that define your plane
2. After that you will be guided to input each point that will define your plane
3. Finally your plane will be drawn in another windows 

Here's some command that can be used to transform your plane!
```
translate <dx> <dy> : translate x by dx and y by dy
dilate <k> : dilate by k
rotate <deg> <a> <b>: rotate by deg
reflect <param>: reflect with param
shear <param> <k>: shear with param
stretch <param> <k>: stretch with param
custom <a> <b> <c> <d>: custom transformation
multiple <n>: multiple transformation 
reset: reset everything
exit: exit from program
```
valid param value : x, y, y=x, y=-x, or a b.
Notes: for reflect with param value (a,b) you should input
reflect a b

## Author
* [Christian Wibisono](https://github.com/christianwbsn)-13516147
* [Eric Jonathan](https://github.com/ericjonathan6)-13516117

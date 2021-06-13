import pandas as pd
from PIL import ImageTk,Image
import time
import math
import os
import time
import matplotlib.pyplot as plt

from tkinter import *
import os

from matplotlib.widgets import Button
from openpyxl.workbook import *
from openpyxl import load_workbook
from openpyxl import Workbook
from tkinter import colorchooser
from tkinter import ttk

import cv2
import numpy as np
from PIL import ImageTk,Image


root=Tk()
root.state('zoomed')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


my_notebook=ttk.Notebook(root)
my_notebook.pack(pady=0)



frame1=Frame(my_notebook,width=screen_width,height=screen_height)
frame2=Frame(my_notebook,width=screen_width,height=screen_height)


frame1.pack(fill='both',expand=1)
frame2.pack(fill='both',expand=1)

my_notebook.add(frame1,text='new map')
my_notebook.add(frame2,text='load map')


from tkinter import filedialog as fd
filename = fd.askopenfilename()
print(filename)
main_img=PhotoImage(file=filename)
import PIL
img_2 = PIL.Image.open(filename)
width, height = img_2.size
########
selected_color=1

colors=[
	'RED',
	'BLUE',
	'GREEN',
	'YELLOW',
	'CYAN'
]
selected_color_str=StringVar()
selected_color_str.set(colors[1])
menu=OptionMenu(root,selected_color_str,*colors)
menu.place(x=width+30,y=200)
def color_sel(event):
	global selected_color
	selected_color=colors.index(selected_color_str.get())+1
	print(selected_color)


menu.bind('<Leave>',color_sel)












print(height)
fig_title_l=Label(root,text='Figure title')
fig_title_l.place(x=width/2,y=20)
fig_title_e=Entry(root,width=50)
fig_title_e.place(x=width/2,y=50)


incr_l=Label(root,text='increments')
incr_l.place(x=width+10,y=20)
incr_e=Entry(root)
incr_e.place(x=width+30,y=50)




im = Image.open(filename)
rgb_im = im.convert('RGB')


my_canvas=Canvas(frame1,bg='white',width=screen_width,height=screen_height,)
my_canvas.pack(anchor='nw',expand=1)
my_canvas.create_image(width/2,height/2,image=main_img)

my_canvas2=Canvas(frame2,bg='white',width=800,height=1000,)
my_canvas2.pack(anchor='nw',expand=1)


class divisions:
	def __init__(self,div_name,div_val,div_old_rgb):
		self.div_name=div_name
		self.div_val=div_val
		self.div_old_rgb=div_old_rgb




val_arr=[]
name_arr=[]
old_rgb_arr=[]
def show_rgb(event):
	
	global const
	const+=1
	print(const)
	x=round(event.x)
	y=round(event.y)
	val_entry=Entry(frame1,width=3)
	val_entry.place(x=x,y=y)
	val_arr.append(val_entry)
	#name.bind('<Return>',add_names_values)
	rgb=rgb_im. getpixel((x,y))
	old_rgb_arr.append(rgb)
	print(rgb)









def caln(event):
	my_canvas.unbind('<Button-1>')
	div_objects=[]
	array_of_values=[]
	for i in range(len(val_arr)):
		my_div=divisions(i,val_arr[i].get(),old_rgb_arr[i])
		div_objects.append(my_div)
		array_of_values.append(float(val_arr[i].get()))
	
	array_of_values.sort(reverse=True)
	print(array_of_values)


	for i in range(len(val_arr)):
		div_objects[i].rank=array_of_values.index(float(div_objects[i].div_val))



	
	for i in range(len(div_objects)):
		print(f'name = {div_objects[i].div_name}  val = {div_objects[i].div_val}    rgb= {div_objects[i].div_old_rgb}   rank ={div_objects[i].rank}')
	
	################################
	increment=int(incr_e.get())
	rgb_mega=[[]]
	for i in range(0,6):
		if i==0:
			r=250
			g=40
			b=70
			tr=[]
			for j in range(0,len(div_objects)):
				
				tr.append([r,g+j*increment,b+j*increment])
				
			rgb_mega.append(tr)

		if i==1:
			r=37
			g=33
			b=164
			tr=[]
			for j in range(0,len(div_objects)):
				
				tr.append([r+j*increment,g+j*increment,b])
				
			rgb_mega.append(tr)
		if i==2:
			r=40
			g=233
			b=35
			tr=[]
			for j in range(0,len(div_objects)):
				
				tr.append([r+j*increment,g,b+j*increment])
				
			rgb_mega.append(tr)
		if i==3:
			r=240
			g=240
			b=35
			tr=[]
			for j in range(0,len(div_objects)):
				
				tr.append([r,g,b+j*increment])
				
			rgb_mega.append(tr)
		if i==4:
			r=30
			g=192
			b=203
			tr=[]
			for j in range(0,len(div_objects)):
				
				tr.append([r+j*increment,g,b])
				
			rgb_mega.append(tr)

		if i==5:
			r=255
			g=50
			b=16
			tr=[]
			for j in range(0,len(div_objects)):
				
				tr.append([r,g+j*increment,b+j*increment])
				
			rgb_mega.append(tr)
	print(rgb_mega[1])
	
	for i in range(len(div_objects)):
		div_objects[i].new_rgb=rgb_mega[selected_color][div_objects[i].rank]
	
	for i in range(len(div_objects)):
		print(f'name = {div_objects[i].div_name}  val = {div_objects[i].div_val}    rgb= {div_objects[i].div_old_rgb}   rank ={div_objects[i].rank}   new rgb ={div_objects[i].new_rgb}  ')
	
	ph=cv2.imread(filename)
	ph=cv2.cvtColor(ph,cv2.COLOR_BGR2RGB)

	for i in range(0,len(div_objects)):
		ph[np.where((ph==div_objects[i].div_old_rgb).all(axis=2))]=div_objects[i].new_rgb
	ph=cv2.cvtColor(ph,cv2.COLOR_RGB2BGR)
	cv2.imwrite(f'bd_2.png',ph)


	fram2_img=PhotoImage(file='bd_2.png')


	bd_2=PhotoImage(file='bd_2.png')
	i = Image.open('bd_2.png')
		
	iar = np.asarray(i)
	fig=plt.imshow(iar)
	plt.xlabel(f'{fig_title_e.get()}')
	plt.show()

		

		




btn=ttk.Button(frame1,text='generate image')
btn.place(x=width+60,y=60)
btn.bind('<Button-1>',caln)

Label(frame1,text='Names',bg='red').place(x=width+10,y=60)
const=0
my_canvas.bind('<Button-1>',show_rgb)




root.mainloop()
import math

def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y+step*math.sin(angle)
	return nx,ny

x=float(input('X轴位置：'))
y=float(input('y轴位置：'))
step=float(input('步移：'))
angle=float(input('角度：'))

x,y=move(x,y,step,angle)#输入“math.pi / 6”为什么不行啊？

print(x,y)
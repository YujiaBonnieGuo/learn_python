import math

def quadratic(A,B,C = 0):
	a=float(A)
	b=float(B)
	c=float(C)
	if a==0:
		print('该方程不是二次方程')
	else:
		s=b**2-4*a*c
		m=float(s)
		if m<0:
			print('该方程无解')
		else:
			k=math.sqrt(m)
			nx=(-b+k)/2*a
			ny=(-b-k)/2*a
			return nx
			return ny

a=input('二次元系数')
b=input('一次元系数')
c=input('常数系数')
s=quadratic(a,b,c)
print(s)

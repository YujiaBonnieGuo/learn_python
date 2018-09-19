import operator

def triangles():
	b=[1]
	while True:
		yield b 
		c=[0]+b
		d=b+[0]
		b=list(map(operator.add,c,d))

p=triangles()
n=0
while True:
	print(next(p))
	n+=1
	if n>9:
		break
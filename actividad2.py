from multiprocessing import Process, Queue
from sys import argv

def x_op(x,l1):
	for i in range(200000):
		x = x * 5.6800001 / 5.68
	l1.put(x)
	return x

def y_op(y,l2):
	for i in range(100000):
		y = y * 5.6800001 / 5.68
	l2.put(y)
	return y
	
if __name__ == '__main__':
	l1 = Queue()
	l2 = Queue()
	x = 10000000 + int(argv[2])*10000
	y = 10000000 - int(argv[2])*10000
	r = 0
	for j in range(500):
		Process(target=x_op, args=(x, l1,)).start()
		Process(target=y_op, args=(y, l2,)).start()
		x = l1.get()
		y = l2.get()
		r = r + x + y
	print('ACTIVIDAD 2')
	print(r)	
		

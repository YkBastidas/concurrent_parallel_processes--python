from subprocess import Popen, PIPE
from sys import argv

file_numeros = open('./numeros.txt','r')
total = 0
running_procs=[]

def handle_results(total, stdout):
	p2 = Popen(["cat"], stdin=stdout, stdout=PIPE)
	output = p2.communicate()[0]
	return int(output) + total
	
for line in file_numeros.readlines():
  running_procs.append(Popen(["python3", "fuente1.py", argv[1], line], stdout=PIPE))

while running_procs:
	for proc in running_procs:
		retcode = proc.poll()
		if retcode is not None:
			running_procs.remove(proc)
			break
		else:
			continue
	total = handle_results(total, proc.stdout)
print("ACTIVIDAD 1")
print(total)
file_numeros.close()

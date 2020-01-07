from subprocess import Popen, PIPE
from sys import argv

p1 = Popen("bash -c 'time python3 actividad1.py "+argv[1]+"'", shell=True)
p2 = Popen("bash -c 'time python3 actividad2.py "+argv[1]+" "+argv[2]+"'", shell=True) 
p3 = Popen("bash -c 'time python3 actividad3.py'", shell=True)
exit_codes = [p.wait() for p in [p1, p2, p3]]
i=0
while i < 3:
	if exit_codes[i] == 0:
		i+=1
	else:
		print("ERROR EN LA ACTIVIDAD" + str(i+1))
		break
print('TIEMPO TOTAL')

from socket import socket

file_numeros = open('./numeros.txt', 'r')
total = 0
s = socket()
s.connect(('localhost', 9999))
arregloEnviados = []
arregloRecibidos =[]
for line in file_numeros.readlines():
	if line in arregloEnviados:
		index = arregloEnviados.index(line)
		total = total + arregloRecibidos[index]
	else:
		s.sendall(line.encode('utf-8'))
		reply = s.recv(8)
		total = total + int(reply)
		arregloEnviados.append(line)
		arregloRecibidos.append(int(reply))
s.close()
print("ACTIVIDAD 3")
print(total)

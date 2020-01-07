from socket import socket

file_numeros = open('./numeros.txt','r')
total = 0
s = socket()
s.connect(('localhost', 9999))
for line in file_numeros.readlines():
	s.sendall(line.encode('utf-8'))
	reply = s.recv(5)
	total = total + int(reply)
s.close()
print("ACTIVIDAD 3")
print(total)

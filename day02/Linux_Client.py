#! /usr/bin/env python
import socket

host = "192.168.189.128"
port = 54123
buffersize = 1024
addr =(host,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

while True:
	data = input(">>:")
	if not data :
		continue
	print("input data :[%s]"%data)
	client.send(data.encode("utf-8"))
	rdata = client.recv(buffersize)
	if not rdata:
		break
	print(rdata.decode("utf-8"))
	if data == "byte" or data == "shutdown":
		break

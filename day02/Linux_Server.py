#! /usr/bin/env python
import socket
import time
import subprocess

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.189.128"
port = 54123
buffersize = 1024
addr = (host,port)

server.bind(addr)
server.listen(5)

quit = False
shutdown = False

while True:
	print("waitting for connection....")
	conn,address = server.accept()
	print("获得客户端的连接是:",address)
	while True:
		# 与客户端获取连接之后获取数据
		data = conn.recv(buffersize)
		data = data.decode("utf-8")
		if not data:
			break
		#ss = '[%s] %s'%(time.ctime(),data)
		cmd_status,cmd_result = subprocess.getstatusoutput(data)
		conn.send(cmd_result.encode("utf-8"))
		print(cmd_result)
		if data == "bye":
			quit = True
			break
		elif data == "shutdown":
			shutdown = True
			break
	print("Bye Bye:[%s:%d]"%(addr[0],addr[1]))
	conn.close()
	if shutdown:
		break
server.close()
print("Server has been closed")

				

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5405))

while True:
	data, address_client = sock.recvfrom(2048)
	# if data == b'Hello':
	print(data)
	sock.sendto(b'World', ('127.0.0.1', 5407))

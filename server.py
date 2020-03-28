import socket

serverpy = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) # AF_INET is IPv6 and SOCK_DGRAM is a UDP protocol
serverpy.bind(('', 12000)) # IP server and default port ('' means a localhost)
print('Server started!')

while True:
    msg_bytes, ip_client = serverpy.recvfrom(2048)  # recvfrom(buffer size). The return value is a pair (bytes, address)
    msg_answer = msg_bytes.decode('ascii').upper()
    serverpy.sendto(msg_answer.encode('ascii'),ip_client)
    print('Message: ', msg_answer)
    print('Connected by', ip_client)


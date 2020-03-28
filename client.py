import socket
import time


client = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) # AF_INET6 is IPv6 and SOCK_DGRAM is a UDP protocol
SERVER = input("Set the IP server: ")
PORT = 12000  # Port default: 12000
my_time = 60 * 15   # Default 900 seconds

while True:
    msg_send = input("What's the message? ")
    if msg_send:
        while my_time >= 0:
            client.sendto(msg_send.encode(), (SERVER, PORT)) 
            msg_bytes, ip_server = client.recvfrom(2048) # recvfrom(buffer size). The return value is a pair (bytes, address)
            print(msg_bytes.decode())
            time.sleep(1)
            my_time = my_time - 1
    else:
        print('Empty message!')
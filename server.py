import socket
from colorama import Fore
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = input('Enter IP Address: ')
port = input('Enter PORT number: ')

# serverSocket.bind(('192.168.189.220', 4445))
serverSocket.bind((ip, int(port)))

serverSocket.listen(2)
print(Fore.BLUE + f'🚀 server is running on PORT {port}\n   waiting for connect client...  '+ Fore.RESET)

c, address = serverSocket.accept()

print(f"{address} is connected . . .")

server_name = input('Enter Your Name: ')

while True:
    send_message = input(Fore.YELLOW+'Enter Your Message: '+ Fore.RESET)
    c.send(f'{server_name}: {send_message}'.encode())
    message = c.recv(1256).decode()
    print(message)

c.close()
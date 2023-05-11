import socket
from colorama import Fore

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input('Enter IP Address: ')
port = input('Enter PORT number: ')

# clientSocket.connect(('192.168.189.220', 4445))
clientSocket.connect((ip, int(port)))

print(Fore.GREEN + f'connect to {ip}' + Fore.RESET)

client_name = input('Enter Your Name: ')

while True:
    mesaage = clientSocket.recv(1256).decode()
    print(mesaage)
    send_message = input(Fore.YELLOW+'Write a Message : ' + Fore.RESET)
    clientSocket.send(f' {client_name}: {send_message}'.encode())

clientSocket.close()

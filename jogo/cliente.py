import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

while True:
    servidor = client.recv(1024).decode('utf-8')
    
    if "[C]" in servidor:
        print(servidor, end='')
        message = input("")
        client.send(message.encode('utf-8'))
    elif "chegou à linha de chegada" in servidor:
        print(servidor)
        break
    else:
        print(servidor)
    

client.close()

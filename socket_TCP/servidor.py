import socket

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8082))
    sock.listen(5)
    while True:
        print("Esperando comunicação do cliente...")
        client, address = sock.accept()
        data = client.recv(2048)
        if data:
            print("Mensagem recebida: %s" % data)
            client.send(data)
            print("Enviando %s de volta para %s" % (data, address))
            client.close()
server()

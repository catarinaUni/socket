import socket

def client():
    host = 'localhost'
    port = 8082
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect((host, port))
        print(f"Conectando em {host} porta {port}")

        message = input("Mensagem: ")
        print(f"Enviando: {message}")
        sock.sendall(message.encode('utf-8'))

        data = sock.recv(2048)
        print(f"Recebido: {data.decode('utf-8')}")

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Outros erros: {e}")
    finally:
        sock.close()

client()

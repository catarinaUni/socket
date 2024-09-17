import socket

def udp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 8082)
    
    try:
        message = input("Mensagem: ")
        message_bytes = message.encode('utf-8')
        print(f"Enviando: {message}")
        sock.sendto(message_bytes, server_address)
        
        data, server = sock.recvfrom(2048)
        print(f"Recebido: {data.decode('utf-8')}")
    finally:
        sock.close()

udp_client()

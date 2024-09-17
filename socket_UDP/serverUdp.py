import socket

def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 8082))
    
    while True:
        print("Esperando comunicação do cliente...")
        data, address = sock.recvfrom(2048)
        if data:
            print(f"Mensagem recebida: {data.decode('utf-8')} de {address}")
            sock.sendto(data, address)
            print(f"Enviando {data.decode('utf-8')} de volta para {address}")

udp_server()

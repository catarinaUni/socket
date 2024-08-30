# servidor.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Porta do servidor
    server_socket.listen(1)
    print("Servidor aguardando conexão...")
    
    conn, addr = server_socket.accept()
    print(f"Conectado com {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Recebido do cliente: {data.decode()}")
        conn.sendall(data)  # Eco do dado recebido

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

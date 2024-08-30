# cliente.py
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Conecta ao servidor real (na prática, deve ser o IP do interceptador)
    
    message = "Olá, servidor!"
    client_socket.sendall(message.encode())
    
    data = client_socket.recv(1024)
    print(f"Recebido do servidor: {data.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

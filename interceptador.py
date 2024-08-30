# interceptador.py
import socket
import threading

# Função para lidar com a comunicação entre cliente e servidor real
def handle_client(client_socket, server_socket):
    while True:
        try:
            # Recebe dados do cliente
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Interceptador recebeu do cliente: {data.decode()}")
            
            # Encaminha os dados para o servidor real
            server_socket.sendall(data)
            
            # Recebe a resposta do servidor real
            response = server_socket.recv(1024)
            print(f"Interceptador recebeu do servidor: {response.decode()}")
            
            # Envia a resposta para o cliente
            client_socket.sendall(response)
        except:
            break

    client_socket.close()
    server_socket.close()

# Função para iniciar o interceptador
def start_interceptor():
    intercept_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    intercept_socket.bind(('localhost', 12346))  # Porta do interceptador
    intercept_socket.listen(1)
    print("Interceptador aguardando conexão do cliente...")
    
    client_socket, _ = intercept_socket.accept()  # Aceita conexão do cliente
    print("Interceptador conectado ao cliente")

    # Conecta-se ao servidor real
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 12345))  # Conecta ao servidor real

    print("Interceptador conectado ao servidor real")

    # Inicia uma nova thread para lidar com a comunicação
    client_handler = threading.Thread(target=handle_client, args=(client_socket, server_socket))
    client_handler.start()

if __name__ == "__main__":
    start_interceptor()


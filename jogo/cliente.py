import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except ConnectionResetError:
            break

def main():
    # Configuração do cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5558))

    # Inicia a thread para receber mensagens do servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        command = input("Digite o comando (roll): ")
        if command == 'roll':
            client.send(command.encode('utf-8'))
        else:
            print("Comando inválido. Use 'roll' para rolar o dado.")

if __name__ == "__main__":
    main()

import socket
import threading
import random
import time

def handle_client(client_socket):
    global current_turn
    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8').strip()
            if not command:
                break

            if command == 'roll':
                if current_turn == 0:
                    dice_roll = random.randint(1, 6)
                    positions[0] += dice_roll
                    response = f"Cliente rolou um {dice_roll} e avançou para a posição {positions[0]}\n"
                    client_socket.send(response.encode('utf-8'))

                    # Verificar se há um vencedor
                    if positions[0] >= 20:
                        client_socket.send("Você ganhou! O jogo acabou.".encode('utf-8'))
                        break

                    # Alternar turno
                    current_turn = 1
                    client_socket.send("Aguardando a sua vez.".encode('utf-8'))
                else:
                    client_socket.send("Aguarde sua vez.".encode('utf-8'))
                    
            else:
                client_socket.send("Comando inválido. Use 'roll' para rolar o dado.".encode('utf-8'))

        except ConnectionResetError:
            break

    client_socket.close()

def handle_server_turn(client_socket):
    global current_turn, positions
    while True:
        time.sleep(1)  # wait for 1 second
        if current_turn == 1:
            while True:
                command = input("Digite o comando (roll): ")
                if command == 'roll':
                    server_dice_roll = random.randint(1, 6)
                    positions[1] += server_dice_roll
                    response = f"Servidor rolou um {server_dice_roll} e avançou para a posição {positions[1]}\n"
                    client_socket.send(response.encode('utf-8'))
                    break
                else:
                    print("Comando inválido. Use 'roll' para rolar o dado.")
                    
            if positions[1] >= 20:
                client_socket.send("O servidor ganhou! O jogo acabou.".encode('utf-8'))
                break

            # Alternar turno
            current_turn = 0
            client_socket.send("Aguardando a sua vez.".encode('utf-8'))

def main():
    global current_turn, positions
    current_turn = 0
    positions = [0, 0] 

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5558))
    server.listen(1)
    print("Servidor aguardando conexão...")

    try:
        client_socket, addr = server.accept()
        print(f"Cliente conectado de {addr}")

        client_socket.send("Bem-vindo ao jogo! Você é o Cliente.".encode('utf-8'))

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

        server_thread = threading.Thread(target=handle_server_turn, args=(client_socket,))
        server_thread.start()
    finally:
        server.close()  # Certifique-se de fechar o socket do servidor

if __name__ == "__main__":
    main()
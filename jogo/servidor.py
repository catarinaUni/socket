import socket
import random

def exibir_tabuleiro(placar):
    tabuleiro = ['_'] * 10
    s_pos = placar[1] if placar[1] < 10 else 9
    c_pos = placar[0] if placar[0] < 10 else 9

    if s_pos == c_pos:
        tabuleiro[s_pos] = 'S/C'
    else:
        tabuleiro[s_pos] = 'S'
        tabuleiro[c_pos] = 'C'

    return ''.join(tabuleiro) + "\n"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(1)

client_socket, addr = server.accept()
placar = [0, 0]
inicioJogo = exibir_tabuleiro(placar)

client_socket.send("---- INICIO DO JOGO ---- \n\n".encode('utf-8') + inicioJogo.encode('utf-8'))

print("---- INICIO DO JOGO ---- \n\n")
print(inicioJogo)

while True:
    client_socket.send("\n[C] Digite 1 para rolar o dado:  ".encode('utf-8'))
    message = client_socket.recv(1024).decode('utf-8').strip()
    if message == "1":
        dado = random.randint(1, 6)
        placar[0] += dado
        if placar[0] >= 10:
            tabuleiro = exibir_tabuleiro(placar)
            client_socket.send(tabuleiro.encode('utf-8'))
            print(tabuleiro)
            mensagemVencedor = f"O Cliente obteve {dado} e chegou à linha de chegada!!!"
            client_socket.send(mensagemVencedor.encode('utf-8'))
            print(mensagemVencedor)
            break
        else:
            mensagemDado = f"O Cliente jogou o dado e obteve: {dado}\n"
            client_socket.send(mensagemDado.encode('utf-8'))
            print(mensagemDado)

            tabuleiro = exibir_tabuleiro(placar)
            client_socket.send(tabuleiro.encode('utf-8'))
            print(tabuleiro)
        
            resposta = input("[S] Digite 1 para rolar o dado:  ")
            if resposta == "1":
                dado = random.randint(1, 6)
                placar[1] += dado
                if placar[1] >= 10:
                    tabuleiro = exibir_tabuleiro(placar)
                    client_socket.send(tabuleiro.encode('utf-8'))
                    print(tabuleiro)
                    mensagemVencedor = f"O Servidor obteve {dado} e chegou à linha de chegada!!!"
                    client_socket.send(mensagemVencedor.encode('utf-8'))
                    print(mensagemVencedor)
                    break
                else:
                    mensagemDado = f"O Servidor jogou o dado e obteve: {dado}\n"
                    client_socket.send(mensagemDado.encode('utf-8'))
                    print(mensagemDado)

                    tabuleiro = exibir_tabuleiro(placar)
                    client_socket.send(tabuleiro.encode('utf-8'))
                    print(tabuleiro)

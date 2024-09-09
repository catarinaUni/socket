import socket

def server(host='localhost', port=8082):
    data_payload = 2048  # Define o tamanho máximo de dados que podem ser recebidos.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP/IP.
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite a reutilização do endereço e porta.
    server_address = (host, port)  # Define o endereço do servidor.
    print("Servidor iniciado em: %s porta %s" % server_address)  # Exibe onde o servidor está rodando.
    sock.bind(server_address)  # Associa o socket ao endereço e porta.
    sock.listen(5)  # Configura o socket para escutar conexões, com uma fila de até 5 conexões pendentes.

    i = 0  # Contador para limitar o número de conexões.
    while True:
        print("Esperando comunicação do cliente...")  # Aguarda por uma conexão de um cliente.
        client, address = sock.accept()  # Aceita a conexão do cliente e obtém o socket do cliente e seu endereço.
        data = client.recv(data_payload)  # Recebe dados do cliente.
        if data:
            print("Mensagem recebida: %s" % data)  # Exibe a mensagem recebida do cliente.
            client.send(data)  # Envia os mesmos dados de volta ao cliente.
            print("Enviando %s de volta para %s" % (data, address))  # Exibe que os dados foram enviados de volta.
            client.close()  # Fecha a conexão com o cliente.
            i += 1  # Incrementa o contador de conexões.
            if i >= 3:  # Se o número de conexões atingir 3, o servidor para.
                break           
server()

import socket

# Configurações do servidor
host = 'localhost'  # Endereço IP ou nome de host do servidor
port = 4545         # Porta do servidor

# Cria um socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    client_socket.connect((host, port))
    print(f"Conexão estabelecida com {host}:{port}")

    # Envie dados para o servidor
    mensagem = "Olá, servidor!"
    client_socket.send(mensagem.encode())

    # Receba dados do servidor
    dados_recebidos = client_socket.recv(1024)
    print("Dados recebidos do servidor:", dados_recebidos.decode())

except Exception as e:
    print(f"Erro: {e}")

finally:
    # Feche o socket
    client_socket.close()
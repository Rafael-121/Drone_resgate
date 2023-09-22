import socket
import time
from threading import Timer

#address

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 4545))
s.listen(1)
print('Servidor ativo.')

def background_controller():
    mensagem = 'Seja bem vindo'
    print(mensagem)
    clientsocket.send(bytes(mensagem, "utf-8"))
    Timer(5, background_controller).start()

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} conexão estabelecida")
    background_controller()
import socket
import sys
import time
import os
from threading import Thread

HOST = '127.0.0.1'  # IP adress
PORT = 20001        # Port used by the server
BUFFER_SIZE = 4096   # buffer size for receiving data

FILE_DATA = {
    'small.txt': os.path.getsize('small.txt'),
    'medium.txt': os.path.getsize('medium.txt'),
    'large.txt': os.path.getsize('large.txt')
}

def on_new_client(clientsocket, addr):
    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            texto_recebido = data.decode('utf-8')
            print('Recebido do cliente {} na porta {}: {}'.format(addr[0], addr[1], texto_recebido))
            if texto_recebido in FILE_DATA:
                filename = texto_recebido
                filesize = FILE_DATA[filename]
                clientsocket.send(str(filesize).encode()) 
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        clientsocket.send(line.encode())  
                print('Arquivo {} enviado para o cliente {}'.format(filename, addr[0]))
            elif texto_recebido == 'bye':
                print('Fechando socket do cliente {}'.format(addr[0]))
                clientsocket.close()
                return
            else:
                clientsocket.send('Comando inválido'.encode())
        except Exception as error:
            print("Erro na conexão com o cliente!!")
            return

    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            texto_recebido = data.decode('utf-8') 
            print('recebido do cliente {} na porta {}: {}'.format(addr[0], addr[1],texto_recebido))
                   
            clientsocket.send(data)
            if (texto_recebido == 'bye'):
                print('vai encerrar o socket do cliente {} !'.format(addr[0]))
                clientsocket.close() 
                return 
        except Exception as error:
            print("Erro na conexão com o cliente!!")
            return


def main(argv):
    try:
        # AF_INET: indica o protocolo IPv4. SOCK_STREAM: tipo de socket para TCP,
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            while True:
                server_socket.listen()
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket,addr))
                t.start()   
    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)        
        return             



if __name__ == "__main__":   
    main(sys.argv[1:])
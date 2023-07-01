import socket
import sys
import time
import os

HOST = '127.0.0.1'  # IP adress
PORT = 20001        # Port used by the server
BUFFER_SIZE = 4096   # buffer size for receiving data

FILE_DATA = {
    'small.txt': os.path.getsize('small.txt'),
    'medium.txt': os.path.getsize('medium.txt'),
    'large.txt': os.path.getsize('large.txt')
}


def main(argv):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Conectado ao servidor!")
            while True:
                print("\nArquivos disponíveis: small.txt, medium.txt, large.txt")
                filename = input("Digite o nome do arquivo para enviar (ou 'bye' para sair): ")
                s.send(filename.encode())
                if filename == 'bye':
                    print('Fechando socket do cliente!')
                    s.close()
                    break
                elif filename in FILE_DATA:
                    data = s.recv(BUFFER_SIZE)
                    filesize = int(data.decode('utf-8'))
                    lines_received = 0
                    start_time = time.time() 
                    with open('received_{}'.format(filename), 'wb') as file:
                        while lines_received < filesize:
                            data = s.recv(BUFFER_SIZE)
                            file.write(data)
                            lines_received += len(data)
                    end_time = time.time()
                    total_time = round((end_time - start_time) * 1000, 2)
                    print('Arquivo {} recebido do servidor'.format(filename))
                    print('Total de bytes recebidos: {}'.format(lines_received))
                    print('Tempo total: {} ms'.format(total_time))
                else:
                    print('Nome de arquivo inválido')
    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":
    main(sys.argv[1:])

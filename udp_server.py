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

def send_file(file_path, client_address, server_socket):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            file_size = os.path.getsize(file_path)
            print("Enviando arquivo '{}' ({} bytes) para o cliente...".format(file_path, file_size))
            for line in lines:
                server_socket.sendto(line.encode(), client_address)
                time.sleep(0.01) 
            print("Arquivo enviado com sucesso!")
            return num_lines, file_size
    except Exception as error:
        print("Erro ao enviar o arquivo!")
        print(error)

def main(argv):
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as UDPServerSocket:
            UDPServerSocket.bind((HOST, PORT))
            print("Servidor UDP iniciado, Ouvindo...")
            while True:
                bytesAddressPair = UDPServerSocket.recvfrom(BUFFER_SIZE)
                request = bytesAddressPair[0].decode()
                client_address = bytesAddressPair[1]
                
                if request in FILE_DATA:
                    start_time = time.time()
                    num_lines, file_size = send_file(request, client_address, UDPServerSocket)
                    end_time = time.time()
                    total_time = (end_time - start_time) * 1000
                    print("Tempo total gasto no envio: {:.2f} ms".format(total_time))
                    print("Número de linhas do arquivo: {}".format(num_lines))
                    print("Tamanho do arquivo: {} bytes".format(file_size))
                else:
                    print("Arquivo inválido!")

    except Exception as error:
        print("Erro na execução do servidor!")
        print(error)

if __name__ == "__main__":
    main(sys.argv[1:])
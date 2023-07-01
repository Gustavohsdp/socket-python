import socket
import sys
import time

HOST = '127.0.0.1'  # IP adress
PORT = 20001        # Port used by the server
BUFFER_SIZE = 4096   # buffer size for receiving data

def receive_file(file_path, client_socket):
    try:
        with open(file_path, 'wb') as file:
            while True:
                data, _ = client_socket.recvfrom(BUFFER_SIZE)
                if not data:
                    break
                file.write(data)
    except Exception as error:
        print("Erro ao receber o arquivo!")
        print(error)

def main(argv):
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as UDPClientSocket:
            while True:
                arquivo = input("Digite o nome do arquivo a ser enviado (small, medium ou large) ou 'exit' para encerrar:\n")
                if arquivo == 'exit':
                    break

                UDPClientSocket.sendto(arquivo.encode(), (HOST, PORT))

                start_time = time.time()
                receive_file("cliente_{}.txt".format(arquivo), UDPClientSocket)
                end_time = time.time()

                total_time = (end_time - start_time) * 1000 
                num_lines = sum(1 for _ in open("cliente_{}.txt".format(arquivo)))
                file_size = os.path.getsize("cliente_{}.txt".format(arquivo))

    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)

if __name__ == "__main__":
    main(sys.argv[1:])
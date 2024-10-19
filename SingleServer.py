import socket
import sys
import threading

# Socket TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menetapkan server_host & server_port
server_host = '192.168.56.1'
server_port = 1234

# Menyiapkan sever socket (bind & listen)
serverSocket.bind((server_host, server_port))  # Misal server namanya localhost, portnya 1234
serverSocket.listen(5)  # Queue untuk clientnya bisa sampai 5

while True:
    # Respon server saat siap connect
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection received from: {addr}')

    try:
        # Menerima pesan permintaan dari client 
        message = connectionSocket.recv(1024).decode()
        # Mendapatkan path file
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Kirim header untuk menandakan bahwa file ditemukan
        connectionSocket.sendall("HTTP/1.1 200 OK\r\n\r\n".encode()) 

        # Mengirim konten file Test.html ke klien 
        for i in range(0, len(outputdata)):
            connectionSocket.sendall(outputdata[i].encode())
        connectionSocket.sendall("\r\n".encode())

        connectionSocket.close()

    except IOError: 
        # Kirim pesan 404 Not Found jika file tidak ditemukan
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 

        # Tutup socketnya
        connectionSocket.close() 

serverSocket.close() 
sys.exit()

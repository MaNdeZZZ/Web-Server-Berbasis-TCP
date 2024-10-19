from socket import *
import sys
import threading
import time
import os

DOCUMENT_ROOT = R'C:\SA Desk\Documents\SNK_Collage\SEMESTER 4\JARKOM\Tugas Besar Jarkom'  
# Sesuaikan dengan direktori tempat file-file server Anda berada

def client_handler(conn_socket, client_address):
    try:
        request_start_time = time.time()

        # Menerima pesan permintaan dari client
        request_message = conn_socket.recv(1024).decode()
        
        # Memeriksa apakah pesan permintaan kosong
        if not request_message:
            conn_socket.close()
            return

        # Mendapatkan path file yang diminta dari pesan permintaan
        requested_file = request_message.split()[1]
        
        # Menghilangkan karakter '/' jika dimulai dari '/'
        if requested_file.startswith('/'):
            requested_file = requested_file[1:]

        # Mengonstruksi path lengkap dari file yang diminta
        file_path = os.path.join(DOCUMENT_ROOT, requested_file)

        # Membuka file yang diminta
        with open(file_path, 'r') as file_to_open:
            file_content = file_to_open.read()

        # Mengirimkan balasan HTTP 200 OK
        response = "HTTP/1.1 200 OK\r\n\r\n" + file_content
        conn_socket.sendall(response.encode())

        # Menutup koneksi
        conn_socket.close()

        # Menghitung waktu eksekusi permintaan
        request_end_time = time.time()
        print(f"Request from {client_address} processed in {request_end_time - request_start_time:.5f} seconds.")

    except IOError:
        # Jika file tidak ditemukan, kirimkan balasan HTTP 404 Not Found
        conn_socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        conn_socket.close()

        # Menampilkan pesan kesalahan ke konsol
        request_end_time = time.time()
        print(f"Request from {client_address} failed: File not found. Processed in {request_end_time - request_start_time:.5f} seconds.")

    except Exception as e:
        # Menangkap kesalahan umum
        print(f"Request from {client_address} failed: {str(e)}")

        # Menutup koneksi
        conn_socket.close()

        # Menampilkan pesan kesalahan ke konsol
        request_end_time = time.time()
        print(f"Request from {client_address} failed: Unknown error. Processed in {request_end_time - request_start_time:.5f} seconds.")

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_address = '192.168.56.1'
    server_port = 1234

    # Mengikat socket server ke alamat dan port tertentu
    server_socket.bind((server_address, server_port))

    # Mendengarkan koneksi yang masuk dengan maksimum 5 koneksi pada antrian
    server_socket.listen(5)
    print('Server is up and running, ready to receive')

    while True:
        # Menerima koneksi dari client
        conn_socket, client_addr = server_socket.accept()
        print('Connection received from:', client_addr)

        # Mencetak working directory dan host serta port yang digunakan
        print("Working directory:", os.getcwd())
        print("Host:", server_address, ":", server_port)

        # Membuat thread baru untuk menangani setiap koneksi
        client_thread = threading.Thread(target=client_handler, args=(conn_socket, client_addr))
        client_thread.start()

    server_socket.close()

if __name__ == "__main__":
    main()

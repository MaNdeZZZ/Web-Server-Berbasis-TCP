import socket
import sys
import threading


def send_request(server_host, server_port):
    # Membuat socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Inisiasi IP address dan nomor port
    server_host = '192.168.56.1'
    server_port = 1234

    # Connect ke server
    print(f'Connecting to server {server_host} port {server_port}')
    client_socket.connect((server_host, server_port))

    try:

        # Mengirim HTTP GET request
        request = f'GET /{path} HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n'
        client_socket.sendall(request.encode())

        # Menerima respon server
        response = b''
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part

        # Menampilkan respon
        print(f'Response from server:\n{response.decode()}')

    finally:
        # Tutup koneksi
        client_socket.close()


def send_multiple_requests(server_host, server_port, path, num_requests):
    # Menyiapkan thread untuk beberapa request
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(server_host, server_port))
        threads.append(thread)
        thread.start()

    # Menunggu threads lengkap
    for thread in threads:
        thread.join()

if __name__ == "__main__":

    # Cara input dari client
    if len(sys.argv) != 5:
        print("Usage: py Client.py <server_host> <server_port> <path> <num_requests>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    path = sys.argv[3]
    num_requests = int(sys.argv[4])

    # Mengirimkan multiple request ke server
    send_multiple_requests(server_host, server_port, path, num_requests)

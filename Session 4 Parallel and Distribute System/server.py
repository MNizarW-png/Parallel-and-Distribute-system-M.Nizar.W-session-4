import socket
import time

def run_server():
    # 1. Membuat objek socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Mengizinkan penggunaan ulang alamat port jika server baru saja ditutup
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 2. Bind socket ke IP dan Port
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    
    # 3. Mendengarkan koneksi masuk
    server_socket.listen(1)
    print(f"Server berjalan dan mendengarkan pada {host}:{port}...")

    try:
        while True:
            # Menerima koneksi dari client (menangani secara sekuensial)
            client_socket, client_address = server_socket.accept()
            print(f"\n[Terhubung] Konek dengan client dari {client_address}")

            # Menerima data dari client (maksimal 1024 bytes)
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f"Pesan dari client: {message}")

            # Simulasi jeda singkat jika diperlukan
            time.sleep(1)

            # Mengirim konfirmasi kembali ke client
            response = "Message received successfully"
            client_socket.send(response.encode('utf-8'))

            # Menutup koneksi dengan client saat ini
            client_socket.close()
            print("[Keluputan] Koneksi ditutup, menunggu client berikutnya...")

    except KeyboardInterrupt:
        print("\nServer dihentikan oleh pengguna.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()
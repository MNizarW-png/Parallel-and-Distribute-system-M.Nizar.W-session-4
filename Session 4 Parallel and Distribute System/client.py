import socket

def run_client():
    host = '127.0.0.1'
    port = 12345

    print("Ketik pesan yang ingin dikirim ke server. Ketik 'exit' untuk keluar.")
    
    while True:
        # Meminta input teks dari pengguna
        message = input("\nMasukkan pesan: ")
        
        if message.lower() == 'exit':
            print("Keluar dari program client.")
            break

        if not message.strip():
            continue

        try:
            # Membuat socket baru untuk setiap pengiriman pesan (atau di dalam loop)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Menghubungkan ke server
            client_socket.connect((host, port))

            # Mengirim pesan yang diketik pengguna ke server
            client_socket.send(message.encode('utf-8'))

            # Menerima respon/konfirmasi dari server
            response = client_socket.recv(1024)
            print(f"Respon dari server: {response.decode('utf-8')}")

        except ConnectionRefusedError:
            print("Gagal terhubung ke server. Pastikan program server.py sudah dinyalakan!")
        finally:
            # Menutup koneksi dengan benar
            client_socket.close()

if __name__ == "__main__":
    run_client()
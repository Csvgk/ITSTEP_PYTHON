import socket
import threading

# Подія "чат завершено": її ставить той потік, який першим побачив exit
chat_over = threading.Event()


def receive_messages(conn):
    while not chat_over.is_set():
        try:
            data = conn.recv(1024)
        except OSError:
            break
        if not data:
            # Якщо ми самі завершили чат, повідомлення не потрібне
            if not chat_over.is_set():
                print("Клієнт закрив з'єднання")
            break
        message = data.decode()
        if message.strip().lower() == "exit":
            print("Клієнт завершив чат. Натисніть Enter для виходу")
            break
        print(f"Клієнт: {message}")
    chat_over.set()


def send_messages(conn):
    while True:
        message = input()
        # Якщо співрозмовник уже вийшов, нічого не надсилаємо
        if chat_over.is_set():
            break
        try:
            conn.sendall(message.encode())
        except OSError:
            print("Не вдалося надіслати повідомлення, з'єднання розірвано")
            break
        if message.strip().lower() == "exit":
            print("Ви завершили чат")
            break
    chat_over.set()


def main():
    host = "127.0.0.1"
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Сервер очікує підключення на {host}:{port}...")

    conn, address = server_socket.accept()
    print(f"Клієнт підключився: {address}. Введіть 'exit' для виходу")

    receive_thread = threading.Thread(target=receive_messages, args=(conn,))
    receive_thread.start()

    try:
        send_messages(conn)
    except (KeyboardInterrupt, EOFError):
        print("\nЧат перервано")
    finally:
        chat_over.set()
        # shutdown розблоковує recv() у потоці прийому, потім закриваємо сокети
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        receive_thread.join()
        conn.close()
        server_socket.close()
        print("Сервер завершив роботу")


if __name__ == "__main__":
    main()

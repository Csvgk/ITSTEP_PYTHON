import socket
import threading

# Подія "чат завершено": її ставить той потік, який першим побачив exit
chat_over = threading.Event()


def receive_messages(client_socket):
    while not chat_over.is_set():
        try:
            data = client_socket.recv(1024)
        except OSError:
            break
        if not data:
            # Якщо ми самі завершили чат, повідомлення не потрібне
            if not chat_over.is_set():
                print("Сервер закрив з'єднання")
            break
        message = data.decode()
        if message.strip().lower() == "exit":
            print("Сервер завершив чат. Натисніть Enter для виходу")
            break
        print(f"Сервер: {message}")
    chat_over.set()


def send_messages(client_socket):
    while True:
        message = input()
        # Якщо співрозмовник уже вийшов, нічого не надсилаємо
        if chat_over.is_set():
            break
        try:
            client_socket.sendall(message.encode())
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

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Не вдалося підключитися. Спочатку запустіть сервер")
        client_socket.close()
        return
    print("Підключено до сервера. Введіть 'exit' для виходу")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    try:
        send_messages(client_socket)
    except (KeyboardInterrupt, EOFError):
        print("\nЧат перервано")
    finally:
        chat_over.set()
        # shutdown розблоковує recv() у потоці прийому, потім закриваємо сокет
        try:
            client_socket.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        receive_thread.join()
        client_socket.close()
        print("Клієнт завершив роботу")


if __name__ == "__main__":
    main()

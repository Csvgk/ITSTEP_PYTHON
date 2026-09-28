import socket
import threading


def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)
        except OSError:
            break
        if not data:
            print("Клієнт закрив з'єднання")
            break
        message = data.decode()
        if message.strip().lower() == "exit":
            print("Клієнт завершив чат")
            break
        print(f"Клієнт: {message}")


def send_messages(conn):
    while True:
        message = input()
        conn.sendall(message.encode())
        if message.strip().lower() == "exit":
            print("Ви завершили чат")
            break


def main():
    host = "127.0.0.1"
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Сервер очікує підключення на {host}:{port}...")

    conn, address = server_socket.accept()
    print(f"Клієнт підключився: {address}")

    receive_thread = threading.Thread(target=receive_messages, args=(conn,))
    receive_thread.start()

    send_messages(conn)

    receive_thread.join(timeout=2)

    conn.close()
    server_socket.close()
    print("Сервер завершив роботу")


if __name__ == "__main__":
    main()
import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
        except OSError:
            break
        if not data:
            print("Сервер закрив з'єднання")
            break
        message = data.decode()
        if message.strip().lower() == "exit":
            print("Сервер завершив чат")
            break
        print(f"Сервер: {message}")


def send_messages(client_socket):
    while True:
        message = input()
        client_socket.sendall(message.encode())
        if message.strip().lower() == "exit":
            print("Ви завершили чат")
            break


def main():
    host = "127.0.0.1"
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Підключено до сервера")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_messages(client_socket)

    receive_thread.join(timeout=2)

    client_socket.close()
    print("Клієнт завершив роботу")


if __name__ == "__main__":
    main()
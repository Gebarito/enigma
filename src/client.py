import socket
from enigma import encrypt
from constants import SERVER_ADDRESS, SERVER_PORT

def run_client() -> socket.socket:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_ADDRESS, SERVER_PORT))
    except Exception as e:
        return print(f"Erro ao conectar ao servidor: {e}")

    print("Conectado ao servidor.")
    return client


def send_messages(client) -> None:
    '''
        Envia mensagens para o servidor.

        param client: socket do cliente
        type client: socket.socket
        return: None
    '''
    while True:
        msg = input("Digite sua mensagem: ")
        if msg == 'quit':
            break

        encrypted_msg = encrypt(msg)

        try:
            client.send(encrypted_msg.encode('utf-8'))
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

def receive_messages(client) -> None:
    '''
        Recebe mensagens do servidor.

        param client: socket do cliente
        type client: socket.socket
        return: None
    '''
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')

            #decrypted_msg = enigma.decrypt(msg)
            #print(decrypted_msg + '\n')
            print(msg + '\n')
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")


if __name__ == "__main__":
    connection = run_client()

    while connection:
        send_messages(connection)
        receive_messages(connection)


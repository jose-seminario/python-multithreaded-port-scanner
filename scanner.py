import socket


def scanner(ip, port):
    connection = socket.socket()
    connection.settimeout(1)

    try:
        connection.connect((ip, port))
        return True

    except:
        return False

    finally:
        connection.close()


def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"
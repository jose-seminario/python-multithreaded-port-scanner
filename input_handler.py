def get_user_option():
    while True:
        try:
            user_option = int(input("Choose an option: "))

        except:
            print("Please enter a valid number.")
            continue

        if user_option == 1 or user_option == 2:
            return user_option

        print("Please choose option 1 or 2.")


def get_ip():
    return input("Enter IP address or domain: ")


def get_port_range():
    while True:
        try:
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

        except:
            print("Please enter a valid number.")
            continue

        if not (0 <= start_port <= 65535):
            print("Start port must be between 0 and 65535.")
            continue

        if not (0 <= end_port <= 65535):
            print("End port must be between 0 and 65535.")
            continue

        if start_port > end_port:
            print("Start port cannot be greater than end port.")
            continue

        return start_port, end_port
    
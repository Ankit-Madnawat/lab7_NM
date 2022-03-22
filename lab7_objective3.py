try:
    from netmiko import ConnectHandler
except:
    print("Install necessary modules!")


def main():
    device_1 = {
        'device_type': 'cisco_ios',
        'host': '198.51.100.3',
        'username': 'lab',
        'password': 'lab123'
    }

    device_2 = {
        'device_type': 'cisco_ios',
        'host': '198.51.100.4',
        'username': 'lab',
        'password': 'lab123'
    }

    device_3 = {
        'device_type': 'cisco_ios',
        'host': '198.51.100.5',
        'username': 'lab',
        'password': 'lab123'
    }

    with open('R1.txt', 'r') as file1:
        lines1 = file1.read().splitlines()
        connection1 = ConnectHandler(**device_1)
        connection1.enable()
        connection1.send_config_set(lines1)
        connection1.disconnect()
    print("R1 configured.")

    with open('R2.txt', 'r') as file2:
        lines2 = file2.read().splitlines()
        connection2 = ConnectHandler(**device_2)
        connection2.enable()
        connection2.send_config_set(lines2)
        connection2.disconnect()
    print("R2 configured.")

    with open('R3.txt', 'r') as file3:
        lines3 = file3.read().splitlines()
        connection3 = ConnectHandler(**device_3)
        connection3.enable()
        connection3.send_config_set(lines3)
        connection3.disconnect()
    print("R3 configured.")


if __name__ == "__main__":
    main()
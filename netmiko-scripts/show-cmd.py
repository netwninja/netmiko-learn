from netmiko import ConnectHandler
from getpass import getpass

node = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**node)
output = net_connect.send_command("show version")
print(output)

with open("show_version.txt", "w") as save_data:
    save_data.write(output)

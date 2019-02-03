from netmiko import ConnectHandler
from getpass import getpass

pasw = getpass()

R1 = {
  "device_type": "cisco_xe",
  "host": "cisco3.lasthop.io",
  "username": "pyclass",
  "password": pasw,
}

R2 = {
  "device_type": "cisco_xe",
  "host": "cisco4.lasthop.io",
  "username": "pyclass",
  "password": pasw,
}

for device in (R1, R2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show version")
    print (output)

with open("show_version.txt", "w") as save_data:
    save_data.write(output)

net_connect.disconnect()

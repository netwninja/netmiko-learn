from netmiko import ConnectHandler 
from getpass import getpass 

pasw = getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": pasw,
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": pasw,
    "device_type": "cisco_nxos",
}

for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())

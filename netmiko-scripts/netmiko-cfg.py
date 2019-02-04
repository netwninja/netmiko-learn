from netmiko import ConnectHandler
from getpass import getpass

pasw = getpass()

node1 = {
  "device_type": "cisco_xe",
  "host": "cisco3.lasthop.io",
  "username": "pyclass",
  "password": pasw,
  "session_log": "node1.txt",
}

net_connect = ConnectHandler(**node1)
print(net_connect.find_prompt())

cfg = 'no ip name-server 4.2.2.2'
output = net_connect.send_config_set(cfg)
print (output)

net_connect.disconnect()

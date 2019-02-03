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

command = 'delete flash:/del.txt'
command2 = 'dir flash:'

output = net_connect.send_command_timing(command2,
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(command,
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("y",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(command2,
    strip_prompt=False, strip_command=False)
print (output)

net_connect.disconnect()

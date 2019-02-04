from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
pasw = getpass()

node1 = {
  "device_type": "cisco_ios",
  "host": "10.0.0.104",
  "username": "gasood",
  "password": pasw,
  #"session_log": "node.txt",
}

net_connect = ConnectHandler(**node1)
output = net_connect.send_command("show ip arp", use_textfsm=True)
pprint(output)

net_connect.disconnect()


##########SAMPLE OUTPUT##########
#python show-textfsm.py
Password:
[{'address': '10.0.0.1',
  'age': '0',
  'interface': 'Ethernet0/0',
  'mac': 'a42b.b0e2.67a0',
  'protocol': 'Internet',
  'type': 'ARPA'},
 {'address': '10.0.0.32',
  'age': '116',
  'interface': 'Ethernet0/0',
  'mac': '000c.29a2.f76a',
  'protocol': 'Internet',
  'type': 'ARPA'},
 {'address': '10.0.0.104',
  'age': '-',
  'interface': 'Ethernet0/0',
  'mac': 'aabb.cc01.2000',
  'protocol': 'Internet',
  'type': 'ARPA'},
 {'address': '10.0.0.145',
  'age': '0',
  'interface': 'Ethernet0/0',
  'mac': '000c.29f3.26fe',
  'protocol': 'Internet',
  'type': 'ARPA'}]

############SAMPLE OUTPUT END########

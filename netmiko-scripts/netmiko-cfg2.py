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

cfg = [
    ' no ip name-server 4.2.2.2',
    ' no ip name-server 8.8.8.8',
]
output = net_connect.send_config_set(cfg)
print (output)

net_connect.disconnect()

###############SAMPLE OUTPUT###########
(py3_venv) [gsood@ip-172-30-0-124 ~]$ python netmiko-cfg2.py
Password:
cisco3#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
cisco3(config)# no ip name-server 4.2.2.2
cisco3(config)# no ip name-server 8.8.8.8
cisco3(config)#end
cisco3#
##########SAMPLE OUTPUT END###########

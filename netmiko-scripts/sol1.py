from netmiko import ConnectHandler 
from getpass import getpass 

node = ConnectHandler(
    host='cisco3.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_ios',
    session_log='my_log.txt',
)

print(node.find_prompt())


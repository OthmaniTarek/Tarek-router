from netmiko import (
  ConnectHandler,
)

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxr-1.cisco.com', 
    'username': 'admin',
    'password': 'C1sco12345',
    'secret': 'enablepass',
    'port': 22,
}
conn = ConnectHandler(**cisco_router)
output = conn.send_command('show ip int br')
print(output)
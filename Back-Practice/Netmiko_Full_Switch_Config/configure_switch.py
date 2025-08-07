import yaml # pyright: ignore[reportMissingModuleSource]
from jinja2 import Environment, FileSystemLoader # pyright: ignore[reportMissingImports]
from netmiko import ConnectHandler  # pyright: ignore[reportMissingImports]


## Load all yaml files

with open ("switch_config_data.yaml") as data:
    config = yaml.safe_load (data)

with open ("device_inventory.yaml") as devices:
    inventory = yaml.safe_load (devices) ["inventory"]

with open ("device_credentials.yaml") as cred: 
    credenatials = yaml.safe_load(cred)

##Select Device
print ("Available Devices:")
for i , inv in enumerate(inventory):
    print (f"{i+1}.{inv['name']} ({inv['host']})")

choice = int(input ("Select device by number: ")) - 1
selected_device = inventory[choice]


## Prompt for Hostname
hostname = input (f"Enter hostname for {selected_device ['name']}:")

##Prompt for VLAN's

vlans = {}
for vlan_type in ['data','voice','mgmt']:
    vlan_id = input (f"Enter VLAN ID for {vlan_type}: ")
    vlan_ip = input (f" Enter IP address for VLAN {vlan_type}: ")
    vlan_mask = input (f"Enter subnet mask for VLAN {vlan_type}: ")
    vlans[vlan_type] = {"id": vlan_id, "ip": vlan_ip , "mask": vlan_mask}

##Jinja Template Rendenring  
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("switch_syntax.j2")

rendered  = template.render(
    hostname = hostname,
    snmp = config['snmp'],
    ntp = config ['ntp'],
    access_list = config['access_list'],
    vlans = vlans
)

##Print Config

print ("\nGenerated Configuration:\n")
print (rendered)

## Build Device Connection dictionary 

device_params = {
    "device_type": credenatials["device_type"],
    "host":selected_device["host"],
    "username": credenatials["username"],
    "password": credenatials ["password"],
    "secret": credenatials["enable_password"] 
}

##Deploy Config
net_connect = ConnectHandler (**device_params)
net_connect.enable()
net_connect.send_config_set(rendered.splitlines())
net_connect.disconnect()

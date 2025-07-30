import yaml  # pyright: ignore[reportMissingModuleSource]
from jinja2 import Environment, FileSystemLoader  # pyright: ignore[reportMissingImports]
from netmiko import ConnectHandler  # pyright: ignore[reportMissingImports]


# Define Cisco devices
cisco_switch = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.135.131",
        "username": "netg",
        "password": "netg"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.135.132",
        "username": "netg",
        "password": "netg"
    }
]


# Load SNMP config from YAML
with open ("snmp-data.yaml", 'r') as yaml_file:
    snmp_data = yaml.safe_load(yaml_file)
  
# Render SNMP config using Jinja2    
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('snmp-template.j2')


rendered_output = template.render(snmp_data=snmp_data)
print("\nGenerated SNMP Config:\n")
print(rendered_output)
 
conf_data = rendered_output.strip().splitlines()   

for switch in cisco_switch:
    print(f"/n---connecting to {switch['host']}---")
    net_connect = ConnectHandler(**switch)
    output = net_connect.send_config_set(conf_data)
    print(output)
    net_connect.disconnect()
import yaml # pyright: ignore[reportMissingModuleSource]
from jinja2 import Environment, FileSystemLoader # pyright: ignore[reportMissingImports]
from netmiko import ConnectHandler  # pyright: ignore[reportMissingImports]


cisco_switch = [{
    "device_type" : "cisco_ios",
    "host" : "192.168.135.131",
    "username" : "netg",
    "password" : "netg"
    
},

{
    "device_type" : "cisco_ios",
    "host" : "192.168.135.132",
    "username" : "netg",
    "password" : "netg"
    
}]

with open ("conf-data.yaml",'r') as yaml_file:
    intf_conf_data = yaml.safe_load(yaml_file)
    
# print (intf_conf_data)  

env = Environment (loader=FileSystemLoader ('.'))
template = env.get_template('intf-syntax.j2')

rendered_output = template.render (intf_conf_data=intf_conf_data)
print(rendered_output)
conf_data= rendered_output.splitlines()
# print(conf_data)

for switch in cisco_switch:
 net_connect = ConnectHandler(**switch)
 output = net_connect.send_config_set(conf_data)
#  print(output)
  



import yaml
from jinja2 import Environment, FileSystemLoader


intf_data_file = open ("config_data.yaml", "r") #Open a file named config_data.yaml for reading.
sw_config_data = yaml.safe_load(intf_data_file) #safely parses the YAML into a Python object 


##Load the Jinja2 template from file
template_loader= FileSystemLoader (searchpath=".") #Looks for template files in the current directory.
env = Environment(loader=template_loader) # Jinja2 environment configured with that loader.
template= env.get_template("multi_intf_config.j2") # Loads the file intf_config.j2 as a Jinja2 template.

 ##Python code to render config data into jinja2 template to 
rendered_output = template.render (data_list=sw_config_data) #Fills the Jinja2 template with values from sw_config_data.
print(rendered_output) #### Data will be in string


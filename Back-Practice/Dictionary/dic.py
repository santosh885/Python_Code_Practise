# new_device_info = [
    # { "device_ip": "10.1.2.3", "model": 9800, "site": "site-a", "rack": "rack1", "os_ver": 16.6,
    #  "mgmt_ips": ["10.1.3.1", "10.1.3.2"]},
    #  { "device_ip": "10.2.2.3", "model": 9300, "site": "site-b", "rack": "rack2", "os_ver": 16.7,
    #    "mgmt_ips": ["10.1.3.1", "10.1.3.2"]},
    #  { "device_ip": "10.3.2.3", "model": 9500, "site": "site-c", "rack": "rack3", "os_ver": 16.8,
    #    "mgmt_ips": ["10.1.4.1","10.1.4.2"]}
# ]
# print(new_device_info[0].keys())
# print(new_device_info[1].items())
# print(new_device_info)

##Above program is list of dictionaries
###############################################################################################

###Below program is dictionary of dictionaries

# inventory = {
# "switch1": { "device_ip": "10.1.2.3", "model": 9800, "site": "site-a", "rack": "rack1", "os_ver": 16.6,
#      "mgmt_ips": ["10.1.3.1", "10.1.3.2"]},
# "switch2": { "device_ip": "10.2.2.3", "model": 9300, "site": "site-b", "rack": "rack2", "os_ver": 16.7,
#       "mgmt_ips": ["10.1.3.1", "10.1.3.2"]},
# "switch3" : { "device_ip": "10.3.2.3", "model": 9500, "site": "site-c", "rack": "rack3", "os_ver": 16.8,
#        "mgmt_ips": ["10.1.4.1","10.1.4.2"]}
# }
# print(inventory)
# print(inventory["switch1"])
# print(inventory["switch3"])
# print(inventory["switch2"] ["mgmt_ips"])
# print(inventory["switch2"] ["mgmt_ips"] [0])


#######################################################################################33

new_device_info = [
    { "device_ip": "10.1.2.3", "model": 9800, "site": "site-a", "rack": "rack1", "os_ver": 16.6,
     "mgmt_ips": ["10.1.3.1", "10.1.3.2"]},
     { "device_ip": "10.2.2.3", "model": 9300, "site": "site-b", "rack": "rack2", "os_ver": 16.7,
       "mgmt_ips": ["10.1.3.1", "10.1.3.2"]},
     { "device_ip": "10.3.2.3", "model": 9500, "site": "site-c", "rack": "rack3", "os_ver": 16.8,
       "mgmt_ips": ["10.1.4.1","10.1.4.2"]}
]

# for item in new_device_info:
#     print(item)
#     print(type(item))

sw1= { "device_ip": "10.1.2.3", "model": 9800, "site": "site-a", "rack": "rack1", "os_ver": 16.6,
     "mgmt_ips": ["10.1.3.1", "10.1.3.2"]}

# print(sw1.values())
# print(sw1.keys())
# print(sw1.items())

for k,v in sw1.items():
    print (k,v)
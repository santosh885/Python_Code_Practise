import requests
import urllib3
import xml.etree.ElementTree as ET

urllib3.disable_warnings()

fw_ip = "10.242.5.9"
api_key = "LUFRPT1IQ0hYa1JnK0EybGxXTEUwakE3em9jc1ZWNzg9SWJDL0gwZHpFTE0vaVdLbXJoT1R1ZXd6SWNuVWVxTUpCQjRQQWpKcnVJWUdqaytaSFQveTNlbWFXZ0hPNDY0dw=="

url = f"https://{fw_ip}/api/?type=op&cmd=<show><vpn><ipsec-sa></ipsec-sa></vpn></show>&key={api_key}"

response = requests.get(url, verify=False)

root = ET.fromstring(response.text)

for entry in root.findall(".//entry"):
    name = entry.findtext("name")
    gateway = entry.findtext("gateway")
    remote = entry.findtext("remote")
    enc = entry.findtext("enc")

    print(f"{gateway} | {name} | Peer: {remote} | Encryption: {enc}")
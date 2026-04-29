# import requests
# import urllib3
# import xml.etree.ElementTree as ET

# urllib3.disable_warnings()

# fw_ip = "10.242.5.9"
# api_key = "LUFRPT0wdmMraFRSYWdjdko2L3pUMWdReDc5dFB2aTg9SWJDL0gwZHpFTE0vaVdLbXJoT1R1Vlpud0g0S0UrRzhBeXVMTnhjT0J4MzQzOFE0bEF5bDZZWW9hNHVuNkdpeA=="

# # -------- CONFIG (IP) --------
# config_url = f"https://{fw_ip}/api/?type=config&action=get&xpath=/config/devices/entry/network/interface&key={api_key}"
# config_response = requests.get(config_url, verify=False)
# config_root = ET.fromstring(config_response.text)

# ip_map = {}

# for entry in config_root.findall(".//entry"):
#     name = entry.get("name")
#     ip_entry = entry.find(".//ip/entry")

#     if ip_entry is not None:
#         ip_map[name] = ip_entry.get("name")

# # -------- OP (STATE + MAC) --------
# cmd = "<show><interface>all</interface></show>"
# url = f"https://{fw_ip}/api/?type=op&cmd={cmd}&key={api_key}"

# response = requests.get(url, verify=False)
# root = ET.fromstring(response.text)

# print("\n===== Interface Status =====")

# seen = set()  # remove duplicates

# for entry in root.findall(".//entry"):

#     name = entry.get("name") or entry.findtext("name")

#     if not name or name in seen:
#         continue

#     seen.add(name)

#     # ✅ FIXED STATE
#     state = entry.findtext("./link/state") or entry.findtext("state")

#     mac = entry.findtext("mac")
#     ip = ip_map.get(name, "N/A")

#     print(f"{name} | {state or 'N/A'} | IP: {ip} | MAC: {mac}")



###################################new script##########################



import requests
import urllib3
import xml.etree.ElementTree as ET
import os
import sys

urllib3.disable_warnings()

# -------- CONFIG --------
fw_ip = "10.242.5.9"
api_key = os.getenv("FW_API_KEY")  # Use GitLab variable

if not api_key:
    print("ERROR: API key not found. Set FW_API_KEY")
    sys.exit(1)

# -------- STEP 1: GET CONFIG (IP ADDRESS) --------
config_url = f"https://{fw_ip}/api/?type=config&action=get&xpath=/config/devices/entry/network/interface&key={api_key}"

config_response = requests.get(config_url, verify=False)
config_root = ET.fromstring(config_response.text)

ip_map = {}

for entry in config_root.findall(".//entry"):
    name = entry.get("name")
    ip_entry = entry.find(".//ip/entry")

    if name and ip_entry is not None:
        ip_map[name] = ip_entry.get("name")

# -------- STEP 2: GET OPERATIONAL DATA (STATE + MAC) --------
cmd = "<show><interface>all</interface></show>"
url = f"https://{fw_ip}/api/?type=op&cmd={cmd}&key={api_key}"

response = requests.get(url, verify=False)
root = ET.fromstring(response.text)

print("\n===== Interface Status =====")

seen = set()
down_interfaces = []

for entry in root.findall(".//entry"):

    name = entry.get("name") or entry.findtext("name")

    if not name or name in seen:
        continue

    seen.add(name)

    # Get interface state correctly
    state = entry.findtext("./link/state") or entry.findtext("state") or "unknown"

    mac = entry.findtext("mac") or "N/A"
    ip = ip_map.get(name, "N/A")

    print(f"{name:<15} | {state:<6} | IP: {ip:<18} | MAC: {mac}")

    # Track DOWN interfaces
    if state.lower() != "up":
        down_interfaces.append(name)

# -------- STEP 3: FAIL PIPELINE IF DOWN --------
if down_interfaces:
    print("\n❌ ALERT: Interfaces DOWN:", ", ".join(down_interfaces))
    sys.exit(1)

print("\n✅ All interfaces are UP")
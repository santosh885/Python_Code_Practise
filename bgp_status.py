import requests
import urllib3
import xml.etree.ElementTree as ET

urllib3.disable_warnings()

fw_ip = "10.242.5.9"
api_key = "LUFRPT02bHNRVlJMR0NORm5mTVhiUTYvTWJCcFBCNm89SWJDL0gwZHpFTE0vaVdLbXJoT1R1ZXNuVHU4L2VSb1NlSVBNc0p6RHNUYTlaZEFRVHl1TUJwUkhLZmEvaGU2MQ=="

virtual_routers = ["User7_Primary_Mum_SASE", "User7_Secondary_Mum_SASE"]

for vr in virtual_routers:
    print(f"\n===== VR: {vr} =====")

    cmd = f"<show><routing><protocol><bgp><peer><virtual-router>{vr}</virtual-router></peer></bgp></protocol></routing></show>"
    url = f"https://{fw_ip}/api/?type=op&cmd={cmd}&key={api_key}"

    response = requests.get(url, verify=False)
    root = ET.fromstring(response.text)

    for peer in root.findall(".//entry"):
        peer_name = peer.findtext("peer-name")
        peer_ip = peer.findtext("peer-address")
        state = peer.findtext("status")
        remote_as = peer.findtext("remote-as")

        # Skip empty entries
        if not peer_ip:
            continue

        print(f"{peer_name} | {peer_ip} | State: {state} | AS: {remote_as}")
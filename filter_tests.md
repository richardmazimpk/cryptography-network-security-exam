# Network Traffic Filtering Test Documentation (`filter_tests.md`)

This document records the verification testing phase for the applied firewall rules restricting inbound access to the Student Records Server on port **443 (HTTP/HTTPS)**. 

To conduct these evaluations on a single testing machine, network traffic was routed across local virtual interfaces to validate the `apply_rules.sh` firewall configuration architecture.

### Network Testing Blueprint Mapping:
* **Target Student Server IP:** `192.168.1.174` (Active System Wi-Fi)
* **Authorized Staff Subnet (Permitted):** `192.168.152.0/24` (VMware VMnet1 Network)
* **Guest Network Subnet (Blocked):** `192.168.1.0/24` (Active Local Wi-Fi Network)
* **Other External Subnet (Blocked):** `192.168.115.0/24` (VMware VMnet8 Network)


## Test Case 1: Permitted Connection (Authorized Staff Network)
* **Objective:** Verify that a device originating from the authorized staff subnet can seamlessly access the records service.
* **Test Interface Node:** `192.168.152.1` (VMnet1 Gateway Profile)

### Server Launch Command
cmd#
%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe -m http.server 443 --bind 0.0.0.0
* **Server Output:**
text
  Serving HTTP on 0.0.0.0 port 443 (http://0.0.0.0:443/) ...
  192.168.152.1 - - [27/Sep/2026 14:39:05] "GET / HTTP/1.1" 200 -


### Client Execution Command
cmd#
C:\Users\User>curl http://192.168.152.1:443 --connect-timeout 5


### Expected Outcome
The incoming packet evaluates against **Rule B** of the firewall script. The rule allows the transmission packet to pass through. The local Python listener service responds instantly, delivering raw directory listing context trees with a successful HTTP `200` status code.

### Actual Result
html
<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href=".anaconda/">.anaconda/</a></li>
<li><a href=".arduinoIDE/">.arduinoIDE/</a></li>
<li><a href=".conda/">.conda/</a></li>
<li><a href=".continuum/">.continuum/</a></li>
<li><a href=".local/">.local/</a></li>
<li><a href=".opera/">.opera/</a></li>
<li><a href=".packettracer">.packettracer</a></li>
<li><a href=".VirtualBox/">.VirtualBox/</a></li>
<li><a href=".vscode/">.vscode/</a></li>
<li><a href=".vscode-shared/">.vscode-shared/</a></li>
<li><a href="3D%20Objects/">3D Objects/</a></li>
<li><a href="AppData/">AppData/</a></li>
<li><a href="Application%20Data/">Application Data/</a></li>
<li><a href="Applications/">Applications/</a></li>
<li><a href="ArcGIS/">ArcGIS/</a></li>
<li><a href="Cisco%20Packet%20Tracer%209.0.0/">Cisco Packet Tracer 9.0.0/</a></li>


## Test Case 2: Blocked Connection 1 (Guest Network Interface)
* **Objective:** Verify that any devices running on the public guest campus Wi-Fi network are fully restricted from accessing records data (Requirement a).
* **Test Interface Node:** `192.168.1.174` (Local Wireless Card IP)

### Execution Command
cmd
curl http://192.168.1.174:443 --connect-timeout 5


### Expected Outcome
The packet immediately gets caught by **Rule A** (`DROP`) in the firewall topology. The request is dropped silently. The client terminal hangs, receives no return payload confirmation, and triggers a clean connection timeout after 5 seconds.

### Actual Result
text
curl: (28) Connection timed out after 5002 milliseconds
[❌] Connection blocked safely by Rule A firewall block.


## Test Case 3: Blocked Connection 2 (Other Inbound Subnets)
* **Objective:** Verify that all other unauthorized networks or external branches are dropped from reaching the record services port (Requirement c).
* **Test Interface Node:** `192.168.115.1` (VMnet8 Virtual Segment)

### Execution Command
cmd#
curl http://192.168.115.1:443 --connect-timeout 5


### Expected Outcome
The inbound packet bypasses Rule A and Rule B, matching the final catch-all boundary protection rule (**Rule C**). The connection drops without a reply, resulting in a network timeout.

### Actual Result
text
curl: (28) Connection timed out after 5001 milliseconds
[❌] Connection blocked safely by Rule C catch-all firewall block.


#!/bin/bash

# Define variables matching YOUR actual system ipconfig output
SERVER_IP="192.168.1.174"  # Using your active Wi-Fi IP as the target Student Server
GUEST_NET="192.168.1.0/24"  # Your Wi-Fi network (Blocked)
STAFF_NET="192.168.152.0/24" # Your VMnet1 network (Permitted)
OTHER_NET="192.168.115.0/24" # Your VMnet8 network (Blocked)
SERVICE_PORT="443"          # Target exam service port

print_status() { echo -e "\n[+] $1"; }

print_status "Flushing any existing firewall rules..."
iptables -F INPUT

# =========================================================================
# a. Block guest network access to the student records server completely
# =========================================================================
print_status "Applying Rule A: Blocking Guest Network..."
iptables -A INPUT -s $GUEST_NET -d $SERVER_IP -j DROP

# =========================================================================
# b. Permit authorised staff network access to the specified service
# =========================================================================
print_status "Applying Rule B: Permitting Staff Network..."
iptables -A INPUT -p tcp -s $STAFF_NET -d $SERVER_IP --dport $SERVICE_PORT -m state --state NEW,ESTABLISHED -j ACCEPT

# =========================================================================
# c. Block all other inbound traffic access to that specific service port
# =========================================================================
print_status "Applying Rule C: Dropping all other inbound traffic..."
iptables -A INPUT -p tcp -d $SERVER_IP --dport $SERVICE_PORT -j DROP

print_status "Firewall rules applied successfully!"

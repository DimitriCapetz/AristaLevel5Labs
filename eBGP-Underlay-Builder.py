from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
import yaml
config = """
spine1-DC1:
  asn: 65100
  interfaces:
    loopback0: 
      ipv4: 192.168.101.101
      mask: 32
    Ethernet2:
      ipv4: 192.168.103.1
      mask: 31
    Ethernet3:
      ipv4: 192.168.103.7
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.13
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.19
      mask: 31
    Ethernet6: 
      ipv4: 192.168.103.25
      mask: 31
    Ethernet7: 
      ipv4: 192.168.103.31
      mask: 31
spine2-DC1:
  asn: 65100
  interfaces:
    loopback0: 
      ipv4: 192.168.101.102
      mask: 32
    Ethernet2:
      ipv4: 192.168.103.3
      mask: 31
    Ethernet3:
      ipv4: 192.168.103.9
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.15
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.21
      mask: 31
    Ethernet6: 
      ipv4: 192.168.103.27
      mask: 31
    Ethernet7: 
      ipv4: 192.168.103.33
      mask: 31
spine3-DC1:
  asn: 65100
  interfaces:
    loopback0: 
      ipv4: 192.168.101.103
      mask: 32
    Ethernet2:
      ipv4: 192.168.103.5
      mask: 31
    Ethernet3:
      ipv4: 192.168.103.11
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.17
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.23
      mask: 31
    Ethernet6: 
      ipv4: 192.168.103.29
      mask: 31
    Ethernet7: 
      ipv4: 192.168.103.35
      mask: 31
leaf1-DC1:
  asn: 65101
  interfaces:
    loopback0: 
      ipv4: 192.168.101.11
      mask: 32
    loopback1: 
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.0
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.2
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.4
      mask: 31
leaf2-DC1:
  asn: 65101
  interfaces:
    loopback0: 
      ipv4: 192.168.101.12
      mask: 32
    loopback1: 
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.6
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.8
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.10
      mask: 31
leaf3-DC1:
  asn: 65102
  interfaces:
    loopback0: 
      ipv4: 192.168.101.13
      mask: 32
    loopback1: 
      ipv4: 192.168.102.13
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.12
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.14
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.16
      mask: 31
leaf4-DC1:
  asn: 65102
  interfaces:
    loopback0: 
      ipv4: 192.168.101.14
      mask: 32
    loopback1: 
      ipv4: 192.168.102.13
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.18
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.20
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.22
      mask: 31
borderleaf1-DC1:
  asn: 65103
  interfaces:
    loopback0: 
      ipv4: 192.168.101.21
      mask: 32
    loopback1: 
      ipv4: 192.168.102.21
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.24
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.26
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.28
      mask: 31
    Ethernet12: 
      ipv4: 192.168.254.0
      mask: 31
borderleaf2-DC1:
  asn: 65103
  interfaces:
    loopback0: 
      ipv4: 192.168.101.22
      mask: 32
    loopback1: 
      ipv4: 192.168.102.21
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.30
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.32
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.34
      mask: 31
    Ethernet12: 
      ipv4: 192.168.254.2
      mask: 31
spine1-DC2:
  asn: 65200
  interfaces:
    loopback0: 
      ipv4: 192.168.201.101
      mask: 32
    Ethernet2:
      ipv4: 192.168.203.1
      mask: 31
    Ethernet3:
      ipv4: 192.168.203.7
      mask: 31
    Ethernet4:
      ipv4: 192.168.203.13
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.19
      mask: 31
    Ethernet6: 
      ipv4: 192.168.203.25
      mask: 31
    Ethernet7: 
      ipv4: 192.168.203.31
      mask: 31
spine2-DC2:
  asn: 65200
  interfaces:
    loopback0: 
      ipv4: 192.168.201.102
      mask: 32
    Ethernet2:
      ipv4: 192.168.203.3
      mask: 31
    Ethernet3:
      ipv4: 192.168.203.9
      mask: 31
    Ethernet4:
      ipv4: 192.168.203.15
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.21
      mask: 31
    Ethernet6: 
      ipv4: 192.168.203.27
      mask: 31
    Ethernet7: 
      ipv4: 192.168.203.33
      mask: 31
spine3-DC2:
  asn: 65200
  interfaces:
    loopback0: 
      ipv4: 192.168.201.103
      mask: 32
    Ethernet2:
      ipv4: 192.168.203.5
      mask: 31
    Ethernet3:
      ipv4: 192.168.203.11
      mask: 31
    Ethernet4:
      ipv4: 192.168.203.17
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.23
      mask: 31
    Ethernet6: 
      ipv4: 192.168.203.29
      mask: 31
    Ethernet7: 
      ipv4: 192.168.203.35
      mask: 31
leaf1-DC2:
  asn: 65201
  interfaces:
    loopback0: 
      ipv4: 192.168.201.11
      mask: 32
    loopback1: 
      ipv4: 192.168.202.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.0
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.2
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.4
      mask: 31
leaf2-DC2:
  asn: 65201
  interfaces:
    loopback0: 
      ipv4: 192.168.201.12
      mask: 32
    loopback1: 
      ipv4: 192.168.202.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.6
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.8
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.10
      mask: 31
leaf3-DC2:
  asn: 65202
  interfaces:
    loopback0: 
      ipv4: 192.168.201.13
      mask: 32
    loopback1: 
      ipv4: 192.168.202.13
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.12
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.14
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.16
      mask: 31
leaf4-DC2:
  asn: 65202
  interfaces:
    loopback0: 
      ipv4: 192.168.201.14
      mask: 32
    loopback1: 
      ipv4: 192.168.202.13
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.18
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.20
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.22
      mask: 31
borderleaf1-DC2:
  asn: 65203
  interfaces:
    loopback0: 
      ipv4: 192.168.201.21
      mask: 32
    loopback1: 
      ipv4: 192.168.202.21
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.24
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.26
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.28
      mask: 31
    Ethernet12: 
      ipv4: 192.168.254.4
      mask: 31
borderleaf2-DC2:
  asn: 65203
  interfaces:
    loopback0: 
      ipv4: 192.168.201.22
      mask: 32
    loopback1: 
      ipv4: 192.168.202.21
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.30
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.32
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.34
      mask: 31
    Ethernet12: 
      ipv4: 192.168.254.6
      mask: 31
"""
switches = yaml.load(config)
print "service routing protocols model multi-agent\n!"

for iface in switches[hostname]['interfaces']:
    #Iterate through all interfaces using iface variable as the incrementing index
    print("interface %s") % iface
    #Pull variables into easier to use variables
    ip = switches[hostname]['interfaces'][iface]['ipv4']
    mask = switches[hostname]['interfaces'][iface]['mask']
    if "Ethernet" in iface:
        print "   mtu 9214\n   no switchport"
    print("   ip address %s/%s\n!") % (ip, mask)

print "ip prefix-list LOOPBACK"
if "DC1" in hostname:
  print "   seq 10 permit 192.168.101.0/24 eq 32"
  print "   seq 20 permit 192.168.102.0/24 eq 32\n!"
else:
  print "   seq 10 permit 192.168.201.0/24 eq 32"
  print "   seq 20 permit 192.168.202.0/24 eq 32\n!"
print "route-map LOOPBACK permit 10"
print "   match ip address prefix-list LOOPBACK\n!"
if "spine" in hostname:
   print "peer-filter LEAF-AS-RANGE"
   print "   10 match as-range 65000-65535 result accept\n!"

print "router bgp {asn}".format(asn = switches[hostname]["asn"])
print "   router-id {id}".format(id = switches[hostname]["interfaces"]["loopback0"]["ipv4"])
print "   no bgp default ipv4-unicast"
print "   maximum-paths 3"
print "   distance bgp 20 200 200"
if "spine" in hostname:
  if "DC1" in hostname:
    print "   bgp listen range 192.168.103.0/24 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE"
  else:
    print "   bgp listen range 192.168.203.0/24 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE"
  print "   neighbor LEAF_Underlay peer group"
  print "   neighbor LEAF_Underlay send-community standard extended"
  print "   neighbor LEAF_Underlay maximum-routes 12000"
if "border" in hostname:
  print "   neighbor DCI peer group"
  print "   neighbor DCI remote-as 65000"
  print "   neighbor DCI send-community standard extended"
  print "   neighbor DCI maximum-routes 12000"
if "leaf" in hostname:
  print "   neighbor LEAF_Peer peer group"
  print "   neighbor LEAF_Peer remote-as {asn}".format(asn = switches[hostname]["asn"])
  print "   neighbor LEAF_Peer next-hop-self"
  print "   neighbor LEAF_Peer maximum-routes 12000"
  print "   neighbor SPINE_Underlay peer group"
  if "DC1" in hostname:
    print "   neighbor SPINE_Underlay remote-as 65100"
  else:
    print "   neighbor SPINE_Underlay remote-as 65200"
  print "   neighbor SPINE_Underlay send-community standard extended"
  print "   neighbor SPINE_Underlay maximum-routes 12000"
  for iface in switches[hostname]["interfaces"]:
    if "Ethernet12" in iface:
      octets = switches[hostname]["interfaces"][iface]["ipv4"].split(".")
      neighbor_octets = [octets[0], octets[1], octets[2], str(int(octets[3]) + 1)]
      neighbor_ip = ".".join(neighbor_octets)
      print "   neighbor {ip} peer group DCI".format(ip = neighbor_ip)
    elif "Ethernet" in iface:
      octets = switches[hostname]["interfaces"][iface]["ipv4"].split(".")
      neighbor_octets = [octets[0], octets[1], octets[2], str(int(octets[3]) + 1)]
      neighbor_ip = ".".join(neighbor_octets)
      print "   neighbor {ip} peer group SPINE_Underlay".format(ip = neighbor_ip)
  if "leaf1" in hostname or "leaf3" in hostname:
    print "   neighbor 192.168.255.2 peer group LEAF_Peer"
  else:
    print "   neighbor 192.168.255.1 peer group LEAF_Peer"
print "   redistribute connected route-map LOOPBACK\n   !"
print "   address-family ipv4"
if "leaf" in hostname:
  print "      neighbor SPINE_Underlay activate"
  print "      neighbor LEAF_Peer activate"
else:
  print "      neighbor LEAF_Underlay activate"
if "border" in hostname:
  print "      neighbor DCI activate"
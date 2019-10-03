import os, re
from firebase import firebase

full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]

final_results = [{**i, **{'LAN_IP':i['LAN_IP'][1:-1]}} for i in final_results]
ip=[]

for i in final_results:
    if "MAC_ADDRESS" in i:
       
        ip.append(i['LAN_IP'])
        
ip1=ip[0]
ip1 = ip1[:-1]
IP = []
MAC = []
device = []

final = os.popen('nmap -sn ' + ip1 + '0/24')

result = final.read()
length = len(result.split('\n'))
l = result.split('\n')
l = l[3:-2]
for i in range(len(l)):
	if i%3 == 1:
		l[i] = (l[i])[21:]
for i in range(len(l)):
	if i%3 == 0:
		MAC.append((l[i])[:30])
	if i%3 == 1:
		IP.append(l[i])
	if i%3 == 0:
		device.append((l[i])[32:-1])

firebase = firebase.FirebaseApplication("https://autobot-32ad5.firebaseio.com/", None)
i=0

while i < len(IP):
    lastIndexOfDot = IP[i].rindex('.')
    lastIndexOfDot = lastIndexOfDot + 1
    deviceIP = IP[i]
    headerNode = "Device " + deviceIP[lastIndexOfDot:]
    firebase.put('mywish',headerNode,{'Device Name': device[i], 'MAC':MAC[i],'Device IP':IP[i]})
    i = i+1


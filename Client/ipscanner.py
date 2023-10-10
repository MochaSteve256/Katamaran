import subprocess
import socket
import platform

#this code probably doesn't work because ping is weird and whois is doing shit as well

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

netIP = get_ip()
dots = 0
counter = 0

def remove_at(i, s):
    return s[:i]

for letter in netIP:
    print(netIP)
    print(dots)
    if letter == ".":
        dots += 1
    if dots == 3:
        netIP = remove_at(counter, netIP)
    counter += 1
netIP += (".")
print(netIP)
ips = []
param = '-n' if platform.system().lower()=='windows' else '-c'
paran = "-c 1"
for ping in range(1, 254):
	address = netIP + str(ping)
	res = subprocess.call(['ping', param, "1", address])
	if res == 0:
		print( "ping to", address, "OK")
		ips.append(address)
	else:
		print("ping to", address, "failed!")
hosts = []
for ip in ips:
    hosts.append(subprocess.call("whois64 -v -nobanner ", ip))
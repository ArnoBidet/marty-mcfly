class IpFinder:

    def __init__(self):
        self.json_active_hosts = []
        self.json_inactive_hosts = []

    def getIpLists(self,networkIp):
        import subprocess
        import ipaddress
        import json

        network = ipaddress.ip_network(networkIp)
        hosts = network.hosts()
        active_hosts = {"active_ip_addrs": []}
        inactive_hosts = {"inactive_ip_addrs": []}

        def pingda(ip_addr):
            try:
                subprocess.check_output(["ping", "-c", "1", ip_addr])
                active_hosts["active_ip_addrs"].append(ip_addr)
            except:
                inactive_hosts["inactive_ip_addrs"].append(ip_addr)

        for ip in hosts:
            pingda(str(ip))

        json_active_hosts = json.dumps(active_hosts, indent=1)
        json_inactive_hosts = json.dumps(inactive_hosts, indent=1)

        self.json_active_hosts = json_active_hosts
        self.json_inactive_hosts = json_inactive_hosts

    def testPorts(self):
        import netifaces

        interfaces = netifaces.interfaces()
        print(interfaces)
        for i in range(len(interfaces)):
            print("{i} :".format(i=i))
            try:
                addrs = netifaces.ifaddresses(interfaces[i])
                print(addrs[netifaces.AF_INET][0])
            except:
                print("error {i}".format(i=i))
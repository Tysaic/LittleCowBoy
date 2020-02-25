from modules.local_info import *

list_ports = ('80', '22')
if __name__ == '__main__':
    ip = 'localhost'
    port = 80
    for x in list_ports:
        print(scan_host_manually(ip, int(x) ) )

    print(nmap_scan_host(ip, list_ports))


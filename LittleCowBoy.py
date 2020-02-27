from modules.local_info import *

list_ports = ('80', '22')
if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 80
    scan = Scanner(ip, port)
    """
    print("Machine Info: ", Scanner.get_machine_info())
    print(scan.scan_host_manually() )
    list_nmap = scan.basic_nmap_scan()
    print(list_nmap)
    print(Scanner("google.com").dns_nmap_scan())
    print(scan.os_detection_nmap_scan())
    """
    print(scan.scanning_techniques())

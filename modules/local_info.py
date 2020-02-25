import platform
import requests
import socket
import nmap

def get_machine_info():
    data = dict()
    data['machine'] = platform.machine()
    data['version'] = platform.version()
    data['platform'] = platform.platform()
    data['uname'] = platform.uname()
    data['system'] = platform.system()
    data['processor'] = platform.processor()
    return data

def scan_host_manually(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        code = sock.connect_ex((ip, port))
        if code == 0:
            return True
        else:
            return False
    except:
        return False
    finally:
        sock.close()

def nmap_scan_host(host, ports):

    nm = nmap.PortScanner()
    flag = ' '
    ports = flag.join(ports)
    nm.scan(host, arguments='-n -sP -PE -PA{}'.format(ports))
    print(nm.all_hosts())

import platform
import requests
import socket

def get_machine_info():
    data = dict()
    data['machine'] = platform.machine()
    data['version'] = platform.version()
    data['platform'] = platform.platform()
    data['uname'] = platform.uname()
    data['system'] = platform.system()
    data['processor'] = platform.processor()
    return data

def get_localhost_info():
    data = dict()
    list_port = list()
    data['ip'] = requests.get('https://api.ipify.org').text
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((data['ip'], port))
            if result == 0:
                list_port.append(port)
            sock.close()
    except socket.error:
        print("Couldn't connect to server")
    finally:
        data['ports'] = list_port
    return data 


import platform
import socket
import nmap3
import json


class Scanner:
    def __init__(self, host, port=80):
        self.nm = nmap3.Nmap()
        self.nm_scan_tech = nmap3.NmapScanTechniques()
        self.host = host
        self.port = port
    
    @classmethod
    def get_machine_info(cls):
        data = dict()
        data['machine'] = platform.machine()
        data['version'] = platform.version()
        data['platform'] = platform.platform()
        data['uname'] = platform.uname()
        data['system'] = platform.system()
        data['processor'] = platform.processor()
        return data

    def scan_host_manually(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            code = sock.connect_ex((self.ip, self.port))
            if code == 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            sock.close()

    def basic_nmap_scan(self):
        results = self.nm.scan_top_ports(self.host)
        return results

    def dns_nmap_scan(self):
        results = self.nm.nmap_dns_brute_script(self.host)
        return results

    def os_detection_nmap_scan(self):
        result = self.nm.nmap_os_detection(self.host)
        return result

    def identify_service_version_detection(self):
        result = self.nm.nmap_version_detection(self.host)
        return result
    def scanning_techniques(self):
        return self.nm_scan_tech.nmap_fin_scan(self.host)
        

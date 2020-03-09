import platform
import socket
import nmap3

class Scanner:
    """
    Scanner class has several functions to scan local and external
    internet service, from basic tools until advanced
    """
    def __init__(self, host, port=80):
        """
        By default the port to scan is 80,
        because it's the web port by default
        """
        self.nm = nmap3.Nmap()
        self.nm_scan_tech = nmap3.NmapScanTechniques()
        self.host = host
        self.port = port
    
    #@classmethod
    @staticmethod
    def get_machine_info():
        """
        Static method to get info local machine,
        would be initialize without create an instance of
        itself.
        """
        data = dict()
        data['machine'] = platform.machine()
        data['version'] = platform.version()
        data['platform'] = platform.platform()
        data['uname'] = platform.uname()
        data['system'] = platform.system()
        data['processor'] = platform.processor()
        return data

    def scan_host_manually(self):
        """
        Scan an host manually.
        Returning if the host's port is open.
        """
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
        """
        Return the open ports of a host, but the port limit is short.
        """
        results = self.nm.scan_top_ports(self.host)
        return results

    def dns_nmap_scan(self):
        """
        Scanning dns host, return where the host is.
        """
        results = self.nm.nmap_dns_brute_script(self.host)
        return results

    def os_detection_nmap_scan(self):
        """
        Return os host information as operating system name, version, patch, so on.
        """
        result = self.nm.nmap_os_detection(self.host)
        return result

    def identify_service_version_detection(self):
        """
        Return service detected by the scan
        """
        result = self.nm.nmap_version_detection(self.host)
        return result
    def scanning_techniques(self):
        """
        Return Scanning techniques
        """
        return self.nm_scan_tech.nmap_fin_scan(self.host)

    def printing_info(self):
        basic_nmap = self.basic_nmap_scan()
        list_data = list()
        data = dict()
        list_data.append({'os':self.os_detection_nmap_scan()[0]["name"]})
        for b in basic_nmap:
            data["name"] = b["service"]["name"]
            data["port"] = b["port"]
            data["protocol"] = b["protocol"]
            data["state"] = b["state"]
            list_data.append(data)
        return list_data
        

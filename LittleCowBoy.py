from modules.scanner import *

list_ports = ('80', '22')
if __name__ == '__main__':
    #host = '127.0.0.1'
    host = 'www.procure.cl'
    port = 80
    scan = Scanner(host, port)
    scan.printing_basic_info()

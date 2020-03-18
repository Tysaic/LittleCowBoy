from modules.scanner import *
from modules.security_files import security_files
list_ports = ('80', '22')
if __name__ == '__main__':
    """
    #host = '127.0.0.1'
    host = 'www.procure.cl'
    port = 80
    scan = Scanner(host, port)
    scan.printing_basic_info()
    """
#    decrypt_file("data.txt.aes", "root1234")
#    security_files("data.txt", "nvim.pdf", "root1234").hide_file_on_img("Vim.png", "data.txt")
    print( security_files("data.txt", "nvim.pdf", "root1234").unhide_file_on_img("Vim.png") )

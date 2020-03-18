import pyAesCrypt
import os
import stegano 
bufferSize = 1024 * 1024


class security_files:
    def __init__(self, filename, target_filename, password):
        self.filename = filename
        self.target_filename = target_filename
        self.password = password
        self.bufferSize = 1024*1024

    def encrypt_file(self):
        """
        Encrypt File
        """
        pyAesCrypt.encryptFile(self.filename, str('{}.aes').format(self.filename), self.password, self.bufferSize)

    def decrypt_file(self):
        """
        Decrypt File
        """
        pyAesCrypt.decryptFile(filename, os.path.splitext(filename)[0], password, self.bufferSize)

    #HIDDEN TEXT IN IMAGES
    @classmethod
    def hide_file_on_img(cls,filename, target):
       hide_img = stegano.lsb.hide(filename, target)
       hide_img.save(filename)

    @classmethod
    def unhide_file_on_img(cls,filename):
        return stegano.lsb.reveal(filename)

    #LACK HIDDEN FILES OR ZIPS IN IMAGE

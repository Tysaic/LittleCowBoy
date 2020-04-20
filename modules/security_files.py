import pyAesCrypt
import os
import stegano 
import cv2
import numpy as np


def data_to_bin(data):
    """Converting data to binary format as string"""

    if isinstance(data, str):
        return (''.join([format(ord(i), "08b") for i in data]))

    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]

    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    
    else:
        raise TypeError("Type not supported")


class security_files:
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password
        self.bufferSize = 1024*1024

    def encrypt_file(self):
        """
        Encrypt File
        """
        pyAesCrypt.encryptFile(self.filename,
                str('{}.aes').format(self.filename),
                self.password, self.bufferSize)
        print("Funciono")

    def decrypt_file(self):
        """
        Decrypt File
        """
        pyAesCrypt.decryptFile(self.filename,
                os.path.splitext(self.filename)[0],
                self.password, self.bufferSize)

    #HIDDEN TEXT IN IMAGES
    @classmethod
    def hide_file_on_img(cls,filename, target):
        """
        Hidding file on Image
        """
        hide_img = stegano.lsb.hide(filename, target)
        hide_img.save(filename)

    @classmethod
    def unhide_file_on_img(cls,filename):
        """
        UnHidding file on immage
        """
        return stegano.lsb.reveal(filename)

    #LACK HIDDEN FILES OR ZIPS IN IMAGE

    @classmethod
    def encode_text_on_img(self, img, secret_data):
        """
        Hidding text on image
        """
        image = cv2.imread(img)

        n_bytes = image.shape[0] * image.shape[1] * 3//8

        print("[*] Maximum bytes to encode: ", n_bytes)

        if len(secret_data) > n_bytes:
            raise ValueError("[!] Insufficient bytes, need bigger image or less data")

        print("[*] Encoding data...")

        secret_data += "====="
        data_index = 0

        binary_secret_data = data_to_bin(secret_data)

        data_len = len(binary_secret_data)

        for row in image:
            for pixel in row:

                r, g, b = data_to_bin(pixel)

                if data_index < data_len:
                    pixel[0] = int(r[:-2] + binary_secret_data[data_index], 2)
                    data_index += 1
                
                if data_index < data_len:

                    pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                    data_index += 1

                if data_index < data_len:

                    pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                if data_index >= data_len:
                    break
        print("[+] Encode Success")
        return image

    def decode_text_on_img(self, img):
        """
        Decode Text on image
        """
        print("[+] Decoding...")
        image = cv2.imread(img)
        binary_data = ""

        for row in image:
            for pixel in row:
                r, g, b = data_to_bin(pixel)
                print(r, g ,b)
                binary_data += r[-1]
                binary_data += g[-1]
                binary_data += b[-1]

        all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "=====":
                break
        return decoded_data[:-5]
#https://www.thepythoncode.com/article/hide-secret-data-in-images-using-steganography-python

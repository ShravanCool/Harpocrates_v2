from Crypto.Cipher import AES
import io
import PIL.Image
import os

# Private Stuff, should not be hardcoded
key = b'Key of length 16'
iv = b'ivb of length 16'

# Encrypting Image
def encrypt_image(file_name):

    global key, iv

    input_file = open(file_name, 'rb')
    input_data = input_file.read()
    input_file.close()

    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    enc_file = open(file_name + ".enc", 'wb')
    enc_file.write(enc_data)
    enc_file.close()

# Decrypting Image
def decrypt_image(file_name):

    global key, iv

    enc_file2 = open(file_name, 'rb')
    enc_data2 = enc_file2.read()
    enc_file2.close()

    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    plain_data = cfb_decipher.decrypt(enc_data2)

    image_stream = io.BytesIO(plain_data)
    image_file = PIL.Image.open(image_stream)

    output_path = 'output_'

    if '.jpg' in file_name:
        image_file.save(output_path + file_name[:-8] + '.jpg')
    elif '.png' in file_name:
        image_file.save(output_path + file_name[:-8] + '.png')

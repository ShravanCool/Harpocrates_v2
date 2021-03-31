from Crypto.Cipher import Salsa20
import io
import PIL.Image
import os

# Private Stuff, should not be hardcoded
key = b'*Thirty-two byte (256 bits) key*'

# Encrypting Image
def encrypt_image(file_name):

    global key

    input_file = open(file_name, 'rb')
    input_data = input_file.read()
    input_file.close()

    cipher = Salsa20.new(key=key)
    enc_data = cipher.nonce + cipher.encrypt(input_data)

    enc_file = open(file_name + ".enc", 'wb')
    enc_file.write(enc_data)
    enc_file.close()

# Decrypting Image
def decrypt_image(file_name):

    global key, iv

    enc_file2 = open(file_name, 'rb')
    enc_data2 = enc_file2.read()
    enc_file2.close()

    msg_nonce = enc_data2[:8]
    rem_msg = enc_data2[8:]

    decipher = Salsa20.new(key=key, nonce=msg_nonce)
    plain_data = decipher.decrypt(rem_msg)

    image_stream = io.BytesIO(plain_data)
    image_file = PIL.Image.open(image_stream)

    if '.jpg' in file_name:
        image_file.save(file_name[:-8] + '.jpg')
    elif '.png' in file_name:
        image_file.save(file_name[:-8] + '.png')


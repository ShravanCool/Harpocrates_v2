import AES

def main():

    file_name = 'pic1.jpg'
    print('Encrypting file...')
    AES.encrypt_image(file_name)
    print('Encrypted...')
    print('Decrypting...')
    AES.decrypt_image(file_name+'.enc')
    print('Decrypted')


main()

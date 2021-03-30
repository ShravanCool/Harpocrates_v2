import Blowfish

def main():

    file_name = 'pic1.jpg'
    print('Encrypting file...')
    Blowfish.encrypt_image(file_name)
    print('Encrypted...')
    print('Decrypting...')
    Blowfish.decrypt_image(file_name+'.enc')
    print('Decrypted')


main()


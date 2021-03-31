import Salsa20

def main():

    file_name = 'pic1.jpg'
    print('Encrypting file...')
    Salsa20.encrypt_image(file_name)
    print('Encrypted...')
    print('Decrypting...')
    Salsa20.decrypt_image(file_name+'.enc')
    print('Decrypted')


main()


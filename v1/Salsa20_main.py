import Salsa20
import TtIED
import time

def main():

    infile = 'message.txt'
    img_file = 'output.png'
    outfile = 'out_message.txt'

    print('Encoding...')
    start = time.time()
    TtIED.encode(infile, img_file)
    Salsa20.encrypt_image(img_file)
    end = time.time()
    print('Encrypting...')

    print('Encryption time: ', end - start)

    print('Decrypting...')
    start = time.time()
    Salsa20.decrypt_image(img_file + '.enc')
    TtIED.decode(img_file, outfile)
    end = time.time()
    print('Decoding...')

    print('Decryption time: ', end - start)

main()


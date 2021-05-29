import Blowfish
import TtIED
import time
import os, psutil

def main():

    infile = 'message.txt'
    img_file = 'output.png'
    outfile = 'out_message.txt'

    # with open('message.txt') as S:
        # print("Plaintext message:", S.read())

    # print('Encoding...')
    start = time.time()
    TtIED.encode(infile, img_file)
    Blowfish.encrypt_image(img_file)
    end = time.time()
    # print('Encrypting...')

    # print('Encryption time: ', (end - start) * 1000)

    # print('Decrypting...')
    start = time.time()
    Blowfish.decrypt_image(img_file + '.enc')
    TtIED.decode(img_file, outfile)
    end = time.time()
    # print('Decoding...')

    # print('Decryption time: ', (end - start) * 1000)

    # with open('out_message.txt') as S:
        # print("Decrypted message:", S.read())

    # time.sleep(10000)
    process = psutil.Process(os.getpid())
    print("Memory in MB:", process.memory_info().rss / 1024 ** 2)

main()


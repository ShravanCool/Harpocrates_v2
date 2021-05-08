from PIL import Image
import numpy as np
import random

def encode(infile, outfile):
    arr = np.array([ord(s) for s in open(infile).read()])
    # print(arr)
    new_arr = []
    for i in arr:
        new_arr.append(random.randrange(0,255))
        new_arr.append(random.randrange(0,255))
        new_arr.append(i)

    bitPlanes = 3
    arrLen = len(new_arr)

    rowSize = int(np.ceil(np.sqrt(arrLen/bitPlanes)))
    pixelsNeeded = np.square(rowSize)
    # print(new_arr)
    # print(rowSize)
    # print(pixelsNeeded)

    while (len(new_arr)/bitPlanes) % 3 != 0:
        new_arr = np.append(new_arr, [0], 0)

    # print(new_arr)

    new_arr = np.pad(new_arr.reshape(-1), (0, int(
        pixelsNeeded - len(new_arr)/bitPlanes) * bitPlanes), 'constant')

    # print(new_arr)
    new_arr = new_arr.reshape((rowSize, rowSize, bitPlanes))
    # print(new_arr)


    Image.fromarray(np.uint8(new_arr)).save(outfile)

def decode(infile, outfile):
    arr = np.array(Image.open(infile).convert('RGB'),)

    arr = arr.reshape(-1)
    bits = arr[arr != 0]

    string = ''.join([chr(b) for b in bits[2::3]])
    # print(string)
    
    with open(outfile, 'w') as f:
        f.write(string)

# def main():
    # infile1 = 'message.txt'
    # outfile1 = 'output.png' 


    # infile2 = 'output.png' 
    # outfile2 = 'message1.txt'

    # encode(infile1, outfile1)
    # print("Encoded!!")
    # decode(infile2, outfile2)
    # print('Decoded!!')

# main()

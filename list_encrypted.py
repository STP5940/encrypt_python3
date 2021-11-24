import os
from wcmatch import glob

filename_encrypt = 'D:/encrypt_python3/.list_encrypted.txt'
fnameclear_encrypt = open(filename_encrypt, "w", encoding="utf-8")
fnameclear_encrypt.write('')
fnameclear_encrypt.close()

print("Scanning file encrypted...")

for root, dirs, files in os.walk("D:/"):

    if root.find("$RECYCLE.BIN") == -1:

        for file in files:
            if file.endswith((".stpdev")):
                print(os.path.join(root, file))
                f_encrypt = open(filename_encrypt, "a", encoding="utf-8")
                f_encrypt.write(os.path.join(root, file)+'|')
                f_encrypt.close()


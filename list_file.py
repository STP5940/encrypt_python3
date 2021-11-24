import os
from wcmatch import glob

filename = 'D:/encrypt_python3/.list_file.txt'
fnameclear = open(filename, "w", encoding="utf-8")
fnameclear.write('')
fnameclear.close()

for root, dirs, files in os.walk("D:/"):

    if root.find("$RECYCLE.BIN") == -1:

        for file in files:
            if file.upper().endswith((".PDF", ".PNG", ".JPG", ".JPGE", ".WEBP", ".GIF", ".SVG", ".JFIF", ".JPEG")):
                print(os.path.join(root, file))
                f = open(filename, "a", encoding="utf-8")
                f.write(os.path.join(root, file)+'|')
                f.close()


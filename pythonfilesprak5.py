import os

print(os.getcwd())


# change directory
os.chdir('/media/aini/504EAA914EAA6F80/python-projek')

print(os.getcwd())
os.mkdir('test')

import os

# melihat isi folder saat ini
print(os.listdir())

# rename directory
if os.path.exists("test"):
    os.rename("test", "new_one")
    print("Folder berhasil diganti nama")
else:
    print("Folder test tidak ditemukan")

# melihat hasil perubahan
print(os.listdir())

# delete "myfile.txt" file
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File berhasil dihapus")
else:
    print("File tidak ditemukan")


import os
import shutil

# membuat folder contoh
if not os.path.exists("mydir"):
    os.mkdir("mydir")

print("Isi folder saat ini:")
print(os.listdir())

# menghapus folder kosong
os.rmdir("mydir")

print("Folder mydir berhasil dihapus")
import os

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

file=findfile("20221205.py","/")
print(f"{file}")
import os

def headers(directory="./"):
    files = os.listdir(directory)
    return filter(lambda f: f.endswith(".h"), files)

def bodies(directory="./"):
    files = os.listdir(directory)
    return filter(lambda f: f.endswith(".m"), files)

def allFiles(directory="./"):
    files = os.listdir(directory)
    return filter(lambda f: f.endswith(".m") or f.endswith(".h"), files)

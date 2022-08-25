import os

source = r"C:/Users/namra/Downloads/newtext2.txt"
destination = r"C:/Users/namra/Downloads/test2.txt"

os.rename(source,destination)
print(source, destination)
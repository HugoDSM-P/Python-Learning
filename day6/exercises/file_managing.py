import os
from pathlib import Path

file = open("test.txt")
print(file.readline())
file.close()

file = open("test.txt")
print(file.readlines())
file.close()

file = open("test.txt")
print(file.readlines()[1])
file.close()

file = open("test1.txt", "w")
file.write("New text line\n")
file.close()

file = open("test1.txt", "a")
file.write("New log in\n")
file.close()

file = open("test1.txt")
print(file.readlines())
file.close()

file = open("test1.txt", "a")
last_register = ["Jane\t", "20/20/2000\t", "8:30AM\t", "Successful"]
file.writelines(last_register)
file.close()

home = Path.home()

testpath = Path("Pythontest", "day6", "testpath.py")

def open_read(open_file):
    file = open(open_file)
    print(file.read())
    file.close()
open_read("test1.txt")

def overwrite(ofile):
    file = open(ofile, "r")
    print(file.read())
    file.close()
    file = open(ofile, "w")
    file.write("Content erased")
    file.close()
    file = open(ofile, "r")
    print(file.read())
    file.close()
overwrite("erasefile.txt")

def error_register(register):
    file = open(register, "a")
    file.write("\nA fatal error has been registered")
    file.close()
error_register("test1.txt")
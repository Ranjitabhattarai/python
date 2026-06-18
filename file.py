#f = open ("myfile.txt", "x")
with open("demofile.txt", "w")as f:
    f.write("woops! I have deleted the context....")

with open ("demofile.txt", "r")as f:
    print(f.read())

with open ("demofile.txt", "a")as f:
    f.write("these is a hello world")

#to remove the file 
import os
os.remove("demofile.txt")
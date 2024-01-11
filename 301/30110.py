# Using file handling commands, 
import os

#create a Python script that creates a new .txt file, 
with open("test30110.txt", "w") as testtxt:

#appends three lines, 
    testtxt.write("Line 0\nLine 1\nLine 2\nLine 3")
    testtxt.close()

#prints to the screen the first line, 
with open("test30110.txt", "r") as testtxt:
    print(testtxt.readline())
    testtxt.close()

#then deletes the .txt file.
os.remove("test30110.txt")
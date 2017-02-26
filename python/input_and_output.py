#########################################
#       Doing Input and Output          #
#########################################

# Uses 'input()' which sends text to the console and returns whatever the user writes.
# The name of the variable doesn't need to be 'inputVariable', that's just done for clarity.
inputVariable = input("What's your name? ")
# Interesting note on the print function: Normally prints a newline, but 'end' overrides that. This is fixed using typical escape character syntax.
print("Hello ", inputVariable, end="!\n")

# As for integers, etc-- because of the way python does comparisons, it's pretty lenient. We just need to make it be in 'int mode':
userInt = mode=int(input("Give a number! "))
if userInt == 1:
        print("That number is 1!")
else:
        print("That number is not 1!")

# To do anything with files, we need to use 'open()' to open a file.
# A variable is assigned the object with open. The first paramater is the path to the file, the second paramater decides what to do with it.
# 'r' is for reading, 'w' is for writing, 'a' is for appending, 'r+' is for reading and writing
myFile = open("./readFile","w")

# To do the actual writing, use the write() method in the file object using typical object.method() format. Doesn't auto-newline, so add a \n.
myFile.write("Hello World!\n")
myFile.write("This is a second line!\n")
myFile.write("This is a third...\n")
myFile.write("And this is the fourth.\n")

myFile = open("./readFile","r")
# Now to do some reading. object.read() returns the contents of the file, which is being printed.
print(myFile.read())

# Of course, we don't always want everything. Giving read() a number means it will get that number of characters.
# print() can also output to a variable, as is done here:
output = myFile.read(5)
# Now we're done with the object, so for efficiency, let's close it:
myFile.close()

#########################################################
#                                                       #
#               MATH IN PYTHON AND STUFF                #
#                                                       #
#########################################################
import math ## We need to import 'math' to use the math library (so this gives us access to any math.(function) things)
## The Basics:
# Making variables
a=1
b=2
c=3
d=4

# Doing math and putting the output in a variable
e=a+b           # Addition
f=b-c           # Subtraction
g=f/d           # Division
gg = (a*b) / 5  # Will return a float. Also, typical order of operations with parenthesis is a thing.
h=e*f           # Multiplication
i=b//c          # Integer division

## Using the math library that we had to import earlier:
# Python follows the IEEE 754 standard (just like C and Java), and works as expected.
# By using the 'math' library, we get access to many more complex computations.
# The format for libraries is the usual deal: library.method() to call a method in a library.
# A full detail of the library can be found here: https://docs.python.org/2/library/math.html but I've written up the important stuff for us here.

# Good to know these, not sure if it will be needed
j=math.log(2,4) # Logarithm, in x,base format. Base can be ommitted to default to e.
k=math.pow(3,4) # Power, in firstNumber^secondNumber format (so in this case, 3^4)

# Also does trig/rad to deg conversion, we'll be needing some of this for vector math.
l=math.degrees((3*math.pi)/2)   # Finding degrees from a radian input. Note usage of 'math.pi'-- that's how pi is used as a constant.
m=math.cos(math.pi)             # Using cosine. math.sin(), math.tan(), math.acos(), etc, also exist
n=math.radians(180)             # Finding radians from a degree input.

# The math library also has some handy booleans
o=math.isinf(3) # Checks if the given number is infinite (positive or negative infinity will return true)
p=math.isnan(4) # Checks if the given number is NaN (Follows IEEE 754, returns true if it is NaN, false if actually a number)

## That's pretty much all the math that we need to worry about for now. Let's print it to the screen to check what the output really is.
## As a side note, the print method acts a lot like println() in other languages. It also acts differently in python 2 and 3.
## To see what I mean, try running this code using the python command and then using the python3 command.

print("a:                               ",a)
print("b:                               ",b)
print("c:                               ",c)
print("d:                               ",d)
print("e=a+b:                           ",e)
print("f=b-c:                           ",f)
print("g=f/d:                           ",g)
print("h=e*f:                           ",h)
print("i=b//c:                          ",i)
print("j=math.log(2,4):                 ",j)
print("k=math.pow(3,4):                 ",k)
print("l=math.degrees((3*math.pi)/2):   ",l)
print("m=math.cos(math.pi):             ",m)
print("n=math.radians(180):             ",n)
print("o=math.isinf(3):                 ",o)
print("p=math.isnan(4):                 ",p)

#########################################
#       Control Flow in Python          #
#########################################

# Python uses a different syntactical structure than most other languages, mainly in that it doesn't use brackets/parenthesis.
# Instead, note colon to show the end of the conditional, and the spacing to show the contents of the statement.
# The basic syntax is as follows:
# if BOOLEAN:
#       runs if true
# else:
#       runs if all else is false
#
# For example:

if 1==1:
        print("This runs if those things are equal!") # This is spaced such that it is inside the statement.
else:
        print("This runs if those things are not equal!")

print("This always gets run because it is outside the if statement!")



# Pretty typical symboloogy is used.
if 1 != 0:
        print("1!=0")
if 1==1:
        print("1==1")


# If you uncomment this, the code will fail. This is because 'true' and 'false' aren't the proper syntax.
#if true:
#       print("true!")
# To use booleans, use 'True' and 'False' with capitilization.
if True:
        print("true!")


# Python does the == differently than other oop languages. == checks if the values of objects are the same.
# To check if two variables point to the same object, use 'is'.
### Note that this is the opposite of other langauges! ###

# Variables that are objects in other languages (Strings, for example), don't have comparison issues in python.
testString = "stringhere"
if testString=="stringhere":
        print("Those are equal!")
else:
        print("Not equal!")

# Greater than/less than operators are a thing too
a=4
b=3
c=2
d=1

if a > b:
        print("a is greater than b!")

if d < c:
        print("d is less than c!")

if a >= a:
        print("a is greater than or equal to a!")

if b <= b:
        print("b is less than or equal to b!")

# Comparisons can be chained together too. Most languages would require ((1<2)&&(2<3)), but python takes 1<2<3:
if 1<2<3:
        print("1 is less than 2 and 2 is less than 3!")

# But you can still use and and or's for when that isn't an option:
if True and True:
        print("True and True is True!")

if True or False:
        print("True or False is True!")


# And you can negate things using 'not':
if not False:
        print("not false!")



## While and For loops also exist, using similar principles.
# Here's a while loop that happens to be acting like a traditional for loop:
a=0
while a < 5:
        print(a)
        a=a+1

# And here's an actual for loop. Note the usage of range(), which prints the full range of integers from first to second paramater.
# Something to note is that python does for loops differently  than other languages in that it cycles through a list. The loop ends when the list ends.
for variableHere in range(10, 15):
        print(variableHere)

# The actual step can also be spceified:
for foo in range(100, 500, 50):
        print(foo)

# Or don't use range at all, and recall that it's looking for a list to run through:
for letter in ["a","b","c","d"]:
        print(letter)

#############################
#   Using GPIO in Python    #
#############################
# This code sends power to GPIO pin 27, then turns it off after 2 seconds.
# This is done by writing a value of 'high' to the pin (which we can do because everything is a file).
# After waiting 2 seconds, we turn it off and the code is complete.


# We start by importing some libraries so we can use the functions they give us.
# 'time' is for the sleep function, 'os' is for checking if the file exists.
import time
import os

# Defining a method (called a function in Python).
# This takes a filename and the contents, and writes the contents to the file.
# It's the same thing as 'echo "contents" > filename' in the bash script version.
def writeFile(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

# In order to use the file, we need to make sure that it exists. If it is not a file, returns True
if not os.path.isfile("/sys/class/gpio/gpio27/direction"):
    # This code makes the file that we need in order to talk to the gpio pin 27.
    writeFile("/sys/class/gpio/export","27")

# Wait a second, just in case the file needs to be set up
time.sleep(0.1)

# Setting the pin mode to out so that can set the output
writeFile("/sys/class/gpio/gpio27/direction", "out")

# Setting the pin value to high, which makes it output a voltage
writeFile("sys/class/gpio/gpio27/value", "1")

# Waits 2 seconds. If we didn't do this, we wouldn't notice the LED turn on (it would be too quick!)
time.sleep(2)

# Now let's turn it off by setting the value to low (0).
writeFile("/sys/class/gpio/gpio27/value", "0")

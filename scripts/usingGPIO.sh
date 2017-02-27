#!/bin/bash

#################################################
#       Using GPIO Pins on the Raspberry Pi     #
#         Remember, EVERYTHING is a file!       #
#################################################

# This should be run as root, which is done by checking if the user ID is 0.
# If it is, user is root and that's fine. If not, complain and exit.
# We want to run it as root because of the file ownership.
# TODO: Add changing file ownership to 'control' for the gpio stuff to hex_firsttime.sh.
if["$EUID" -ne 0]
        then echo "This must be run as root!"
        exit
fi

# Echoing "27" returns 27, which is then piped into the gpio 'export' command. The command makes a file.
# The file that is created is corresponds to the gpio pin we want to use (in this case, 27).
echo "27" >/sys/class/gpio/export

# In order to be able to manipulate the output on the pin, we need to set it to 'out' mode.
# Note the same path as earlier, but now through the 'gpio27' that 'export' made and piping that output into 'direction'.
echo "out" >/sys/class/gpio/gpio27/direction

# Everything is now set up, so it's ready to be used.
# This for loop will turn the pin on, wait 1 second, then turn it off, 10 times.
for count in  {0..10}
do
        # To turn it on, we set the value to 1:
        echo "1" >/sys/class/gpio/gpio27/value

        # We want it to stay on for a bit, so sleep for 1 sec.
        # If we didn't add this delay, we would never be able to see it turn on because of how fast the pi is running.
        sleep 1

        # It has now been on for 1 second, so let's turn it off.
        echo "0" >/sys/class/gpio/gpio27/value
done

#!/bin/bash
## A lot of these commands need root, so let's check for that first:
if ["$EUID" -ne 0] # Checking to see if the user ID is not 0. This checks for root, as root has a user ID of 0.
  then echo "This needs root permissions! Run this command as root, either by changing user to root with 'su root' or by using 'sudo'." # Inform the user
  exit                                                                                                                                  # Exit the program
fi

## Now that we know we're root, we can move on to making sure everything is updated:
apt-get update                                    # Update makes sure that the Pi has up-to-date information on the repositories
apt-get --assume-yes upgrade                      # Upgrade does the actual upgrading of software, with --assume-yes making sure that there's less for the user to do
apt-get --assume-yes install hostapd              # Installs hostapd, allowing us to make the pi transmit on the antenna
apt-get --assume-yes install openssh-server       # Installs openssh-server, which allows us to open ssh on the pi. It may already be installed, but since we're using it, we may as well double-check.
apt-get --assume-yes install git                  # Should already have Git, but just to make sure

## We know we have the tools we'll need, so now we can start downloading things.
cd /                                                           # Changes directory to root so that it's all in one easy place. We'll clean it up later.
git clone https://github.com/thieraufc/WIT-Robotics-Hexacopter # Clones the code from the WIT-Robotics-Hexacopter repository on my account
cd /WIT-Robotics-Hexacopter/                                   # Since we went to / earlier, we know that the repo is here and we can cd to it.

## Now we have the config files. Let's put them where they belong.
## NOTE: ONLY 1 FILE EXISTS ATM, MORE COMING SOON. THIS IS WHERE THEY GO!
mv ./sshd_config /etc/ssh/sshd_config   # Moves the sshd_config file from earlier and moves it over to where it belongs.



useradd -m -p control                   	# Adds a user called 'control'
echo control:defaultpassword | chpasswd 	# Changes the password of 'control' to 'defaultpassword' by piping it into chpasswd
# passwd -l pi	 							# Locks the Pi user for security reasons

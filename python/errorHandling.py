#########################################
#       Error Handling in Python        #
#########################################

# Python uses try blocks.
try:
        print("Trying things!")
        # Raise can be used to manually throw an exception.
        # A full list of exception can be found at https://docs.python.org/2/library/exceptions.html
        # For the sake of example, we're raising an Import Error.
        raise ImportError("Oh no, Index Error!")
# Similar syntax to better languages, where this block runs if the error specified was caught, putting info in variable e.
except ImportError as e:
        # Do stuff here
        pass
        # I don't have anything to do here, so pass passes without doing things
# Or catch several errors with one block:
except (IndexError, IOError):
        pass

# This part is optional: If we want to run something only if the try runs properly, else is used.
# This won't run because we've had it through an error up top-- comment it out, and this will run.
else:
        print("Hey, everything worked!")

# 'finally' always runs. It's something that would be good to use in cleanup, like closing objects.
finally:
        print("try block is over!")

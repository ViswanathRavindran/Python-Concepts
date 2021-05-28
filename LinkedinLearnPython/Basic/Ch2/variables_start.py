# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)


# re-declaring the variable works
f = "abc"
print(f)


# ERROR: variables of different types cannot be combined
# print("This is a string"+ str(123))


# Global vs. local variables in functions
def some_function():
    global f
    f = "def"
    print(f)

some_function()
del f
print(f)

#The point of this code is to run an automation to print the following pattern
#using 1 for loop and an if/else statement.
#*
#**
#***
#****
#*****
#****
#***
#**
#*
# The for loop is set to increment to 10.
# while the counter variable i is 5 or less it will print the same number of stars as i.
# if i is more than 5 it will calculate 10-i which will then be multiplied by *
# To incrementally reduce the number of stars per iteration back down to 1.

#start
for i in range(0, 10):
    if i <= 5:
        print(i * "*")
    elif i > 5:
        print((10 - i) * "*")
#End
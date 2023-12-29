'''This programme will adapt a string to have each alternate letter in upper case
Then to turn each alternate word into upper case.'''
#In this case we will ask the user for a string by requesting input of a sentence. 
#We will create an empty string to store output string
#and conditional variable to control the for loop. 
#Use for loop to assign .upper and .lower instruction to capitalise every other character 
#within the string. The capitalise variable will change with each loop to achieve this.
#For fun also added if statement to skip the change is capitalise variable if the character
#is a space.
#Print output 1

#To have every other word capitalised we first split the string into words using .split()
#Then apply same for loop structure as above to capitalise every other word
# adding a space after each word added to the output list. 
#print string 2.

#I am first requesting a string from the user, 
#then creating an empty string (output_string) to store the output string and 
#a conditional statement (capitalise) to control the loop. 
user_string = input("Please write your sentence here?")
output_string = ""
capitalise = True
#The for loop will run through all characters in the string and depending on 
#condition of the capitalise variable it will add either a lower or upper case character
#to the output string. 
for char in user_string:
    if capitalise:
        output_string = output_string + char.upper()
    else:
        output_string = output_string + char.lower()
#Added functionality to ignore the change in the capitalise condition variable if 
# there is a space so the change in case will only happen with other characters. 
    if char != " ":
        capitalise = not capitalise
        #This step will change the capitalise condition between True and False with every
        #run through the loop if the character is not a space. 
print(output_string)

#2nd part of the task is to present string with every other word capitalised. 
#Using original user string the words are split into a list of words when there is a space.
#Then creating an empty string to store the output string and the conditional variable
#which will control the loop.
user_string = user_string.split(" ")
word_string = ""
capital = True
#The for loop will now run through the list of words and attach each word to the
#word_string variable in either upper case or lower depending on the capital variable. 

for word in user_string:
    if capital:
        word_string = word_string + word.upper() + " " 
        #A space has also been added between each word in the output string.
    else:
        word_string = word_string + word.lower() + " "
#The capital variable will change with each loop round.    
    capital = not capital
#The new string is printed with every other word capitalised. 
print(word_string)

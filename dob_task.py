"""This programme is to present 2 sets of information from a text file"""

"""pseudocode
1 open file using with statement so that it automatically closes and use unicode to encode correctly
2 iterate through the data to create a 2d list
use indexing to print name and surname of each line first
then print date of birth in second section.
use styling to improve readability of the titles
"""
# setting style class for later reference in titles.
class style:
    BOLD = '\033[1m'
    END = '\033[0m'
#open file using with statement this also closes the file when done. 
with open("./DOB.txt","r+",encoding="utf-8") as file:
    #Reading through data in the file and splitting into a list of lines
    line_list = file.read().splitlines()
    #creating a new empty list to generate a 2d list.
    #with data of each person as items inside the nested list.
    #The for loop iterates, splits each line into words and appends to the empty new_list.
    new_list = []
    for line in line_list:
        new_list.append(line.split())
    
    #Creating output styling titles and 
    #calling the 1st and 2nd items in each nested list to generate list of names. 
    #Calling the 3rd, 4th and 5th items in each nexted list for date of birth of each person.
    print(style.BOLD + "NAME" + style.END)
    print()
    for person in new_list:
        print(person[0] + " " + person[1])
    print("-" * 30)
    #space between 2 sets of output for readability.
    print() 
    print(style.BOLD + "BIRTHDATE" + style.END)
    print()
    for person in new_list:
        print(person[2] + " " + person[3] + " " + person[4])
    print("-" * 30)


    


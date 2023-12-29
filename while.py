#Pseudocode - set list in a variable to store user input answers.
#request input from user within while loop and store result in a control variable num.
#set while loop to repeat when !+ -1
#when user inputs -1 under an if condition, break loop and go to next code block.
#calculate sum and length of list excluding the -1
#print result

# setting a list variable to store the numbers input by the user.
# Num is the control variable that will request the user input and be used in
# the while loop condition.
user_list = []
num = int(input("Please enter a number:"))
while num != -1:
    #while loop set to repeat if not -1. Then to add to list and re-request.
    user_list.append(num)
    new_num = int(input("Please enter another number:"))
    #new_num is reassigned to num to continue the loop with the new input.
    num = new_num
    if num == -1:
        #Once user inputs -1 the average is found by dividing sum of all elements
        # by the length of the list. The result is then printed.
        list_length = len(user_list)
        list_total = sum(user_list)
        average = round((list_total/list_length), 2)
        print(f"Average of the numbers entered = {average}")
        break #LF (\n)
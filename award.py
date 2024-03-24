"""
This programme determines the award of a triathlon
record times of 3 events in minutes 
(swimming, cycling and running)
calculate total time 
display total time
assign award based on finishing time
if more than 111 minutes then no reward
edited to add SUPER HERO AWARD 240324
"""

#requesting times of races as integers to enable later calculating.
swimming = (int(input(" Please enter finishing time for your swimming race:")))
cycling = (int(input(" Please enter finishing time for your cycling race:")))
running = (int(input(" Please enter finishing time for running race:")))
total_time = swimming + cycling + running #calculating total time of race.
# Printing all results as well as the total to have a full table of results.
print("-" * 50)
print("YOUR RESULTS ARE AS FOLLOWS")
print("-" * 50)
print(f"Swimming :\t {swimming}")
print(f"Cycling :\t {cycling}")
print(f"Running :\t {running}")
print("-" * 50)
print(f"Your total race time is : {total_time} minutes.") # printing total time of race as requested. 
print("-" * 50)

#conditional statements assigning the correct rewards based on total finishing time. 
if total_time <= 80:
    print("You are an absolute SUPER HERO! you win £100,000")
elif total_time <= 100 :
    print("Congratulations on your Provincial colours award!")
elif total_time <= 105 :
    print("Congratulations on your Provincial half colours award!")
elif total_time <= 110 :
    print("Congratulations on your Provincial scroll award!")
else :
    print("Sorry but you have not won an award on this occasion!")
#end
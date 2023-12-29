"""
start programme that determines award of triathlon
record times of 3 events in minutes 
(swimming, cycling and running)
calculate total time 
display total time
assign award based on finishing time
if more than 111 minutes then no reward
"""

#requesting times of races as integers to enable later calculating.
swimming = (int(input(" Please enter finishing time for your swimming race:")))
cycling = (int(input(" Please enter finishing time for your cycling race:")))
running = (int(input(" Please enter finishing time for running race:")))
total_time = swimming + cycling + running #calculating total time of race.
print(f"Your total race time is : {total_time} minutes.") # printing total time of race as requested. 

#conditional statements assigning the correct rewards based on total finishing time. 
if total_time <= 100 :
    print("Congratulations on your Provincial colours award!")
elif total_time <= 105 :
    print("Congratulations on your Provincial half colours award!")
elif total_time <= 110 :
    print("Congratulations on your Provincial scroll award!")
else :
    print("Sorry but you have not won an award on this occasion!")
#end
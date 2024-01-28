''' The purpose of this programme is to calculate the total cost of a holiday

pseudocode
request user input for: 
city_flight with options from different cities with different costs
num_nights for the number of nights at a hotel
rental_days for number of days hiring a car. 

create 4 separate functions to calculate the following:
plane_cost
hotel_cost
car_rental
holiday_cost to add all cost outputs together

then display the details of the holiday with associated costs
'''
#class created for styling output.
class color:
   YELLOW = '\033[93m'
   BOLD = '\033[1m'
   END = '\033[0m'

# List of options for cities created using a nested list with following info:
# number, city Country, flight cost, hotel name, hotel cost, car rental cost. 
cities = [
    [1,"London England", 200, "The Plaza", 90, 25], 
    [2,"Manchester England", 300, "Holiday Inn", 80, 40], 
    [3, "Bercelona Spain", 400, "La Royale", 65, 50], 
    [4, "Rome Italy", 500, "La Spiagga", 55, 25 ], 
    [5, "Valletta Malta", 250, "Tas-Sliema", 70, 40], 
    [6, "Milan Italy",350, "La Famiglia", 60, 45], 
    [7, "Paris France", 450, "Le Chien Royal", 60, 60], 
    [8, "Marseille France", 220, "La Palace", 65, 40], 
    [9, "Athens Greece", 320, "Cosmopolit", 26, 30], 
    [10, "Prague Czech Republic", 420, "Salvator", 39, 26]
]
# Menu presentation using a title and for loop to iterate through the list and present
# information in a meaningful way. 
# While loop created to re-request input if incorrect input detected.
# This loop will break once city_flight is assigned a value other than 0.
city_flight = 0
while city_flight == 0:
    print(color.BOLD, color.YELLOW)
    print("MENU")
    print("FLIGHT DESTINATIONS:")
    print(color.END)

    for city in cities:
        print(f"{color.YELLOW}{city[0]}:{color.END} {city[1]} - £{city[2]}")
    # requesting selection from menu.
    city_selection = input("Please select a number from the menu to choose which city you will be visiting: ")
    # using try except to manage possible input errors such as alphabetical or out of range.
    #input is then converted to an integer and checked for being out of range with error message.
    try:
        city_selection = int(city_selection)
        if city_selection < 1 or city_selection > 10:
            print("Please choose a number between 1-10 from the menu")
            continue
    # Exception errors are managed below with instruction to enter 1-10.
    except Exception:
        print("Please enter a number between 1 and 10 to select the city you'd like to fly to.")
    else:
        # city_flight will point to the index of the chosen option on the menu.
        city_flight = (city_selection - 1)
        
        break
# requesting user input for number of nights and days needing rental car. 
num_nights = input("How many nights will you be staying? ")
num_nights = int(num_nights)

rental_days = input("How many days will you need a rental car? ")
rental_days = int(rental_days)

# Function that will point to flight cost
def plane_cost(city_flight):
    plane = cities[city_flight][2]
    return plane
# Function calculating cost of hotel stay based on number of nights required. 
def hotel_cost(num_nights):
    hotel = cities[city_flight][4] * num_nights
    return hotel
# Function calculating total cost of car rental based on number of days needed.
def car_rental(rental_days):
    car = cities[city_flight][5] * rental_days
    return car
# Function to calculate total cost of holiday using the outcome of the other 3 functions. 
def holiday_cost(city_flight, num_nights, rental_days):
    total = (plane_cost(city_flight)) + (hotel_cost(num_nights)) + (car_rental(rental_days))
    return total

# Print statements to present information to user of break down of cost and total. 
# Yellow and bold styling used to create a readable output. 
print(color.BOLD, color.YELLOW)
print("YOUR WOW HOLIDAY DETAILS!!")
print(color.END)
print(f"The cost of your flight to {cities[city_flight][1]} is{color.BOLD}{color.YELLOW} £{plane_cost(city_flight)}{color.END}")
print()
print(f"The cost of your hotel stay at {cities[city_flight][3]} for {num_nights} nights is{color.BOLD}{color.YELLOW} £ {hotel_cost(num_nights)}{color.END}")
print()
print(f"The cost of your car rental for {rental_days} days is{color.BOLD}{color.YELLOW} £{car_rental(rental_days)}{color.END}")
print(color.YELLOW)
print( "-" * 70)
print(color.END)
print(f"The total cost of your holiday comes to {color.BOLD}{color.YELLOW}£{holiday_cost(city_flight, num_nights, rental_days)}{color.END}")
print(color.YELLOW)
print("-" * 70)
print(color.END)
# END
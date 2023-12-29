"""This programme is to calculate stock and cost of inventory of items at a cafe."""

#Create a menu of items in the form of a list. 
#Create a dictionary with the items as keys and the number of each item as the value. 
#Create a dictionary with items as keys and the price of each item. 
#Create a calculation that will calculate the cost of all the inventory. 
#calculation- for each item(number of item x price), then add the results together to 
#get full cost of inventory. needs to iterate through each item in the menu. 

#menu created of items available in form of a list.
#dictionaries for stock amounts and prices created with keys referencing the menu items. 
menu = ["sugar sachets", "coffee pods", "tea bags", "carrot cake", "lemon cake", "biscuits"]
item_stock = {menu[0]:50, menu[1]:25, menu[2]:30, menu[3]:15, menu[4]:20, menu[5]:10}
item_price = {menu[0]:0.5, menu[1]:1, menu[2]:1, menu[3]:3, menu[4]:3, menu[5]:1}
#inventory variable created to calculate total of inventory for output. 
inventory_value = 0
#for loop created to iterate through the menu.
#Loop variable used to call out the keys in the 2 dictionaries for the calculation. 
for item in menu:
    inventory_value += (item_stock[item] * item_price[item])
    #calculation calculates the stock amount xitem price for each item in the menu
    #and adds it to the inventory_value variable for output
    #inventory value is printed.
print(inventory_value)

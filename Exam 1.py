#   Filename:           Exam 1
#   Created by:         jasongreen
#   Date:               Saturday, January 19, 2019
#   Time of Creation:   14:16
#   ---

import math

nights = int(input("How many nights will you be staying? "))
hotel_rate = int(input("What is the hotel cost? "))
miles_to_gal = int(input("How many miles to the gallon do you get? "))
miles_to_dest = int(input("How many miles is it to the destination? "))
cost_of_fuel = int(input("How much is gas these days? "))

total_hotel_cost = hotel_rate * nights
total_driving_cost = (miles_to_dest / miles_to_gal) * cost_of_fuel

total_vacation_cost = math.ceil(total_hotel_cost + total_driving_cost)

print("Sharon, your vacation will cost you ${}, "
      "wouldn't you rather just do a stay'cation instead?".format(total_vacation_cost))


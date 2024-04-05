# Name: Daniel James Keaty
# Purpose: Modular Programming Project 
# Date: 04 - April - 2024

# print ("Hello World")
# I didnt realise this was still in here lol. Carry over from when I made the file and wanted to check everything was working.

# Okay so I am doing the project for the college break. 
# It will be submitted for graded next week. Im using VScode on Fedora Linux, and Github for the first time. 
# The learning curve is steep but hopefully, itl be worth it lol.

# I made a flow chart last week outlining how I aim to tackle the project and how it should work. That is also on the Github page. 

import os
# Need this for checking if bookings.txt exists in the same directory as this file.

current_directory = os.path.dirname(os.path.abspath(__file__))
booking_file_path = os.path.join(current_directory, "bookings.txt")
# After puling my hair out for ages to get the txt files to work, realised i need this to make it work. Might be due to me using linux though. 
# This code should also make the code more platform agnostic since Linux, Windows and Mac have different directory structures. 


from datetime import date
from datetime import datetime
# Need this to check if the date the customer wants to fly on, is valid. 


def main():
    # Creating main function.
    # Initial introduction.
    print ("Welcome to Dan's Flight Management system!")
    print("Please select an option from the menu below")


    while True:
    # Display Menu Options.
    # TODO will add a secret option 5 here to reset the program and make debugging easier. 
        print("\n Menu")
        print("1) Book a Flight")
        print("2) Review Booking")
        print("3) Manage Passenger Details")
        print("4) Exit")
        
        # Handle User Input.
        # NB might need to ad better input validation here. 
        user_menu_selection = int(input("Please select an option (1-4): "))
        
        if user_menu_selection == 1:
            book_a_flight_function()
            
            break
            
        elif user_menu_selection == 2:
            review_booking_function()
            
            break
            
        elif user_menu_selection == 3:
            print ("Placeholder where function 3 goes")
            
            break
            
        elif user_menu_selection == 4:
            # Exits program.
            print ("Exiting Program...")
            
            break
        
        # Option 5 will go here to reset the program. 
            
        else:
            # Handles Invalid choices.
            print("Invalid choice. Please try again.")
            


    #print ("Please select an option;")
    
def book_a_flight_function():
    # Creating the function for option 1 in the main menu. 
    # On booking, should deduct one available seat from flight_data.txt . 
    # Should also add a customers details to bookings.txt. 
    # Going to create the flight_data.txt file now. 
    
    # print("Yay, you found function 1!")
    while True:
        # prompt the user to enter their name.
            customer_name = input("Please enter your name: ")
            # Gets the length of the user's name.
            customer_name_length = len(customer_name)
            
            # Checks to make sure the name is between 1 and 20 characters long. 
            if customer_name_length >= 1 and customer_name_length <= 20:
                break
    
            else:
                print("Please enter a name between 1 and 20 characters long.")
                
    while True:
        # Prompt the user to enter a valid contact number.
            customer_contact_number = input("Please enter your contact number: ")
            # Checks to make sure the number is 10 numbers long. 
            customer_contact_number_length = len(customer_contact_number)
        
            if customer_contact_number_length == 10:
                try :
                    customer_contact_number = int(customer_contact_number)
                    break
                except ValueError:
                    print("Please enter a valid contact number.")
            else:
                print("Please enter a contact number 10 numbers long")
            
        
    
    customer_departure_city = input("Please enter the city you wish to travel from: ")
    # TODO check to see that the departure city is valid 
    
    customer_arrival_city = input("Please enter your the city you wish to travel to: ")
    # TODO check to see that the arrival city is valid 

    
    while True:
        # Prompt the user to enter a valid date. 
        customer_depart_date = input("Please enter the date you wish to travel on (DD/MM/YYYY): ")
        try:
            # Try to convert the input to a datetime object. 
            customer_depart_date = datetime.strptime(customer_depart_date, "%d/%m/%Y")
            # Check to see if the date is in the future. 
            if customer_depart_date.date() >= datetime.now().date():
                # 
                break
            else:
                print("Please enter a date in the future.")
        except ValueError:
            # If date is incorrect, reprompt user to enter a valid date. 
            print("Please enter a valid date in the format DD/MM/YYYY")
            # The above code works. Don't touch lol. 
            
    print ("Testing to see if code reaches here....")        
    with open (booking_file_path, "a") as file:
        file.write(f"{customer_name},{customer_contact_number},{customer_departure_city},{customer_arrival_city},{customer_depart_date}\n")
        # This fucking line refuses to cooperate. Jesus Christ.
    print("program has read after the file open line wtf")
    
    
        
                
                
    
    
    
    

def review_booking_function():
    # Creating the fuction for option 2 in the menu. 
    # Will be able to review bookings and interact with bookings.txt file.
    
    # From what I understand, this uses import.os to grab current directory. 
    current_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Uses the same thing to grab the path to the bookings.txt file. 
    booking_file_path = os.path.join(current_directory, "bookings.txt")
    
    # print("Booking function found, yay!")
    # Currently having trouble as this function isn't being called properly. 
    
    
    if os.path.isfile(booking_file_path):
        print("Booking file found...initialising!")
        
    else:
        print("Booking file not found...creating file now")
        with open(booking_file_path, "w") as file:
            pass
        print("File has now been created!")
        
        
    
    
    # TODO might need to add more input validation here. 
    int(input(("Please enter your booking number: ")))
    print("Thank you.")
    
    # Going to work on the function for booking flights now, will return here later. 
    
    
    



main()
# 



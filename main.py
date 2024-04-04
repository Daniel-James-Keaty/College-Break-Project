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


def main():
    # Creating main function.
    # Initial introduction.
    print ("Welcome to Dan's Flight Management system!")
    print("Please select an option from the menu below")


    while True:
    # Display Menu Options.
        print("\n Menu")
        print("1) Book a Flight")
        print("2) Review Booking")
        print("3) Manage Passenger Details")
        print("4) Exit")
        
        # Handle User Input.
        # NB might need to ad better input validation here. 
        user_menu_selection = int(input("Please select an option (1-4): "))
        
        if user_menu_selection == 1:
            print ("Placeholder where function 1 goes")
            
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
            
        else:
            # Handles Invalid choices.
            print("Invalid choice. Please try again.")
            


    #print ("Please select an option;")

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
        
        
    
    
    # NB might need to add more input validation here. 
    int(input(("Please enter your booking number: ")))
    print("Thank you.")
    
    
    
    



main()




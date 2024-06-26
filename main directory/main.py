# Name: Daniel James Keaty
# Purpose: Modular Programming Project 
# Date: 04 - April - 2024
# Okay so I am doing the project for the college break. 
# It will be submitted for graded next week. Im using VScode on Fedora Linux, and Github for the first time. 
# The learning curve is steep but hopefully, itl be worth it lol.
# I made a flow chart last week outlining how I aim to tackle the project and how it should work. That is also on the Github page. 
# To see the history and git commits, see my Github repo (https://github.com/Daniel-James-Keaty/College-Break-Project/tree/main)
import os
# Need this for checking if bookings.txt exists in the same directory as this file.
current_directory = os.path.dirname(os.path.abspath(__file__))
booking_file_path = os.path.join(current_directory, "bookings.txt")
flight_data_file_path = os.path.join(current_directory, "flight_data.txt")
# After puling my hair out for ages to get the txt files to work, realised i need this to make it work. Might be due to me using linux though. 
# This code should also make the code more platform agnostic since Linux, Windows and Mac have different directory structures. 
from datetime import date
from datetime import datetime
# Need this to check if the date the customer wants to fly on, is valid. 


def main():
    '''
    Creating main function. 
    This presents a menu thatdisplays options to the user. 
    Shows menu along with introduction.
    '''
    print ("Welcome to Dan's Flight Management system!")
    print("Please select an option from the menu below")
    while True:
    # Display Menu Options.
        print("\n Menu")
        print("1) Book a Flight")
        print("2) Review Booking")
        print("3) Manage Passenger Details")
        print("4) Cancel Booking")
        # Adding this bit for part 2 of the project.
        print("5) Exit")
        print()
        print()
        # New line
        user_menu_selection = int(input("Please select an option (1-4): "))
        if user_menu_selection == 1:
            book_a_flight_function()
            # Takes user to book a flight  
        elif user_menu_selection == 2:
            review_booking_function()
            # Takes user to review their booking. 
        elif user_menu_selection == 3:
            manage_passenger_details()     
            # Takes user to review their booking.       
        elif user_menu_selection == 4:
            cancel_user_booking(booking_file_path)     
            # Takes user to cancel their booking.     
        elif user_menu_selection == 5:
            # Exits program.
            print ("Exiting Program...")
            break           
        else:
            # Handles Invalid choices.
            print("Invalid choice. Please try again.")
    # End of funtion

            
                
def book_a_flight_function():
    '''
    This is the function for option 1 in the main menu. 
    On booking, should deduct one available seat from flight_data.txt . 
    Should also add a customers details to bookings.txt. 
    Going to create the flight_data.txt file now. 
    '''
    while True:
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
        # TODO check to see that the departure city is valid.
        customer_arrival_city = input("Please enter your the city you wish to travel to: ")
        # TODO check to see that the arrival city is valid.
        while True:
            # Prompt the user to enter a valid date. 
            customer_depart_date = input("Please enter the date you wish to travel on (DD/MM/YYYY): ")
            try:
                # Try to convert the input to a datetime object. 
                customer_depart_date = datetime.strtime(customer_depart_date.split()[0], "%d/%m/%Y")
                # Check to see if the date is in the future. 
                if customer_depart_date.date() >= datetime.now().date():
                    break
                else:
                    print("Please enter a date in the future.")
            except ValueError:
            # If date is incorrect, reprompt user to enter a valid date. 
                print("Please enter a valid date in the format DD/MM/YYYY")
            # The above code works. Don't touch lol. 
        with open (booking_file_path, "a") as file:
            file.write(f"{customer_name},{customer_contact_number},{customer_departure_city},{customer_arrival_city},{customer_depart_date}\n")
            # This line was being uncooperative. Dont touch lol.
        print()
        # New line
        break
    # End of funtion

    

def review_booking_function():
    ''''
    Lets users view, interact with their booking in bookings.txt
    Option 2 in the manin menu.
    '''
    while True:
    # From what I understand, this uses import.os to grab current directory. 
        current_directory = os.path.dirname(os.path.realpath(__file__))
    # Uses the same thing to grab the path to the bookings.txt file. 
        booking_file_path = os.path.join(current_directory, "bookings.txt")    
        if os.path.isfile(booking_file_path):
            print("Booking file found...initialising!")
            # Should print if bookings.txt file already exists
        else:
            print("Booking file not found...creating file now")
            # Should print if bookings.txt file doesn't exist.
            with open(booking_file_path, "w") as file:    
                pass    
        search_contact_number = input("Please enter contact number: ")
        found = False
        with open(booking_file_path, "r") as file:
            next(file)
            for line in file:
                fields = line.strip().split(",")
                if len(fields) >= 5:
                    if search_contact_number in fields[1]: 
                        # Check if the contact number is in the second field
                        print("Found the booking: ")
                        print("Name         | Contact Number | Departure City | Arrival City | Departure Date")
                        print("-" * 80)  
                        # Print a line separator
                        # Split the line into fields
                        fields = line.strip().split(",")
                        # Print each field with formatting
                        print(f"{fields[0]:<13}| {fields[1]:<15}| {fields[2]:<15}| {fields[3]:<13}| {fields[4]:<15}")
                        found = True
            if not found:
                print("Booking not found.")
        print()
        print()
        # New line
        menu_prompt = input("Please input 1 to return to the main menu: ")
        if menu_prompt == "1":
            print("Returning to main menu.")
            break
            # Should take user back to the main menu if they enter 1
    # End of funtion


def manage_passenger_details():
    '''
    This function checks if a users booking exists by checking the name they used in the booking. 
    Diplays the inofrmation in a nice table. 
    If a booking under the entered name does not exist, it prompts the user to go to the main menu and book there with
    option 1.
    '''
    while True:
        passenger_name = input("Please enter the name of the passenger: ")
        booking_file_path = os.path.join(current_directory, "bookings.txt")
        booked_passengers = []
        # Need to declare these variables so that code works okay. 
        with open (booking_file_path, 'r') as file:
            next(file)
            for line in file:
                booking_info = line.strip().split(',')
                customer_name = booking_info[0].strip()
                booked_passengers.append(customer_name)
                # This code took a lot of messing around with to get it working. Seems to work okay now. Should get passenger info from text file and make it appear nicely here.
                print()
                # New line
                if customer_name == passenger_name:
                    # Format the booking details into a table
                    headers = ["Customer Name", "Contact Number", "Departing From", "Arriving To", "Date of Departure"]
                    # Print headers
                    for header in headers:
                        print(f"{header:<20}", end="")  
                        # Left-align headers with a width of 20 characters
                print()  
                # New line
                for info in booking_info:
                    print(f"{info:<20}", end="")  
                    # Left-align datflight_data_file_path = os.path.join(current_directory, "flight_data.txt")a with a width of 20 characters
                print()    
                # Handle User Input.
            # Stop after finding the matching passenger name
        print()
        # Print line
        print("Returning to main menu.")
        # Gonna try using these, while True and break statements to stop the program from exiting prematurely. 
        break
    while True:
        if passenger_name in booked_passengers:
                print(f"{passenger_name} has a booking.")
                print(f"Please see the passenger details below")
                print()
                # New line
                menu_prompt = input("Please input 1 to return to the main menu: ")
                if menu_prompt == "1":
                    break
                # Should take user back to the main menu if they enter 1
        else:
            print(f"{passenger_name} does not have a booking, Please go to option 2 in the main menu to book a flight.")
            print()
            # New line
            break
    # End of funtion


def cancel_user_booking(booking_file_path):
    '''
    This function is option 4 in the main menu, will allow a user to cancel their booking. 
    '''
    found = False
    contact_number_for_cancel = int(input("Please eneter your contact number: "))
    # Gets a user to enter their contact number to cancel their booking. 
    with open (booking_file_path, 'r') as file:
        lines = file.readlines()
        # Reads the bookings file to see if the user's contact number exist in it.      
    with open(booking_file_path, 'w') as file:
        for line in lines:
            booking_info = line.strip().split(',')
            if booking_info[1].strip() == str(contact_number_for_cancel):
                found = True
                print("Booking found, cancelling...")
                # Removes customer's data from booking file if their contact number matches a value in the file.   
            else:
                file.write(line)        
        if not found:
            print("Booking mot found with the provided contact number.")
        else:
            print("Booking cancelled successfully.")
            # Informs the user that their booking has been cancelled. Then returns them to main menu.
    # End of funtion


main()
'''
Main function. Should pull in all the functions shown above. 
'''





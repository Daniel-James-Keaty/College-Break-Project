# Name: Daniel James Keaty
# Purpose: Modular Programming Project 
# Date: 04 - April - 2024

print ("Hello World")

# Okay so I am doing the project for the college break. 
# It will be submitted for graded next week. Im using VScode on Fedora Linux, and Github for the first time. 
# The learning curve is steep but hopefully, itl be worth it lol

# I made a flow chart last week outlining how I aim to tackle the project and how it should work

def main():
    # Initial introduction
    print ("Welcome to Dan's Flight Management system!")
    print("Please select an option from the menu below")


    while True:
    # Display Menu Options
        print("\n Menu")
        print("1) Book a Flight")
        print("2) Review Booking")
        print("3) Manage Passenger Details")
        print("4) Exit")
        
        # Handle User Input
        user_menu_selection = int(input("Please select an option (1-4): "))
        
        if user_menu_selection == 1:
            print ("Placeholder where function 1 goes")
            
            break
            
        elif user_menu_selection == 2:
            print ("Placeholder where function 2 goes")
            
            break
            
        elif user_menu_selection == 3:
            print ("Placeholder where function 3 goes")
            
            break
            
        elif user_menu_selection == 4:
            # Exit program
            print ("Exiting Program...")
            
            break
            
        else:
            # Handles Invalid choices
            print("Invalid choice. Please try again.")
            


    #print ("Please select an option;")

main()


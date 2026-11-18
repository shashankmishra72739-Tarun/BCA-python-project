# Railway Ticket Reservation System
# BCA 1st Semester Python Assignment

tickets = []


# Main Program

def main():

    while True:

        print("RAILWAY TICKET RESERVATION SYSTEM")

        print("1. Book Ticket")
        print("2. Show All Tickets")
        print("3. Search Ticket")
        print("4. Cancel Ticket")
        print("5. Check Ticket Status")
        print("6. Calculate Fare")
        print("7. Show Passenger Details")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket()

        elif choice == "2":
            show_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            cancel_ticket()

        elif choice == "5":
            check_status()

        elif choice == "6":
            calculate_fare()

        elif choice == "7":
            passenger_details()

        elif choice == "8":
            print("Thank you for using the Railway Ticket Reservation System.")
            break

        else:
            print("Wrong choice. Please try again.")


# Function to book a ticket

def book_ticket():

    print("Book Railway Ticket")

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    gender = input("Enter gender: ")
    source = input("Enter source station: ")
    destination = input("Enter destination station: ")
    train = input("Enter train name: ")
    date = input("Enter journey date: ")

    print("Select class")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")
    print("4. AC First Class")

    class_choice = input("Enter class choice: ")

    if class_choice == "1":
        train_class = "Sleeper"
        fare = 500

    elif class_choice == "2":
        train_class = "AC 3 Tier"
        fare = 1200

    elif class_choice == "3":
        train_class = "AC 2 Tier"
        fare = 1800

    elif class_choice == "4":
        train_class = "AC First Class"
        fare = 2500

    else:
        print("Invalid class choice.")
        return

    ticket_number = len(tickets) + 1001

    ticket = {
        "ticket": ticket_number,
        "name": name,
        "age": age,
        "gender": gender,
        "source": source,
        "destination": destination,
        "train": train,
        "date": date,
        "class": train_class,
        "fare": fare,
        "status": "Confirmed"
    }

    tickets.append(ticket)

    print("Ticket booked successfully!")
    print("Ticket Number:", ticket_number)
    print("Passenger Name:", name)
    print("Train:", train)
    print("Class:", train_class)
    print("Fare:", fare)
    print("Status: Confirmed")


# Function to show all tickets

def show_tickets():

    print("All Booked Tickets")

    if len(tickets) == 0:
        print("No tickets booked.")
        return

    for ticket in tickets:

        print("Ticket Number:", ticket["ticket"])
        print("Passenger Name:", ticket["name"])
        print("Age:", ticket["age"])
        print("Gender:", ticket["gender"])
        print("From:", ticket["source"])
        print("To:", ticket["destination"])
        print("Train:", ticket["train"])
        print("Journey Date:", ticket["date"])
        print("Class:", ticket["class"])
        print("Fare:", ticket["fare"])
        print("Status:", ticket["status"])


# Function to search ticket

def search_ticket():

    print("Search Ticket")

    ticket_number = int(input("Enter ticket number: "))

    for ticket in tickets:

        if ticket["ticket"] == ticket_number:

            print("Ticket Found")
            print("Passenger Name:", ticket["name"])
            print("Train:", ticket["train"])
            print("From:", ticket["source"])
            print("To:", ticket["destination"])
            print("Journey Date:", ticket["date"])
            print("Class:", ticket["class"])
            print("Fare:", ticket["fare"])
            print("Status:", ticket["status"])

            return

    print("Ticket not found.")


# Function to cancel ticket

def cancel_ticket():

    print("Cancel Ticket")

    ticket_number = int(input("Enter ticket number: "))

    for ticket in tickets:

        if ticket["ticket"] == ticket_number:

            if ticket["status"] == "Cancelled":
                print("Ticket is already cancelled.")
                return

            ticket["status"] = "Cancelled"

            print("Ticket cancelled successfully.")
            return

    print("Ticket not found.")


# Function to check ticket status

def check_status():

    print("Check Ticket Status")

    ticket_number = int(input("Enter ticket number: "))

    for ticket in tickets:

        if ticket["ticket"] == ticket_number:

            print("Passenger Name:", ticket["name"])
            print("Ticket Number:", ticket["ticket"])
            print("Status:", ticket["status"])

            return

    print("Ticket not found.")


# Function to calculate fare

def calculate_fare():

    print("Calculate Railway Fare")

    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")
    print("4. AC First Class")

    choice = input("Enter class choice: ")

    if choice == "1":
        print("Sleeper Fare: 500")

    elif choice == "2":
        print("AC 3 Tier Fare: 1200")

    elif choice == "3":
        print("AC 2 Tier Fare: 1800")

    elif choice == "4":
        print("AC First Class Fare: 2500")

    else:
        print("Invalid choice.")


# Function to show passenger details

def passenger_details():

    print("Passenger Details")

    ticket_number = int(input("Enter ticket number: "))

    for ticket in tickets:

        if ticket["ticket"] == ticket_number:

            print("Passenger Name:", ticket["name"])
            print("Age:", ticket["age"])
            print("Gender:", ticket["gender"])
            print("Source:", ticket["source"])
            print("Destination:", ticket["destination"])
            print("Train:", ticket["train"])
            print("Journey Date:", ticket["date"])
            print("Class:", ticket["class"])

            return

    print("Ticket not found.")


# Start the program

main()

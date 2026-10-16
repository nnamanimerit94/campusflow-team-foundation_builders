#imports
import json
import os
from campusflow.tickets import view_all_tickets, assign_ticket, create_ticket, view_student_tickets
from campusflow.workflow import update_ticket_status, view_work_queue
from campusflow.reports import view_reports
from campusflow.storage import save_tickets


# Get the path of the JSON file in the project root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TICKET_FILE = os.path.join(BASE_DIR, "tickets.json")

# Create the JSON file if it does not exist
if not os.path.exists(TICKET_FILE):
    with open(TICKET_FILE, "w") as file:
        json.dump({}, file, indent=4)

# Load the tickets from the JSON file
with open(TICKET_FILE, "r") as file:
    tickets = json.load(file)
if not tickets:
    tickets = {}



# CampusFlow Helpdesk Application
def main():
    print("================================")
    print(" Welcome to CampusFlow")
    print(" Campus Helpdesk Management")
    print("================================")

    while True:
        print("\nWho are you?")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                print("\n--- ADMIN MENU ---")
                print("1. View all tickets")
                print("2. Assign ticket")
                print("3. Update ticket status")
                print("4. View work queue")
                print("5. View reports")
                print("6. Return to main menu")
                admin_choise=input("Enter your choice: ")

                if admin_choise=="1":
                    while True:
                        print("=========")
                        view_all_tickets(tickets)
                        print("=========")
                        exit_view=input("1. To exit: ")
                        print()
                        if exit_view=="1":
                            break
                        else:
                            print("invalid input")

                elif admin_choise=="2":
                    while True:
                        print("=========")
                        assign_ticket(tickets)
                        save_tickets(tickets)
                        print("=========")
                        exit_assing=input("1. To exit: ")
                        if exit_assing=="1":
                            break
                        else:
                            print("invalid input")

                elif admin_choise=="3":
                    while True:
                        print("=========")
                        update_ticket_status(tickets)
                        save_tickets(tickets)
                        print("=========")
                        exit_update=input("1. To exit: ")
                        if exit_update=="1":
                            break
                        else:
                            print("invalid input")
                elif admin_choise=="4":
                    while True:
                        print("=========")
                        view_work_queue(tickets)
                        print("=========")
                        exit_update=input("1. To exit: ")
                        if exit_update=="1":
                            break
                        else:
                            print("invalid input")
                elif admin_choise=="5":
                    while True:
                        print("=========")
                        view_reports(tickets)
                        print("=========")
                        exit_assing=input("1. To exit: ")
                        if exit_assing=="1":
                            break
                        else:
                            print("invalid input")
                elif admin_choise=="6":
                    print("Exited")
                    break

        elif choice == "2":
            while True:
                print("\n--- STUDENT MENU ---")
                print("1. Create a support ticket")
                print("2. View tickets")
                print("3. Return to main menu")
                student_choice=input("Enter your choice: ")

                if student_choice=="1":
                    while True:
                        print("=========")
                        create_ticket(tickets)
                        save_tickets(tickets)
                        print("=========")
                        student_Create=input("1. To exit: ")
                        if student_Create=="1":
                            break
                        else:
                            print("invalid input")
                elif student_choice=="2":
                    while True:
                        print("=========")
                        view_student_tickets(tickets)
                        print("=========")
                        student_Create=input("1. To exit: ")
                        if student_Create=="1":
                            break
                        else:
                            print("invalid input")
                elif student_choice=="3":
                    print("Exited")
                    break

        elif choice == "3":
            print("Thank you for using CampusFlow!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
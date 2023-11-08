class Flight:
    def __init__(self, passenger_name, passport_id, journey_date, destination, flight_type):
        self.passenger_name = passenger_name
        self.passport_id = passport_id
        self.journey_date = journey_date
        self.destination = destination
        self.flight_type = flight_type

    def __str__(self):
        return f"Flight for {self.passenger_name} (Passport ID: {self.passport_id}) on {self.journey_date} to {self.destination} ({self.flight_type} Class)"

class OnlineReservation:
    def __init__(self):
        self.accounts = {}

    def create_account(self, mobile, name, pin):
        if mobile in self.accounts:
            print("\nAn account with this number already exists!\n")
        else:
            new_account = {"mobile": mobile, "name": name, "pin": pin, "flights": []}
            self.accounts[mobile] = new_account
            print("\nAccount created successfully.\n")

    def login(self, mobile, pin):
        if mobile in self.accounts and self.accounts[mobile]['pin'] == pin:
            return self.accounts[mobile]
        else:
            print("\nIncorrect mobile or PIN.\n")
            return None

    def book_flight(self, user):
        passenger_name = input("Enter passenger name: ")
        passport_id = input("Enter Passport ID: ")
        journey_date = input("Enter journey date (e.g., DD-MM-YYYY): ")
        destination = input("Enter destination: ")
        flight_type = input("Select flight type (Business or Economy): ").capitalize()
        flight = Flight(passenger_name, passport_id, journey_date, destination, flight_type)
        user["flights"].append(flight)
        print(f"\n{flight}\n")

    def cancel_reservation(self, user, passport_id):
        for flight in user["flights"]:
            if flight.passport_id == passport_id:
                user["flights"].remove(flight)
                print(f"\nFlight for passenger with Passport ID {passport_id} cancelled.\n")
                return
        print(f"\nFlight for passenger with Passport ID {passport_id} not found.\n")

    def view_flights(self, user):
        if not user["flights"]:
            print("\nNo flights found.\n")
            return

        print("\nYour Flights:")
        for flight in user["flights"]:
            print(flight)

    def delete_account(self, mobile, pin):
        if mobile in self.accounts and self.accounts[mobile]['pin'] == pin:
            del self.accounts[mobile]
            print("\nAccount deleted successfully.\n")
        else:
            print("\nIncorrect mobile or PIN.\n")

def main():
    registration = OnlineReservation()
    print("Reservation System of BANGLADESH BIMAN!")

    while True:
        print("1. Sign Up")
        print("2. Log In")
        print("3. Delete Account")
        print("4. Exit")

        choice = input("\nEnter your choice, Please: ")

        if choice == "1":
            mobile = input("Enter your mobile number: ")
            name = input("Enter your name: ")
            pin = input("Enter your new PIN: ")
            registration.create_account(mobile, name, pin)

        elif choice == "2":
            mobile = input("Enter mobile number: ")
            pin = input("Enter your PIN: ")
            user = registration.login(mobile, pin)
            if user:
                while True:
                    print("1. Book Flight")
                    print("2. Cancel Flight")
                    print("3. View Flights")
                    print("4. Log Out")

                    user_choice = input("\nEnter your choice: ")

                    if user_choice == "1":
                        registration.book_flight(user)

                    elif user_choice == "2":
                        passport_id = input("Enter Passport ID to cancel: ")
                        registration.cancel_reservation(user, passport_id)

                    elif user_choice == "3":
                        registration.view_flights(user)

                    elif user_choice == "4":
                        print("\nLogged out successfully!\n")
                        break

                    else:
                        print("\nInvalid choice!\n")

        elif choice == "3":
            mobile = input("Enter mobile number: ")
            pin = input("Enter your PIN: ")
            registration.delete_account(mobile, pin)

        elif choice == "4":
            print("\nTHANK YOU!\n")
            break

        else:
            print("\nInvalid choice!\n")

if __name__ == '__main__':
    main()

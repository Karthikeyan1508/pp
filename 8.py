print("Welcome to Bike Shop!")

bikes = ["MTB", "Geared", "Non-Geared", "With Training Wheels", "For Trail Riding"]
bill = 0

while True:
    print("\nChoose any of the following Services:")
    print("1: View Available Bikes\n2: View Prices\n3: Place Orders\n4: Exit")

    try:
        option = int(input("Enter your choice: "))

        if option == 1:
            print("\nThe Bikes Available are:")
            for bike in bikes:
                print(f"- {bike}")

        elif option == 2:
            print("\nPrice List:")
            print("1. Hourly ---- Rs 100 per hour")
            print("2. Daily ---- Rs 500 per day")
            print("3. Weekly ---- Rs 2500 per week")
            print("Family Pack (3 to 5 rentals) gets a 30% discount.")

        elif option == 3:
            print("\nChoose your rental type:")
            print("1. Hourly\n2. Daily\n3. Weekly")
            
            rental_type = int(input("Enter your option: "))
            num_bikes = int(input("Enter the number of bikes (3-5 for family pack discount): "))

            if num_bikes < 1:
                print("Invalid number of bikes.")
                continue

            if rental_type == 1:
                bill += 100 * num_bikes
            elif rental_type == 2:
                bill += 500 * num_bikes
            elif rental_type == 3:
                bill += 2500 * num_bikes
            else:
                print("Invalid rental type. Please choose a valid option.")
                continue

            print(f"Your initial bill is Rs {bill}")

            if 3 <= num_bikes <= 5:
                discount_choice = input("Do you want to avail the family pack discount? (y/n): ").lower()
                if discount_choice == 'y':
                    bill *= 0.7
                    print("30% Family Pack discount applied.")
            
            print(f"Thanks for renting! Your final bill is Rs {bill}")
            print("Pay on checkout.")
            break

        elif option == 4:
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid service.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

total_slots = 5
rate_per_hour = 50
parking = {}

while True:
    print("\n---- Smart Parking Menu ----")
    print("1. Park Vehicle")
    print("2. Remove Vehicle & Pay")
    print("3. Check Available Slots")
    print("4. View Parked Vehicles")
    print("5. Exit")

    
    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 5:
        print("Invalid choice. Please enter between 1 and 5.")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(parking) < total_slots:
            vehicle_no = input("Enter vehicle number: ")
            hours = int(input("Enter expected parking hours: "))
            parking[vehicle_no] = hours
            print("Vehicle parked successfully")
        else:
            print("Parking Full")

    elif choice == 2:
        vehicle_no = input("Enter vehicle number: ")
        if vehicle_no in parking:
            hours = parking[vehicle_no]
            amount = hours * rate_per_hour
            print("Parking Hours:", hours)
            print("Amount to Pay: Rs.", amount)
            print("Payment Successful")
            del parking[vehicle_no]
        else:
            print("Vehicle not found")

    elif choice == 3:
        available = total_slots - len(parking)
        print("Available Slots:", available)

       
        print("Slot Numbers:")
        for i in range(1, total_slots + 1):
            print("Slot", i)

    elif choice == 4:
        if parking:
            print("\nParked Vehicles:")
           
            for v, h in parking.items():
                print(v, "-", h, "hours")
        else:
            print("No vehicles parked")

    elif choice == 5:
        print("Thank you for using Smart Parking System")
        break

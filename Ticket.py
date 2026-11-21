print("====================================")
print("      BUS TICKET FARE CALCULATOR")
print("====================================")

name = input("Enter Passenger Name: ")

distance = float(input("Enter Distance (KM): "))

passengers = int(input("Enter Number of Passengers: "))

print("\nSelect Passenger Category:")
print("1. Normal Passenger")
print("2. Student (20% Discount)")
print("3. Senior Citizen (30% Discount)")

choice = int(input("Enter Your Choice: "))

rate = 2

basic_fare = distance * rate * passengers

if choice == 1:
    category = "Normal Passenger"
    discount = 0

elif choice == 2:
    category = "Student"
    discount = 20

elif choice == 3:
    category = "Senior Citizen"
    discount = 30

else:
    print("Invalid Choice!")
    exit()

discount_amount = basic_fare * discount / 100

total_fare = basic_fare - discount_amount

print("\n========== BUS TICKET ==========")

print("Passenger Name:", name)
print("Distance:", distance, "KM")
print("Passengers:", passengers)
print("Category:", category)
print("Basic Fare: Rs.", basic_fare)
print("Discount:", discount, "%")
print("Discount Amount: Rs.", discount_amount)

print("--------------------------------")
print("FINAL TICKET FARE: Rs.", total_fare)
print("================================")

print("Thank You! Have a Safe Journey.")
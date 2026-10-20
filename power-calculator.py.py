print("===== UNIT CONVERTER =====")

while True:
    print("\n1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n1. Kilometers to Meters")
        print("2. Meters to Kilometers")
        print("3. Centimeters to Meters")
        
        option = input("Enter option: ")
        value = float(input("Enter value: "))

        if option == "1":
            print("Result:", value * 1000, "meters")
        elif option == "2":
            print("Result:", value / 1000, "kilometers")
        elif option == "3":
            print("Result:", value / 100, "meters")
        else:
            print("Invalid option")

    elif choice == "2":
        print("\n1. Kilograms to Grams")
        print("2. Grams to Kilograms")
        
        option = input("Enter option: ")
        value = float(input("Enter value: "))

        if option == "1":
            print("Result:", value * 1000, "grams")
        elif option == "2":
            print("Result:", value / 1000, "kilograms")
        else:
            print("Invalid option")

    elif choice == "3":
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        option = input("Enter option: ")
        value = float(input("Enter temperature: "))

        if option == "1":
            result = (value * 9 / 5) + 32
            print("Result:", result, "°F")
        elif option == "2":
            result = (value - 32) * 5 / 9
            print("Result:", result, "°C")
        else:
            print("Invalid option")

    elif choice == "4":
        print("Thank you for using Unit Converter!")
        break

    else:
        print("Invalid choice")
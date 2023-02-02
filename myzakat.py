print("Select operation.")
print("1.Money")
print("2.Gold")
print("3.Silver")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")


    # check if choice is one of the three options
    if choice in ('1', '2', '3'):
        try:
            num1 = float(input("Enter the number of your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if '1' >= '150000':
            print(num1*2.5/100)

        if '1' < '150000':
            print('u dont need to pay')

        elif choice == '2':
            print(num1*2.5/100)

        elif choice == '3':
            print(num1*2.5/100 )


        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
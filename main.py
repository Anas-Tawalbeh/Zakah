"""
Program: Zakat Calculator 
Author: Anas Tawalbeh
Terminal-based calcuator that help user calculate the amount of zakat for thier various type of wealth including:
Cash, Gold, Silver,Agrichulture, Livestock and more
Significant constants
         there is no constants
 2. The inputs are
         Type of wealth
         Amount of wealth
 3. Computations:
         
 4. The outputs are
         zakat amount
"""
zakat = input("Type of wealt: Cash, Gold,Plantation:")
cash = float(input("Enter the number of money"))
gold = float(input("Enter the number of gold(kg):"))
silver = float(input ("Enter the number of silver: "))


print(zakat)

#functions definitions
#def main():
#<<<<<<< HEAD
        #print('something')
#=======
        #print()   
#>>>>>>> 8ffe6ac310b457302c86c69c6242bbc5990cbf81
        #code goes her

                
#if __name__ == "__main__":
         #main()


print("Select choice.")
print("cash")
print("gold")
print("silver")

"cash" >= 200000

while True:
    # take input from the user
    choice = input("Enter option: ")

    # check if choice is one of the four options
    if choice in ('cash', 'gold', 'silver'):
        try:
            num1 = float(input("Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter the number!!")
        
        except:
            print("Can not calculate!! Please check your data.")

        if choice == 'cash':
            print(num1*2.5/100)

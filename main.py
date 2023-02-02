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
while True:
    try:
        x = input("select the type (cash,Gold,Silver,Agrichulture): ")
        number1 = float(input("Input  the number:"))     #we need to put 'int' before the code if u dont put the result will be string not numeric ex '5'+'5'=55 not 10    
    except ValueError:
        print("Pleas enter the correct value")
    except NameError:
        print("Please Enter the correct selection")
        continue

    try:
    #calculate 
        if x=='cash'>='150000':
            print(number1*2.5/100)
        elif "cash"<="150000":
         print("U didn't need to pay")
        elif x == 'gold'>='85':
            print(number1*2.5/100)
        elif x == 'silver'>='85':
            print(number1*2.5/100)
    except ZeroDivisionError:
        print("Cannot devide by zero")

# check if user wants another calculation
# break the while loop if answer is no
    next_calculation = input("Do you want to calculate again? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Welcom")
#functions definitions
#def main():
#print('something')
#print()   
#if __name__ == "__main__":
#main()

a = True  # Initialize a boolean value for the loop

while a:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    
    print("1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division")
    choice = int(input())
    
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice")
    
    # Ask the user if they want to continue
    a = int(input("Enter 1 or any other number to continue or 0 exit:"))

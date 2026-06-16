import os
import time

def clear_screen():
    """Clears the terminal screen for both Windows ('nt') and Mac/Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate(prompt):
    """Safely captures numeric inputs and prevents crashes from text strings."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def format_result(result):
    """Formats the float result into an integer if it has no decimal part."""
    if result.is_integer():
        return int(result)
    return result

# Fresh start: clear the screen right when the program fires up
clear_screen()

while True:
    print("\n--- CALCULATOR MENU | VERSION 1.0 ---")
    calculator_input = input("Choose an option (div, mul, add, sub, power, clear, exit): ").strip().lower()
    print("-" * 65)

    # UTILITY COMMANDS
    if calculator_input == "clear":
        clear_screen()
        continue  # Skips the rest of the loop and starts fresh at the menu
        
    elif calculator_input in ["exit", "quit"]:
        print("Thanks for using the calculator. Goodbye!")
        time.sleep(3)
        break  # Breaks the while loop to end the program cleanly

    # DIVISON SECTION
    elif calculator_input == "div":
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")        
        try:
            if num2 == 0:
                print("Error: You cannot divide by zero! It breaks the core calculating system!")
            else:
                result = num1 / num2
                print(f"The result of {num1:g} divided by {num2:g} is {format_result(result)}")
        except OverflowError:
            print("Error: The result overflows the python interger limit!")
            
    # MULTIPLICATION SECTION
    elif calculator_input == "mul":
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")       
        try:
            result = num1 * num2
            print(f"The result of {num1:g} multiplied by {num2:g} is {format_result(result)}")
        except OverflowError:
            print("Error: The result overflows the python interger limit!")
        
    # ADDITION SECTION
    elif calculator_input == "add":
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")
        try:
            result = num1 + num2
            print(f"The result of {num1:g} plus {num2:g} is {format_result(result)}")
        except OverflowError:
            print("Error: The result overflows the python interger limit!")
        
    # SUBTRACTION SECTION
    elif calculator_input == "sub":
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")      
        try:
            result = num1 - num2
            print(f"The result of {num1:g} minus {num2:g} is {format_result(result)}")
        except OverflowError:
            print("Error: The result overflows the python interger limit!")
        
    # POWER SECTION
    elif calculator_input == "power":
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")      
        try:
            result = num1 ** num2
            print(f"The result of {num1:g} powered by {num2:g} is {format_result(result)}")
        except OverflowError:
            print("Error: The result overflows the python interger limit!")
        except ZeroDivisionError:
            print("Error: Cannot raise 0 to a negative power!")

    # INVALID OPTION PROTECTION
    else:
        print("Invalid selection! Please choose a valid menu operation.")

# END OF CALCULATOR
"""
hey so they dont care about this right?
im kinda confused on what to add now
i might add like a gui later but for now i cannot be fucked in the slighest manner
"""
# Made by Aycifree

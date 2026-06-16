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

# Fresh start: clear the screen right when the program fires up
clear_screen()

while True:
    DIVIDE = False
    MULTIPLY = False
    ADDITION = False
    SUBTRACTION = False
    POWER = False

    print("\n--- CALCULATOR MENU ---")
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
        DIVIDE = True
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")        
        if num2 == 0:
            print("Error: You cannot divide by zero! It breaks the core calculating system!")
        else:
            result = num1 / num2
            if result.is_integer():
                result = int(result)           
            print(f"The result of {num1:g} divided by {num2:g} is {result}")
            
    # MULTIPLICATION SECTION
    elif calculator_input == "mul":
        MULTIPLY = True
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")       
        result = num1 * num2
        if result.is_integer():
            result = int(result)            
        print(f"The result of {num1:g} multiplied by {num2:g} is {result}")
        
    # ADDITION SECTION
    elif calculator_input == "add":
        ADDITION = True
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")
        result = num1 + num2
        if result.is_integer():
            result = int(result)            
        print(f"The result of {num1:g} plus {num2:g} is {result}")
        
    # SUBTRACTION SECTION
    elif calculator_input == "sub":
        SUBTRACTION = True
        num1 = calculate("Enter the first number: ")
        num2 = calculate ("Enter the second number: ")      
        result = num1 - num2
        if result.is_integer():
            result = int(result)            
        print(f"The result of {num1:g} minus {num2:g} is {result}")
        
    # POWER SECTION
    elif calculator_input == "power":
        POWER = True
        num1 = calculate("Enter the first number: ")
        num2 = calculate("Enter the second number: ")      
        result = num1 ** num2
        if result.is_integer():
            result = int(result)            
        print(f"The result of {num1:g} powered by {num2:g} is {result}")

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

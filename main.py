
from utils import show_menu, get_number, save_history, load_history, clear_screen
from operations import *
from colorama import Fore, Style, init
import math

init(autoreset=True)

def basic_operations_menu():
    print("\n--- Basic Operations ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Select an option: ")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    operations = {'1': ('+', add), '2': ('-', subtract),
                  '3': ('*', multiply), '4': ('/', divide)}
    if choice in operations:
        symbol, func = operations[choice]
        result = func(a, b)
        expression = f"{a} {symbol} {b} = {result}"
        print(Fore.GREEN + "Result:", str(result))
        save_history(expression)
    else:
        print(Fore.RED + "Invalid option.")

def advanced_operations_menu():
    print("\n--- Advanced Operations ---")
    print("1. Power")
    print("2. Square root")
    print("3. Modulo")
    print("4. Factorial")
    print("5. Percentage")
    choice = input("Select an option: ")
    if choice == '1':
        a = get_number("Base: ")
        b = get_number("Exponent: ")
        result = power(a, b)
        expression = f"{a} ^ {b} = {result}"
    elif choice == '2':
        a = get_number("Number: ")
        result = square_root(a)
        expression = f"√{a} = {result}"
    elif choice == '3':
        a = get_number("Dividend: ")
        b = get_number("Divisor: ")
        result = modulo(a, b)
        expression = f"{a} % {b} = {result}"
    elif choice == '4':
        a = get_number("Number: ")
        result = factorial(a)
        expression = f"{int(a)}! = {result}"
    elif choice == '5':
        a = get_number("Total: ")
        b = get_number("Percentage: ")
        result = percentage(a, b)
        expression = f"{b}% of {a} = {result}"
    else:
        print(Fore.RED + "Invalid option.")
        return
    print(Fore.GREEN + "Result:", str(result))
    save_history(expression)

def evaluate_expression():
    expr = input("Enter the expression (e.g. 2 + 3 * (4 - 1)): ")
    try:
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        print(Fore.GREEN + "Result:", str(result))
        save_history(f"{expr} = {result}")
    except Exception as e:
        print(Fore.RED + "Expression error:", str(e))

def view_history():
    history = load_history()
    if not history:
        print("History is empty.")
    else:
        print("\n--- History ---")
        for i, op in enumerate(history, 1):
            print(f"{i}. {op}")

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            basic_operations_menu()
        elif choice == '2':
            advanced_operations_menu()
        elif choice == '3':
            evaluate_expression()
        elif choice == '4':
            view_history()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

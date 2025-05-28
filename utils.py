
import json
import os

HISTORY_FILE = "history.json"

def show_menu():
    print("=== CALCULATOR ===")
    print("1. Basic Operations")
    print("2. Advanced Operations")
    print("3. Evaluate Expression")
    print("4. View History")
    print("5. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

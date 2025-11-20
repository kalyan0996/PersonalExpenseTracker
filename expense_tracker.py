#expense_tracker.py[file_name] 
import json 
from datetime import datetime 
import os 
 
# --- 1. Global Data Structure and File Handling --- 
 
# Global list to store all expense dictionaries 
EXPENSES = []  
FILE_NAME = 'expenses.json' 
 
def load_expenses(): 
    """Loads expenses from the JSON file into the global EXPENSES list.""" 
    global EXPENSES 
    if os.path.exists(FILE_NAME): 
        try: 
            with open(FILE_NAME, 'r') as f: 
                # Load the data, default to an empty list if the file is empty 
                EXPENSES = json.load(f) 
            print(f"   Loaded {len(EXPENSES)} expenses from {FILE_NAME}.") 
        except (IOError, json.JSONDecodeError): 
            print("    Error loading expenses file. Starting with an empty list.") 
            EXPENSES = [] 
    else: 
        print(f"    {FILE_NAME} not found. Starting a new expense list.") 
        EXPENSES = [] 
 
def save_expenses(): 
    """Saves the current global EXPENSES list to the JSON file.""" 
    try: 
        with open(FILE_NAME, 'w') as f: 
            json.dump(EXPENSES, f, indent=4) 
        print(f"\n   Successfully saved {len(EXPENSES)} expenses to 
{FILE_NAME}.") 
    except IOError: 
        print("  Error saving expenses to file.") 
 
# --- 2. Add Expense Function --- 
 
def add_expense(): 
    """Prompts user for expense details and adds it to the list.""" 
    print("\n--- ADD NEW EXPENSE ---") 
     
    # Get Amount and ensure it's a valid number 
    while True: 
        try: 
            amount = float(input("Enter amount spent ($): ")) 
            if amount <= 0: 
                print("Amount must be positive.") 
                continue 
            break 
        except ValueError: 
            print("Invalid input. Please enter a numerical amount.") 
 
    # Get Category (could be extended with a predefined list) 
    category = input("Enter category (e.g., Food, Transport, Entertainment): 
").strip().capitalize() 
     
    # Automatically get Date (can be modified for user input if needed) 
    date_str = datetime.now().strftime("%Y-%m-%d") # Format: YYYY-MM-DD 
     
    # Store the information in a dictionary  
    new_expense = { 
        'amount': amount, 
        'category': category, 
        'date': date_str 
    } 
     
    EXPENSES.append(new_expense) 
    print(f"\n    Expense added: ${amount:.2f} on {category} ({date_str})") 
 
# --- 3. View Summary Functions --- 
 
def view_summary(): 
    """Displays overall and category-specific spending summaries.""" 
    print("\n--- EXPENSE SUMMARY ---") 
    if not EXPENSES: 
        print("No expenses recorded yet.") 
        return 
 
    # a) Total Overall Spending  
    total_spending = sum(item['amount'] for item in EXPENSES) 
    print(f"\n   **TOTAL OVERALL SPENDING:** ${total_spending:.2f}") 
 
    # b) Total Spending by Category  
    category_spending = {} 
    for expense in EXPENSES: 
        category = expense['category'] 
        amount = expense['amount'] 
        category_spending[category] = category_spending.get(category, 0) + 
amount 
 
    print("\n      **SPENDING BY CATEGORY:**") 
    for category, total in category_spending.items(): 
        print(f"- {category}: ${total:.2f}") 
 
    # c) Spending over time (Daily Summary)  
    date_spending = {} 
    for expense in EXPENSES: 
        date = expense['date'] 
        amount = expense['amount'] 
        date_spending[date] = date_spending.get(date, 0) + amount 
     
    print("\n             **DAILY SPENDING SUMMARY (last 5 days):**") 
    # Display the last 5 days with spending, sorted by date 
    recent_dates = sorted(date_spending.keys(), reverse=True)[:5] 
    for date in recent_dates: 
        print(f"- {date}: ${date_spending[date]:.2f}") 
 
# --- 4. User Menu and Main Execution --- 
 
def display_menu(): 
    """Shows the user menu options.""" 
    print("\n==================================") 
    print("      PERSONAL EXPENSE TRACKER") 
    print("==================================") 
    print("1. Add New Expense :") 
    print("2. View Summaries  :") 
    print("3. Exit Program    :") 
    print("----------------------------------") 
 
def main(): 
    """Main function to run the expense tracker program.""" 
    load_expenses() # Load existing data at startup [cite: 26] 
 
    while True: 
        display_menu() 
        choice = input("Enter your choice (1-3): ").strip() 
 
        if choice == '1': 
            add_expense() 
        elif choice == '2': 
            view_summary() 
        elif choice == '3': 
            print("\nSaving data before exit...") 
            save_expenses() # Save data before closing [cite: 25] 
") 
print("Goodbye!          
break 
else: 
print("Invalid choice. Please enter 1, 2, or 3.") 
# Run the program 
if __name__ == "__main__": 
main()

from account import *

all_record = []

def create(file,username):

    expense_record = {}

    print("---CREATING EXPENSE RECORD---")

    date = input("Date(MM/DD/YYY):             ")
    expense_record['Date(MM/DD/YYY)'] = date

    budget = float(input("Budget Today:     "))
    expense_record["Budget"] = budget

    print("\nCategories:")
    print("[FOOD] [TRANSPORTATION] [EDUCATION] [ENTERTAINMENT]")
    print("[BILLS] [SHOPPING] [HEALTH] [OTHERS]")

    while True:
        print("\nEnter [q] - 'Quit'")
        category = input("Category:     ").lower()

        if category == "q":
            break

        amount = float(input("Amount:       "))

        if category in expense_record:
            expense_record[category] += amount
        else:
            expense_record[category] = amount

    all_record.append(expense_record)
    print("\nExpense Added!")

    with open(f"{username}.txt", 'a') as file:

        file.write("\n======================================\n")

        balance = 0
        file.write(f"Date:             {expense_record["Date(MM/DD/YYY)"]}\n")
        file.write(f"Budget Today:     {expense_record["Budget"]}\n")

        total = 0
        for category, amount in expense_record.items():
            if category != "Date(MM/DD/YYY)" and category != "Budget" and category != "Day":
                file.write(f"\n {category.capitalize()}:   P{amount}\n")
                total += float(amount)

        file.write(f"\n Total Spend:       P{total}\n")

        if total >= expense_record["Budget"]:
            file.write("Nothing Saved Today :<\n")
        else:
            remain = expense_record["Budget"] - total
            balance += remain
            file.write(f"\n You saved P{balance} today!")
        file.write("\n======================================\n")

def view_expense(username):
    with open(f"{username}.txt") as file:
        print("\n    --- My Spending Report ---")
        for i, line in enumerate(file):
            print(line, end="")



def create(file, username):
    expense_record = {}

    print("---CREATING EXPENSE RECORD---")

    date = input("Date(MM/DD/YYYY):             ")
    expense_record['Date(MM/DD/YYYY)'] = date

    budget = float(input("Budget Today:     "))
    expense_record["Budget"] = budget

    print("\nCategories:")
    print("[FOOD] [TRANSPORTATION] [EDUCATION] [ENTERTAINMENT]")
    print("[BILLS] [SHOPPING] [HEALTH] [OTHERS]")

    while True:
        print("\nEnter [q] - 'Quit'")
        category = input("Category:     ").lower()

        if category == "q":
            break

        amount = float(input("Amount:       "))

        if category in expense_record:
            expense_record[category] += amount
        else:
            expense_record[category] = amount

    print("\nExpense Added!")

    with open(f"{username}.txt", 'a') as file:
        file.write("\n======================================HAHHAHAHHAHAHAHHAH\n")

        balance = 0
        file.write(f"Date:             {expense_record['Date(MM/DD/YYYY)']}\n")
        file.write(f"Budget Today:     {expense_record['Budget']}\n")

        total = 0
        for category, amount in expense_record.items():
            if category not in ["Date(MM/DD/YYYY)", "Budget"]:
                file.write(f"\n {category.capitalize()}:   P{amount}\n")
                total += float(amount)

        file.write(f"\n Total Spend:       P{total}\n")

        if total >= expense_record["Budget"]:
            file.write("Nothing Saved Today :<\n")
        else:
            remain = expense_record["Budget"] - total
            balance += remain
            file.write(f"\n You saved P{balance} today!")
        file.write("\n======================================\n")

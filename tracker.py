# Project: Expense Tracker - Installment 5
# Author: Rose Anne B. Roquino
# Description: An interactive menu for an expense tracker.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

print("Welcome, " + name + "!")

subtotal = 0
count = 0
choice = ""

print("\nMAIN MENU")
print("[1] Add an expense")
print("[2] View all expenses (coming soon)")
print("[3] Show total spent")
print("[4] Exit")

while True:
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count +=1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax

        print("-" * 40)
        print("SUMMARY")
        print("Expenses:\t", count)
        print("Subtotal:\t$", format(subtotal, ".1f"))
        print("Tax (", tax_percent, "%):\t$", format(tax, ".1f"))
        print("Grand total:\t$", format(total, ".1f"))

        if total > budget:
            difference = total - budget
            print(f"Over budget by ${difference:.1f}!")
        elif total > budget * 0.90:
            left = budget - total
            print(f"Careful: only ${left:.1f} left.")
        else:
            left = budget - total
            print(f"Within budget. ${left:.1f} left.")

        print("-" * 40)

    elif choice == "4":
        print("Goodbye, " + name + "!")
        print("-" * 40)
        print("Made by: Rose Anne B. Roquino  |  Installment 5")
        print("=" * 40)
        break

    else:
        print("Please choose 1, 2, 3 or 4.")
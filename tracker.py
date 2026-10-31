# Project: Expense Tracker - Installment 4
# Author: Rose Anne B. Roquino
# Description: A simple landing page for an expense tracker.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("[1] Add an expense\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print("Welcome, " + name + "! Let's log two expenses.")

subtotal = 0

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

average = subtotal / 2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * tax_percent / 100

total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget

print("-" * 40)
print("SUMMARY")
print("- ", item1, ":\t$", amount1)
print("- ", item2, ":\t$", amount2)
print("Subtotal:\t$", subtotal)
print("Average:\t$", average)
print("Tax (", tax_percent, "%):\t$", tax)
print("Grand total:\t$", total)

if over_budget:
    difference = total - budget
    print(f"Over budget by ${difference:.1f}!")
elif total > budget * 0.90:
    left = budget - total
    print(f"Careful: only ${left:.1f} left.")
else:
    left = budget - total
    print(f"Within budget. ${left:.1f} left.")

print("-" * 40)
print("Made by: Rose Anne B.Roquino  |  Installment 4")
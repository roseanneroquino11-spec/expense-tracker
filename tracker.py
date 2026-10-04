# Project: Expense Tracker - Installment 2
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

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount: "))

item2 = input("Second expense? ")
amount2 = float(input("Amount: "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print("- " + item1 + ":\t$" + str(amount1))
print("- " + item2 + ":\t$" + str(amount2))
print("Total spent:\t$" + str(total))
print("Average:\t$" + str(average))
print("-" * 40)

print("Made by: Rose Anne Roquino  |  Installment 2")
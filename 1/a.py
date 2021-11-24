if __name__ == "__main__":
  expenses = []

  with open("expense_report.txt", "r") as expenses_file:
    expenses = [int(x) for x in expenses_file.readlines()]

  unique_expenses = set(expenses)

  for expense in expenses:
    remainder = 2020-expense

    if remainder in unique_expenses and remainder != expense:
      print("Two numbers are " + str(expense) + " and " + str(remainder) + ".")
      print("The result of multiplication is " + str(expense * remainder) + ".")
      break

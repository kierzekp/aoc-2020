if __name__ == "__main__":
  expenses = []

  with open("expense_report.txt", "r") as expenses_file:
    expenses = [int(x) for x in expenses_file.readlines()]

  unique_expenses = set(expenses)

  for expense in expenses:
    remainder = 2020-expense

    # remainder must be covered by two other expenses
    possible_expenses = list(filter(lambda e: e <= remainder, expenses))
    unique_possible_expenses = set(possible_expenses)
    
    for possible_expense in possible_expenses:
      remainder_of_remainder = remainder - possible_expense

      if remainder_of_remainder in unique_possible_expenses and remainder_of_remainder != possible_expense:
          print("Three numbers are " + str(expense) + ", " + str(possible_expense) + " and " + str(remainder_of_remainder) + ".")
          print("The result of multiplication is " + str(expense * possible_expense * remainder_of_remainder) + ".")
          break

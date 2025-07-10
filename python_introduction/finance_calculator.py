income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

monthly_savings = income - expenses

interest_rate = 0.05  # Assuming a 5% annual interest rate

# Calculate projected annual savings with interest
projected_annual_savings = int((monthly_savings*12 + (monthly_savings*0.05*12)) )

print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year, with interest, is : ${projected_annual_savings}")

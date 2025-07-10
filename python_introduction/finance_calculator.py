monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

interest_rate = 0.05  # Assuming a 5% annual interest rate

# Calculate projected annual savings with interest
annual_savings = monthly_savings * 12
projected_annual_savings = int(annual_savings + (annual_savings * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is : ${projected_annual_savings}.")

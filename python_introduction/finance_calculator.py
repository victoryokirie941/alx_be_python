income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

monthly_savings = income - expenses

interest_rate = 0.05  # Assuming a 5% annual interest rate
monthly_interest = monthly_savings * interest_rate


projected_annual_savings = int((monthly_savings + monthly_interest) * 12)

print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year, with interest is : ${projected_annual_savings}")

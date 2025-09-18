monthly_income = float(input("Enter your monthly income: "));
monthly_expenses = float(input("Enter your total monthly expenses: "));

monthly_savings = monthly_income - monthly_expenses;

annual_savings_without_interest = monthly_savings * 12;
projected_annual_savings = annual_savings_without_interest + (annual_savings_without_interest * 0.05);

print(f"\nYour monthly savings: ${monthly_savings:,.2f}");
print(f"Projected annual savings with 5% interest: ${projected_annual_savings:,.2f}");

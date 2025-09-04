# Program to calculate Simple and Compound Interest

principal = float(input("Enter the principal amount (in ₹): "))
rate = float(input("Enter the rate (%): "))
time = float(input("Enter the time in years: "))

# Calculations
amount = principal * (1 + rate / 100) ** time
simple_interest = (principal * rate * time) / 100
compound_interest = amount - principal

# Results
print("\n--- Interest Calculation ---")
print("Principal (in ₹)   = ₹", round(principal, 2))
print("Rate in %          =", str(rate) + "%")
print("Time in years      =", str(time))
print("Simple Interest    = ₹", round(simple_interest, 2))
print("Compound Interest  = ₹", round(compound_interest, 2))
print("Total Amount       = ₹", round(amount, 2))

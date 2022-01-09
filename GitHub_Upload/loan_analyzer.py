import csv
from pathlib import Path

"Part 1: Automate the Calculations. Automate the calculations for the loan portfolio summaries."
loan_costs = [500, 600, 200, 1000, 450]
# @TODO: Calculate the total number of loans in the list.
total_number_of_loans = len(loan_costs)
# @TODO: Calculate the total of all loans in the list.
total_loans_sum = sum(loan_costs)
# @TODO: Calculate the average loan price.
average_loan_price = total_loans_sum/total_number_of_loans
#Print total number of loans, sum of loans, and average loan price
print("The total number of loans is: ", total_number_of_loans)
print("The total sum of the loans is: ", total_loans_sum)
print("The average loan amount is: ", average_loan_price)

"Part 2: Analyze Loan Data. Analyze the loan to determine the investment evaluation."
# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# @TODO: Extract the Future Value and Remaining Months on the loan.
future_value = loan.get("future_value", 0)
remaining_months = loan.get("remaining_months", 0)
# Print each variable.
print("Future value = ", future_value)
print("Remaining months = ", remaining_months)


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Used a minimum required return of 20% as the discount rate.
# Used the **monthly** version of the present value formula
fair_value = future_value / (1+ (0.20/12)) ** remaining_months

# @TODO: Decide if the present value represents the loan's fair value.
# If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price", 0)
if fair_value >= loan_price:
    print("The loan is worth atleast the cost to buy it.")
elif fair_value < loan_price:
    print("The loan is too expensive and not worth the price.")

"Part 3: Perform Financial Calculations."
# Given the following loan data, calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use a function that will be used to calculate present value.
# This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# The function should return the `present_value` for the loan.
def calc_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return present_value

# @TODO: Calculate the present value of the new loan given below.
# Used `annual_discount_rate` of 0.2 for this new loan calculation.
future_value2 = new_loan.get("future_value", 0)
remaining_months = new_loan.get("remaining_months", 0)
annual_discount_rate = 0.20
present_value = calc_present_value(future_value2, remaining_months, annual_discount_rate)
# Print present value of loan
print(f"The present value of the loan is: {present_value}")

"Part 4: Conditionally filter lists of loans"
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#create inexpenive loans list
inexpensive_loans = []
# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for dictionary in loans:
    loan_price = dictionary.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(dictionary)
    
# @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)

"Part 5"
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list
with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
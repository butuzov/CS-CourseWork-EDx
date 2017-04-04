"""
Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

    `balance` - the outstanding balance on the credit card
    `annualInterestRate` - annual interest rate as a decimal
    `monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

    Remaining balance: 813.41

instead of

    Remaining balance: 813.4141998135

So your program only prints out one thing: the remaining balance at the end of the year in the format:

    Remaining balance: 4784.0

A summary of the required math is found below:

"""

# balance = 3329; annualInterestRate = 0.2; expected=310
# balance = 3347; annualInterestRate = 0.2; expected=310

balance = 3926; annualInterestRate = 0.2; expected=360


monthInterestRate = annualInterestRate/12;
minimum = ( ( balance // 12 ) // 10 ) * 10



while True:
    balance_working_copy = balance;

    for _ in range(12):
        balance_working_copy = round( ( 1 + monthInterestRate ) * \
                                ( balance_working_copy - minimum ), 2)

    if balance_working_copy < 0 :
        break;

    minimum += 10;

print('Lowest Payment:', minimum)

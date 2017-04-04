"""
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    `balance` - the outstanding balance on the credit card
    `annualInterestRate` - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

- Monthly interest rate = (Annual interest rate) / 12.0
- Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
- Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
balance = 42; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
# balance = 484; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
# t121balance = 479; annualInterestRate = 0.22; monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12;

for _ in range(12):
    monthly_unpaid_balance = round( balance - (balance * monthlyPaymentRate), 2 );
    monthly_interest = round( monthly_unpaid_balance * monthlyInterestRate, 2);
    balance = round( monthly_unpaid_balance + monthly_interest, 2)

print( 'Remaining balance: {}'.format(balance) );

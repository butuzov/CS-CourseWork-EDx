#The sales tax for restaurant purchases in Atlanta is 8%, meaning that
#the cost of a purchase at a restaurant is the cost of the meal plus
#8%. It's also customary to tip 20% of the meal cost before tax is added.
#
#Below, follow the instructions to calculate the tax and tip amount for a
#meal you've purchased.

#Modify the variable, tax, so that it's equal to 8% as a decimal value.
#Then modify the variable, tip, so that it's equal to 20% as a decimal value.
#Use mathematical operators -- don't just set them equal to the right values,
#and remember to convert the percents to decimals.
#
#Once you've correctly modified the tax and tip variables, recalculate the
#total price of the meal after each is applied. Remember, mealWithTax should
#be the price of the meal plus 8%, while meal total should be the price of
#the meal, plus 8% of the price of the meal for tax, plus 20% of the price
#of the meal for tip. Use the tax and tip variables to calculate the total
#costs.

mealCost = 21.91
# change the tax variable below
tax = mealCost * 0.08
# change the tip variable below
tip = mealCost * 0.2

#Apply the tax to mealCost.
mealWithTax = mealCost + tax
#Apply the tip to mealWithTax. Remember, tip is calculated on the original
#cost of the meal, not the cost after tax is added.
mealTotal = mealWithTax + tip


#Do not modify the print statements below. Note that we use round() in these
#lines to round your answer to the nearest cent since that's what restaurants
#do.
print("Initial meal cost:", round(mealCost, 2))
print("Meal cost after tax:", round(mealWithTax, 2))
print("Meal cost after tax and tip:", round(mealTotal, 2))

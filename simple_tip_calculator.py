tmp_in = input("What is the meal cost? $")
meal_cost = float(tmp_in)

tmp_in = input("What is the tip percentage: ")
tip_percentage = float(tmp_in)

tip_amount = (tip_percentage / 100) * meal_cost

total = tip_amount + meal_cost

print(f"Meal cost: ${meal_cost:.2f}")
print(f"Tip percentage: {tip_percentage}%")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount due: ${total:.2f}")
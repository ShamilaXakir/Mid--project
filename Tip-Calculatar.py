
def calculate_tip(total_bill, tip_percentage):
    tip_amount = (total_bill * tip_percentage) / 100
    total_amount = total_bill + tip_amount
    return tip_amount, total_amount

print("Welcome TO The Tip Calculater!")
total_bill = float (input("Enter the total bill amount: "))
tip_percentage = float (input("Enter the tip percentage: "))

tip_amount, total_amount = calculate_tip(total_bill, tip_percentage)

print(f"\nTip Amount: Rs.{tip_amount:.2f}")
print(f"Total Amount (including tip): Rs.{total_amount:.2f}")

print("\nProject Developed by:Ruqayya, Saliha and Shamila Zakir")
units = int(input("Enter units consumed: "))
rate_per_unit = 5
total_bill = units * rate_per_unit
if total_bill >1000:
    discount = total_bill*0.10
else:
    discount = 0
final_bill = total_bill - discount
print("\nUnits Consumed:", units)
print("Total Bill: ₹", total_bill)
print("dicount applied :",discount)
print("final bill:",final_bill)

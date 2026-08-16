# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
coffee_price = 3.50
coffee_qty = 2
coffee_total = coffee_price * coffee_qty

muffin_price = 2.10
muffin_qty = 3
muffin_total = muffin_price * muffin_qty

Water_price = 1.05 
Water_qty = 4
Water_total = Water_price * Water_qty

subtotal = (coffee_price * coffee_qty)+ (muffin_price * muffin_qty)+(Water_price*Water_qty)
tax = subtotal * 0.06
total = subtotal+tax

print("==========RECEIPT==========")
 "ITEM\t\tprice\tQty\tTotal\n"
  
 

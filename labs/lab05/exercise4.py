item_name = input("Enter the item name: ")
price = float(input("Enter the price: "))

quantity = 3
tax_rate = 0.06

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Item Information:")
print(f"Item Name: {item_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {total:.2f}")   
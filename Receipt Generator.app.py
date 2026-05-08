total_price = 0
items_count = int(input("How many items did you buy? "))

# This loop runs as many times as the user said
for i in range(items_count):
    # We use f-strings to show "Item 1", "Item 2", etc.
    price = int(input(f"Enter price for item {i+1}: "))
    total_price = total_price + price

print("-" * 20)
print(f"SUBTOTAL: RM {total_price}")
tax = total_price * 0.06
print(f"TAX (6%): RM {tax:.2f}") # .2f rounds to 2 decimal places!
print(f"TOTAL: RM {total_price + tax}")
print("-" * 20)

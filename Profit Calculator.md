total_profit = 0

print("--- SARAH'S BOUTIQUE PROFIT CALCULATOR ---")
item_count = int(input("How many different types of items were sold? "))

for i in range(item_count):
    print(f"\nProcessing Item #{i+1}:")
    
    name = input("  Product Name: ").strip().title()
    price = float(input(f"  What did {name} sell for? RM "))
    cost = float(input(f"  How much did it cost to make? RM "))
    quantity = int(input(f"  How many {name}s were sold? "))
    
    profit_per_item = price - cost
    total_item_profit = profit_per_item * quantity
    
    total_profit = total_profit + total_item_profit
    
    print(f"  > Profit for this batch: RM {total_item_profit:.2f}")


commission = total_profit * 0.15
final_take_home = total_profit - commission

print("\n" + "="*40)
print("FINAL SALES SUMMARY")
print("="*40)
print(f"TOTAL GROSS PROFIT:   RM {total_profit:.2f}")
print(f"MARKET FEE (15%):     RM {commission:.2f}")
print("-" * 20)
print(f"SARAH'S TAKE-HOME:    RM {final_take_home:.2f}")
print("="*40)

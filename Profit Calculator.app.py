import streamlit as st

st.title("--- SARAH'S BOUTIQUE PROFIT CALCULATOR ---")

# Use sidebar or columns for inputs
item_count = st.number_input("How many different types of items were sold?", min_value=1, step=1)

total_profit = 0

for i in range(int(item_count)):
    st.subheader(f"Processing Item #{i+1}")
    name = st.text_input(f"Product Name (Item {i+1})", key=f"name_{i}")
    price = st.number_input(f"What did {name} sell for? RM", key=f"price_{i}")
    cost = st.number_input(f"How much did it cost to make? RM", key=f"cost_{i}")
    quantity = st.number_input(f"How many {name}s were sold?", step=1, key=f"qty_{i}")
    
    profit_per_item = price - cost
    total_item_profit = profit_per_item * quantity
    total_profit += total_item_profit

if st.button("Calculate Final Summary"):
    commission = total_profit * 0.15
    final_take_home = total_profit - commission

    st.divider()
    st.header("FINAL SALES SUMMARY")
    st.write(f"**TOTAL GROSS PROFIT:** RM {total_profit:.2f}")
    st.write(f"**MARKET FEE (15%):** RM {commission:.2f}")
    st.success(f"**SARAH'S TAKE-HOME: RM {final_take_home:.2f}**")


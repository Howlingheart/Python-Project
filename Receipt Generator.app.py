import streamlit as st

st.title("Receipt Generator")

total_price = 0
# Use st.number_input instead of input()
items_count = st.number_input("How many items did you buy?", min_value=1, step=1)

# This loop runs as many times as the user said
for i in range(int(items_count)):
    # We use st.number_input with a unique 'key' so the web knows which box is which
    price = st.number_input(f"Enter price for item {i+1}: RM", key=f"price_{i}")
    total_price = total_price + price

st.divider() # Makes a nice line on the web

st.write(f"### SUBTOTAL: RM {total_price:.2f}")
tax = total_price * 0.06
st.write(f"### TAX (6%): RM {tax:.2f}") 
st.success(f"## TOTAL: RM {total_price + tax:.2f}")

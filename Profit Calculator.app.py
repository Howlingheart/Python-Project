import streamlit as st

# 1. Setup Currency Rates (Manually updated for simplicity)
currencies = {
    "RM (Malaysia)": 4.72,
    "USD (USA)": 1.0,
    "SGD (Singapore)": 1.35,
    "JPY (Japan)": 155.80,
    "KRW (South Korea)": 1365.0
}

st.set_page_config(page_title="Universal Profit Calc", page_icon="💰")

st.title("🛍️ Universal Profit Calculator")
st.write("Calculate your earnings in any currency.")

# 2. Sidebar for Settings
st.sidebar.header("Global Settings")
selected_currency = st.sidebar.selectbox("Select Currency", list(currencies.keys()))
currency_symbol = selected_currency.split(" ")[0]

# 3. Main Input Section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Item Details")
    item_name = st.text_input("Item Name", placeholder="e.g., Silk Scarf")
    selling_price = st.number_input(f"Selling Price ({currency_symbol})", min_value=0.0, step=1.0)
    item_cost = st.number_input(f"Item Cost ({currency_symbol})", min_value=0.0, step=1.0)

with col2:
    st.subheader("Fees & Taxes")
    platform_fee_pct = st.number_input("Platform Fee (%)", min_value=0.0, max_value=100.0, value=5.0)
    tax_pct = st.number_input("Tax/SST (%)", min_value=0.0, max_value=100.0, value=0.0)

# 4. The Logic (The "Brain")
platform_fee_amount = selling_price * (platform_fee_pct / 100)
tax_amount = (selling_price - item_cost) * (tax_pct / 100) if selling_price > item_cost else 0
total_profit = selling_price - item_cost - platform_fee_amount - tax_amount

# 5. Results Display
st.divider()

if selling_price > 0:
    c1, c2, c3 = st.columns(3)
    c1.metric("Gross Profit", f"{currency_symbol} {selling_price - item_cost:.2f}")
    c2.metric("Total Fees", f"- {currency_symbol} {platform_fee_amount + tax_amount:.2f}", delta_color="inverse")
    
    # Final Result Color Coding
    if total_profit > 0:
        c3.metric("Net Profit", f"{currency_symbol} {total_profit:.2f}")
        st.success(f"✅ Success! You make **{currency_symbol} {total_profit:.2f}** per {item_name}")
    else:
        c3.metric("Net Profit", f"{currency_symbol} {total_profit:.2f}")
        st.error(f"⚠️ Warning: This item is currently at a loss of {abs(total_profit):.2f}")
else:
    st.info("Enter a selling price to see the calculation.")

# 6. Technical Export (Optional)
st.sidebar.download_button("Export as Report", f"Item: {item_name}\nProfit: {total_profit}", file_name="report.txt")

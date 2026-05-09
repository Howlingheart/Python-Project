import streamlit as st

# 1. Setup
st.set_page_config(page_title="My Custom Game Tracker", page_icon="🕹️")

# 2. The Setup Wizard (User fills this out)
st.sidebar.header("🛠️ Initial Setup")
game_name = st.sidebar.text_input("What is your game?", "Blue Archive")
currency_name = st.sidebar.text_input("What is the currency name?", "Pyroxenes")
currency_emoji = st.sidebar.selectbox("Pick an icon", ["💎", "🪙", "🎫", "💰", "⚔️", "⭐"])

st.sidebar.divider()

# 3. The Live Data
st.sidebar.subheader(f"Your {game_name} Wallet")
current_balance = st.sidebar.number_input(f"Current {currency_name}", min_value=0, value=0)
reserve_limit = st.sidebar.number_input(f"Minimum {currency_name} to keep", min_value=0, value=0)

# 4. Main App Interface
st.title(f"{currency_emoji} {game_name} Manager")
st.write(f"This tool is currently configured to track **{currency_name}**.")

# 5. The "Should I Spend?" Calculator
st.header("🛒 Spending Planner")
item_to_buy = st.text_input("What do you want to buy/pull?", placeholder="e.g. Limited Banner")
cost = st.number_input(f"Cost of {item_to_buy} ({currency_name})", min_value=0)

if st.button("Calculate Financial Impact"):
    remaining = current_balance - cost
    
    if remaining >= reserve_limit:
        st.success(f"Go for it! You'll still have {remaining} {currency_name} left. ✅")
    else:
        shortfall = abs(remaining - reserve_limit)
        st.error(f"Stop! You need {shortfall} more {currency_name} to stay above your limit. ❌")

# 6. Your Personal Signature
st.divider()
st.caption(f"Created by Howlingheart | {game_name} Strategy Tool")

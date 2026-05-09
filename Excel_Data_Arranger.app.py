import pandas as pd
import streamlit as st
import io

# --- 1. APP INTERFACE SETUP ---
st.set_page_config(page_title="Excel Data Arranger", page_icon="📊")
st.title("📊 Excel Data Arranger")
st.write("Upload your messy Excel file below to clean spaces, fix 'RM' pricing, and calculate profit instantly.")

# --- 2. THE UNIVERSAL UPLOADER ---
uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])

if uploaded_file is not None:
    # Load the data
    df = pd.read_excel(uploaded_file)
    st.info("File uploaded successfully!")

    # --- 3. THE CLEANING ENGINE ---
    # Delete empty rows (The "Ghost" rows)
    df = df.dropna(how='all')

    # Trim spaces in 'Product Name' if it exists
    if 'Product Name' in df.columns:
        df['Product Name'] = df['Product Name'].astype(str).str.strip()

    # The "Money Fixer" for Selling and Cost Price
    for col in ['Selling Price', 'Cost Price']:
        if col in df.columns:
            # Remove 'RM', commas, and extra spaces, then turn into a number
            df[col] = df[col].astype(str).str.replace('RM', '').str.replace(',', '').str.strip()
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # --- 4. CALCULATE PROFIT ---
    if 'Selling Price' in df.columns and 'Cost Price' in df.columns:
        df['Profit'] = df['Selling Price'] - df['Cost Price']

    # --- 5. THE "PRETTY" DISPLAY ---
    # We make a copy to add 'RM' back for the browser view
    display_df = df.copy()

    #This line shifts the numbering to starts at 1 instead of 0
    display_df.index = display_df.index + 1
    
    for col in ['Selling Price', 'Cost Price', 'Profit']:
        if col in display_df.columns:
            display_df[col] = 'RM ' + display_df[col].map('{:,.2f}'.format)

    st.write("### ✨ Cleaned Data Preview")
    st.dataframe(display_df, use_container_width=True)

    # --- 5.5 NEW SUMMARY SECTION STARTS HERE ---
    st.divider() 
    st.subheader("💰 Business Summary")
    
    # We calculate totals using 'df' because it has pure numbers
    total_sales = df['Selling Price'].sum()
    total_cost = df['Cost Price'].sum()
    total_profit = df['Profit'].sum()

    # This creates three side-by-side boxes
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"RM {total_sales:,.2f}")
    col2.metric("Total Cost", f"RM {total_cost:,.2f}")
    col3.metric("Total Profit", f"RM {total_profit:,.2f}", delta=f"{total_profit:,.2f}")
    st.divider()
    # --- SUMMARY SECTION ENDS HERE ---

    # --- 6. EXPORT / DOWNLOAD ---
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    
    st.download_button(
        label="Download Arranged Excel 📥",
        data=buffer.getvalue(),
        file_name="arranged_data.xlsx",
        mime="application/vnd.ms-excel"
    )

else:
    st.warning("Please upload an Excel file to begin.")

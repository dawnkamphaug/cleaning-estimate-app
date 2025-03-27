import streamlit as st
st.set_page_config(page_title="Dust Busters Estimate App", page_icon="favicon.png")

# Function to calculate cleaning estimates
def calculate_estimates(square_footage, dirt_code, bedrooms, bathrooms, kids, pets):
    deep_cleaning_price = (
        4.16 + (0.11 * square_footage) +
        (27.77 * dirt_code) + (13.17 * bedrooms) +
        (27.32 * bathrooms) + (13.66 * kids) + (13.66 * pets)
    )

    # Apply minimum price of $124.26
    deep_cleaning_price = max(124.26, deep_cleaning_price)
    weekly_price = max(124.26, deep_cleaning_price * 0.45)
    biweekly_price = max(124.26, deep_cleaning_price * 0.60)
    monthly_price = max(124.26, deep_cleaning_price * 0.75)

    return deep_cleaning_price, weekly_price, biweekly_price, monthly_price

# Streamlit UI
st.title("🧼 Cleaning Estimate Calculator")

# Input fields
square_footage = st.number_input("Square Footage", min_value=0, value=1000)
dirt_code = st.number_input("Dirt Code (1-5)", min_value=1, max_value=5, value=1)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=2)
kids = st.number_input("Number of Kids", min_value=0, value=0)
pets = st.number_input("Number of Pets", min_value=0, value=0)

# Calculate estimate
deep, weekly, biweekly, monthly = calculate_estimates(square_footage, dirt_code, bedrooms, bathrooms, kids, pets)

st.subheader("🧾 Estimate Breakdown:")
st.write(f"**Deep Cleaning Price:** ${deep:.2f}")
st.write(f"**Weekly Price:** ${weekly:.2f}")
st.write(f"**Bi-Weekly Price:** ${biweekly:.2f}")
st.write(f"**Monthly Price:** ${monthly:.2f}")

# Mobile-friendly layout with Streamlit's built-in responsiveness
st.caption("🔹 Dust Busters Cleaning Service - Internal Use Only")

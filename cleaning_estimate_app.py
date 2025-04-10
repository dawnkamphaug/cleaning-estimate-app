import streamlit as st

st.set_page_config(page_title="Dust Busters Estimate App", page_icon="🧽")

st.title("🧼 Dust Busters Estimate App")
st.markdown("Enter the home details below to see your custom quote!")

# Input fields
sqft = st.number_input("Square Footage", min_value=0)
dirt = st.slider("Dirt Level (1–8)", min_value=1, max_value=8, value=4)
beds = st.number_input("Bedrooms", min_value=0)
baths = st.number_input("Bathrooms", min_value=0.0, step=0.5)
pets = st.number_input("Pets", min_value=0)

# Pricing formulas with min price of $124.26
min_price = 124.26

deep_clean = max(min_price, 10.69 + 0.112 * sqft + 28.15 * dirt + 13.57 * beds + 26.12 * baths + 10.98 * pets)
weekly = max(min_price, 69.90 + 0.024 * sqft + 6.40 * dirt - 0.58 * beds + 3.91 * baths + 6.12 * pets)
biweekly = max(min_price, 18.48 + 0.050 * sqft + 12.68 * dirt + 4.86 * beds + 12.65 * baths + 4.62 * pets)
monthly = max(min_price, 6.52 + 0.067 * sqft + 16.82 * dirt + 8.10 * beds + 15.60 * baths + 6.56 * pets)

# Results
st.subheader("Estimated Prices:")
st.write(f"💎 **Deep Clean**: ${deep_clean:.2f}")
st.write(f"🧼 **Weekly**: ${weekly:.2f}")
st.write(f"🔁 **Bi-Weekly**: ${biweekly:.2f}")
st.write(f"📅 **Monthly**: ${monthly:.2f}")


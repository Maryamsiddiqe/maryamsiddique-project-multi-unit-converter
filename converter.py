import streamlit as st

st.set_page_config(page_title="✨ Multi-Unit Converter", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        body { background-color: #eef2f3; font-family: 'Arial', sans-serif; }
        
        .header-box {
            border-radius: 15px;
            padding: 20px;
            background: linear-gradient(135deg, #ff7e5f, #feb47b);
            text-align: center;
            box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .header-box h1 {
            color: white;
            margin: 0;
            font-size: 36px;
            font-weight: bold;
        }

        .stTabs [data-baseweb="tab-list"] button {
            background-color: #0073e6;
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            transition: 0.3s;
        }
        
        .stTabs [data-baseweb="tab-list"] button:hover {
            background-color: #005bb5;
            transform: scale(1.05);
        }

        .stButton>button {
            background: linear-gradient(135deg, #4CAF50, #8BC34A);
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #388E3C, #689F38);
            transform: scale(1.08);
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }

        h3 { color: #ff4500; text-align: center; font-size: 22px; }
        h4 { color: #0073e6; text-align: center; font-size: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-box"><h1> Multi-Unit Converter</h1></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📏 Length", "🌡 Temperature", "💰 Currency"])

# LENGTH CONVERTER
with tab1:
    st.markdown('<div class="card"><h3>📏 Length Converter</h3>', unsafe_allow_html=True)
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
                    "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701}
    
    length_value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1)
    from_length = st.selectbox("From", list(length_units.keys()))
    to_length = st.selectbox("To", list(length_units.keys()))
    
    if st.button("🔄 Convert Length"):
        length_result = length_value * length_units[to_length] / length_units[from_length]
        st.success(f"✅ Converted: {length_result:.4f} {to_length}")
    
    st.markdown("</div>", unsafe_allow_html=True)

# TEMPERATURE CONVERTER
with tab2:
    st.markdown('<div class="card"><h3>🌡 Temperature Converter</h3>', unsafe_allow_html=True)
    
    temp_value = st.number_input("Enter Temperature", value=0.0, step=0.1)
    temp_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
        if from_unit == "Fahrenheit":
            return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
        if from_unit == "Kelvin":
            return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)
    
    if st.button("🔄 Convert Temperature"):
        temp_result = convert_temperature(temp_value, temp_from, temp_to)
        st.success(f"✅ Converted: {temp_result:.2f} {temp_to}")
    
    st.markdown("</div>", unsafe_allow_html=True)

# CURRENCY CONVERTER
with tab3:
    st.markdown('<div class="card"><h3>💰 Currency Converter</h3>', unsafe_allow_html=True)
    
    currency_rates = {
        "USD (United States Dollar)": 1, "EUR (Euro)": 0.91, "GBP (British Pound)": 0.76, 
        "PKR (Pakistani Rupee)": 277.50, "INR (Indian Rupee)": 83.00, "AUD (Australian Dollar)": 1.55, 
        "CAD (Canadian Dollar)": 1.35, "SGD (Singapore Dollar)": 1.34, "JPY (Japanese Yen)": 150.20, 
        "CNY (Chinese Yuan)": 7.14, "AED (UAE Dirham)": 3.67, "SAR (Saudi Riyal)": 3.75
    }
    
    currency_value = st.number_input("Enter Amount", min_value=0.0, value=1.0, step=0.1)
    from_currency = st.selectbox("From", list(currency_rates.keys()))
    to_currency = st.selectbox("To", list(currency_rates.keys()))
    
    if st.button("🔄 Convert Currency"):
        currency_result = currency_value * currency_rates[to_currency] / currency_rates[from_currency]
        st.success(f"✅ Converted: {currency_result:.2f} {to_currency}")
    
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h4>🔹 Created by Maryam Siddique 🔹</h4>", unsafe_allow_html=True)

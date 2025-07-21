import streamlit as st

def risk_based_futures_calculator(entry_price, target_price, stoploss_price, margin, max_loss, position_type='long'):
    risk_per_unit = abs(entry_price - stoploss_price)
    if risk_per_unit == 0:
        return {"error": "SL tidak boleh sama dengan entry (risk per unit = 0)."}

    coin_amount = max_loss / risk_per_unit
    position_size = coin_amount * entry_price
    leverage = position_size / margin

    if position_type == 'long':
        profit = (target_price - entry_price) * coin_amount
    elif position_type == 'short':
        profit = (entry_price - target_price) * coin_amount
    else:
        return {"error": "Tipe posisi salah. Gunakan 'long' atau 'short'."}

    return {
        "Profit jika TP tercapai": round(profit, 2),
        "Kerugian jika SL tercapai": round(max_loss, 2),
        "Leverage": round(leverage, 2),
        "Jumlah koin": round(coin_amount, 2),
        "Ukuran posisi (USD)": round(position_size, 2)
    }

# ===============================
# Streamlit UI
st.title("📈 Kalkulator Risiko Trading Futures")

with st.form("futures_form"):
    position_type = st.selectbox("Pilih posisi", ["long", "short"])
    entry_price = st.number_input("Harga Entry", value=0.01385, format="%.8f")
    target_price = st.number_input("Target (TP)", value=0.0162, format="%.8f")
    stoploss_price = st.number_input("Stop Loss (SL)", value=0.013385, format="%.8f")
    margin = st.number_input("Margin (USD)", value=30.0)
    max_loss = st.number_input("Toleransi Kerugian Maksimum (USD)", value=6.2)

    submitted = st.form_submit_button("Hitung")

if submitted:
    result = risk_based_futures_calculator(
        entry_price, target_price, stoploss_price, margin, max_loss, position_type
    )

    st.subheader("📊 Hasil Perhitungan")
    if "error" in result:
        st.error(result["error"])
    else:
        for key, val in result.items():
            st.write(f"**{key}**: ${val}")

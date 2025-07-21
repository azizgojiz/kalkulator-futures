def risk_based_futures_calculator(entry_price, target_price, stoploss_price, margin, max_loss, position_type='long'):
    risk_per_unit = abs(entry_price - stoploss_price)
    coin_amount = max_loss / risk_per_unit
    position_size = coin_amount * entry_price
    leverage = position_size / margin

    if position_type == 'long':
        profit = (target_price - entry_price) * coin_amount
    elif position_type == 'short':
        profit = (entry_price - target_price) * coin_amount
    else:
        return {"error": "Invalid position type. Use 'long' or 'short'."}

    return {
        "max_profit_if_tp_hit": round(profit, 2),
        "max_loss_if_sl_hit": round(max_loss, 2),
        "calculated_leverage": round(leverage, 2),
        "coin_amount": round(coin_amount, 2),
        "position_size": round(position_size, 2)
    }

# 🚀 MAIN PROGRAM
if __name__ == "__main__":
    print("=== Kalkulator Risiko Trading Futures ===")
    position_type = input("Masukkan posisi (long/short): ").strip().lower()
    entry_price = float(input("Masukkan harga entry: "))
    target_price = float(input("Masukkan harga target (TP): "))
    stoploss_price = float(input("Masukkan harga stop loss (SL): "))
    margin = float(input("Masukkan nilai margin (USD): "))
    max_loss = float(input("Masukkan toleransi kerugian maksimum (USD): "))

    result = risk_based_futures_calculator(
        entry_price=entry_price,
        target_price=target_price,
        stoploss_price=stoploss_price,
        margin=margin,
        max_loss=max_loss,
        position_type=position_type
    )

    print("\n📊 Hasil Perhitungan:")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

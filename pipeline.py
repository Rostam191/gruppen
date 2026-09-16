# ... load_data funktionen här ...

def transform_data(data):
    """Konverterar temperaturen från Celsius till Fahrenheit."""
    if data is None:
        return None
    for row in data:
        celsius = row['temperature']
        fahrenheit = (celsius * 9/5) + 32
        row['temperature_f'] = round(fahrenheit, 1)
    print("✅ Data transformerad (Celsius → Fahrenheit)")
    return data
print("Laddar data från fil...")

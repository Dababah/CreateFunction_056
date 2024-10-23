def konversi_suhu(nilai, satuan):
    # Mengonversi Celsius ke Fahrenheit
    if satuan.upper() == 'C':
        nilai_konversi = (nilai * 9/5) + 32  
        satuan_konversi = 'F'
    # Mengonversi Fahrenheit ke Celsius    
    elif satuan.upper() == 'F':
        nilai_konversi = (nilai - 32) * 5/9  
        satuan_konversi = 'C'
    else:
        raise ValueError("Satuan harus 'C' untuk Celsius atau 'F' untuk Fahrenheit.")
    
    return nilai_konversi, satuan_konversi

# Contoh penggunaan:
suhu_dalam_fahrenheit = konversi_suhu(60, 'C')
suhu_dalam_celsius = konversi_suhu(212, 'F')

print(f"60°C adalah {suhu_dalam_fahrenheit[0]}°{suhu_dalam_fahrenheit[1]}")
print(f"212°F adalah {suhu_dalam_celsius[0]}°{suhu_dalam_celsius[1]}")

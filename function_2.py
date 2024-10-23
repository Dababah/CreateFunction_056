import math

# Fungsi lambda untuk menghitung luas lingkaran

luas_lingkaran = lambda jari_jari: math.pi * jari_jari ** 2

# Contoh penggunaan:

jari_jari = 7
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas_lingkaran(jari_jari):.2f}")

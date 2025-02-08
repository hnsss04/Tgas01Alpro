# Diketahui soal

hargabeliawal = 650000
beratawal = 25
hargasekarang = 685000
hargabelikedua = 685000
beratkedua =  15
hargakeduanaik = 715000

#Hitung Soal Pertama

modalawal = hargabeliawal * beratawal
keuntunganpertama = (hargasekarang * beratawal) - modalawal
persen_keuntunganpertama =  (keuntunganpertama/modalawal) * 100

print(f"Keuntungan pertama dalam rupiah: Rp {keuntunganpertama:,}")
print(f"Keuntungan pertama dalam persen: {persen_keuntunganpertama:.2f}%")

print("------")


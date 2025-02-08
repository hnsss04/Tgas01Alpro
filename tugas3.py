import math

# Diketahui
modal_awal = 200_000_000  
target_akhir = 400_000_000  
bunga_tahunan = 0.1  

# Rumus Menghitung waktu yang dibutuhkan

t = math.log(target_akhir/modal_awal) /math.log(1 + bunga_tahunan)


# Hasil hitung 
print(f"Waktu yang dibutuhkan agar tercapai 400jt adalah {t:.2f} tahun")
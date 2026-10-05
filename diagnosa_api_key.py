import hmac
from main import settings

# Nilai yang kita kirim dari Postman
req_key = 'CMoeAa-06uwbtoWCTRbfNL1Acqx3P510ajUNTt28js'

# Nilai yang dibaca server dari .env
env_key = settings.internal_api_key

print("=" * 70)
print("PANJANG:")
print(f"  Yang dikirim (Postman)    : {len(req_key)} karakter")
print(f"  Yang dibaca server (.env) : {len(env_key)} karakter")
print()

print("=" * 70)
print("PERBANDINGAN KARAKTER PER KARAKTER:")
print(f"{'Pos':>4} | {'req':^8} | {'kode':>6} | {'env':^8} | {'kode':>6} | Status")
print("-" * 70)

max_len = max(len(req_key), len(env_key))
beda_ditemukan = False

for i in range(max_len):
    a = req_key[i] if i < len(req_key) else '<kosong>'
    b = env_key[i] if i < len(env_key) else '<kosong>'
    kode_a = ord(a) if len(a) == 1 else '-'
    kode_b = ord(b) if len(b) == 1 else '-'
    
    if a != b:
        status = "  <<< BEDA!"
        beda_ditemukan = True
    else:
        status = ""
    
    print(f"{i:>4} | {a!r:>8} | {kode_a:>6} | {b!r:>8} | {kode_b:>6} |{status}")

print("=" * 70)
if not beda_ditemukan:
    print("Semua karakter SAMA, tapi hmac.compare_digest tetap False?")
    print("Kemungkinan masalah encoding Unicode vs UTF-8 di .env.")
else:
    print(">>> Ketemu posisi yang beda! Lihat baris dengan '<<< BEDA!'")

print()
print("HASIL PERBANDINGAN hmac.compare_digest:")
print(f"  {hmac.compare_digest(req_key, env_key)}")
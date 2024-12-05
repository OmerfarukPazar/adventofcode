import re

# Dosyayı aç ve işlemleri uygula
with open("puzzle3/puzzle3_input.txt", "r") as input_file:
    # Dosya içeriğini bir string olarak oku
    content = input_file.read()

# Patternler
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d+),(\d+)\)"

# 1. Tüm mul'ları dikkate alarak toplam
all_mul_matches = re.findall(mul_pattern, content)
all_mul_total = sum(int(x) * int(y) for x, y in all_mul_matches)

# 2. do() ve don't() ifadelerini dikkate alarak toplam
mul_enabled = True
conditional_total = 0

# Tüm ifadeleri sırayla işle
instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", content)

for instr in instructions:
    if re.fullmatch(do_pattern, instr):
        # do() bulundu, mul'lar etkinleştirildi
        mul_enabled = True
    elif re.fullmatch(dont_pattern, instr):
        # don't() bulundu, mul'lar devre dışı bırakıldı
        mul_enabled = False
    elif re.fullmatch(mul_pattern, instr) and mul_enabled:
        # Etkin bir mul(x, y) işlemi varsa, çarpımı hesapla ve ekle
        x, y = map(int, re.findall(r"\d+", instr))
        conditional_total += x * y

# Sonuçları yazdır
print("Tüm mul toplamı (do() ve don't() dikkate alınmadan):", all_mul_total)
print("Şartlı toplam (do() ve don't() dikkate alındı):", conditional_total)

import math
leiviska = float(input("Anna leiviska"))
naula = float(input("Anna naula"))
luoti = float(input("Anna luoti"))

kaikki_naulat = leiviska * 20 + naula
kaikki_luodit = kaikki_naulat * 32 + luoti

grammat = kaikki_luodit * 13.3
kilot = grammat / 1000

print(f"kilogrammat {math.floor(kilot)} ja grammat {round((kilot - math.floor(kilot)) * 1000, 2)}")

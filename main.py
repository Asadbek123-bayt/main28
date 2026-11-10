import math

def pifagor_gipotenuza(katet_a, katet_b):
    print(f"📐 Toʻgʻri burchakli uchburchak katetlari: a = {katet_a}, b = {katet_b}")
    gipotenuza_c = math.sqrt(katet_a ** 2 + katet_b ** 2)
    S = (katet_a * math.sqrt(katet_b ** 2)) / 2

    print(f"   Pifagor formulasi boʻyicha gipotenuza: c = {gipotenuza_c:.2f}")
    print(f"   Uchburchak yuzi: S = {S:.1f} kv. birlik")
    print("-" * 50 + "\n")

def shar_olchamlari(radius):
    print(f"🔮 Shar radiusi: r = {radius}")
    hajm = (4 / 3) * math.pi * (radius ** 3)
    sirt_yuzi = 4 * math.pi * (radius ** 2)

    print(f"   Shar hajmi (V): {hajm:.2f} kub birlik")
    print(f"   Sirtining yuzi (S): {sirt_yuzi:.2f} kv. birlik")
    print("-" * 50 + "\n")

def arifmetik_progressiya(a1, d, n):
    print(f"🔢 Arifmetik progressiya: birinchi had a1 = {a1}, ayirma d = {d}")
    an = a1 + (n - 1) * d
    Sn = ((a1 + an) * n) / 2

    print(f"   Progressiyaning {n}-hadi (a{n}): {an}")
    print(f"   Dastlabki {n} ta hadining yigʻindisi (S{n}): {Sn}")
    print("-" * 50 + "\n")

def mexanik_energiya(mass_kg, tezlik_ms, balandlik_m):
    g = 9.81
    print(f"🏃 Jism parametrlari: massasi = {mass_kg} kg, tezligi = {tezlik_ms} m/s, balandligi = {balandlik_m} m")
    Ek = (mass_kg * (tezlik_ms ** 2)) / 2
    Ep = mass_kg * g * balandlik_m
    E_jami = Ek + Ep

    print(f"   Kinetik energiya (Ek): {Ek:.2f} J (Joul)")
    print(f"   Potensial energiya (Ep): {Ep:.2f} J (Joul)")
    print(f"   Toʻla mexanik energiya: {E_jami:.2f} J")
    print("-" * 50 + "\n")

def gaz_bosimi_hisobla(hajm_m3, mol, harorat_selisiy):
    R = 8.314
    T_kelvin = harorat_selisiy + 273.15

    print(f"💨 Gaz holati: hajmi = {hajm_m3} m³, miqdori = {mol} mol, harorat = {harorat_selisiy}°C")
    P_bosim = (mol * R * T_kelvin) / hajm_m3

    print(f"   Harorat Kelvin shkalasida (T): {T_kelvin:.2f} K")
    print(f"   Mendeleyev-Klapeyron boʻyicha bosim (P): {P_bosim:.2f} Pa (Paskal)")
    print("-" * 50 + "\n")

print("=" * 50)
pifagor_gipotenuza(3, 4)

shar_olchamlari(5)

arifmetik_progressiya(a1=2, d=3, n=10)

mexanik_energiya(mass_kg=2, tezlik_ms=10, balandlik_m=5)

gaz_bosimi_hisobla(hajm_m3=0.1, mol=2, harorat_selisiy=25)
print("=" * 50)
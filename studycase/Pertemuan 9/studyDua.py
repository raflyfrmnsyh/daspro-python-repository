# Menghitung volume tabung
# Rumus phi*r2*t

r = float(input('Masukan nilai jari-jari : '))
t = float(input('Masukan nilai tinggi : '))
def volumeTabung(r, t):
    phi = 3.14
    kuadrat = r**2
    rumus = phi * kuadrat * t
    print(f"Volume Balok adalah : {rumus}")

volumeTabung(r,t)
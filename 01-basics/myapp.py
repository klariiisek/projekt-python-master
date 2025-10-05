"""
Jednoduchý kvíz o zvířatech
Aplikace pro začátečníky demonstrující vstup a výstup v Pythonu
"""

# Uvítání
print("Ahoj! Vítej v kvízu o zvířatech!")
print("===============================")

# Získání jména uživatele
jmeno = input("Jak se jmenuješ? ")
print("Ahoj " + jmeno + "! Jsem rád, že jsi tady.")

# Získání věku
vek = input("Kolik ti je let? ")
print("Skvělé! {} let je perfektní věk na kvíz.".format(vek))

# Začátek kvízu
print("\nZačínáme kvíz! Budou tě čekat 3 otázky.")
print("Na každou odpověz pomocí čísla 1, 2 nebo 3.")

spravne_odpovedi = 0

# Otázka 1
print("\n1. Které zvíře říká 'mňau'?")
print("   1) Pes")
print("   2) Kočka") 
print("   3) Kráva")

odpoved1 = input("Tvoje odpověď (1-3): ")

if odpoved1 == "2":
    print("✓ Správně! Kočka říká 'mňau'.")
    spravne_odpovedi = spravne_odpovedi + 1
else:
    print("✗ Špatně. Správná odpověď je 2 - Kočka.")

# Otázka 2
print("\n2. Kde žije tučňák?")
print("   1) V poušti")
print("   2) V džungli")
print("   3) Na Antarktidě")

odpoved2 = input("Tvoje odpověď (1-3): ")

if odpoved2 == "3":
    print("✓ Správně! Tučňáci žijí na Antarktidě.")
    spravne_odpovedi = spravne_odpovedi + 1
else:
    print("✗ Špatně. Správná odpověď je 3 - Na Antarktidě.")

# Otázka 3
print("\n3. Kolik nohou má pavouk?")
print("   1) 6 nohou")
print("   2) 8 nohou")
print("   3) 10 nohou")

odpoved3 = input("Tvoje odpověď (1-3): ")

if odpoved3 == "2":
    print("✓ Správně! Pavouk má 8 nohou.")
    spravne_odpovedi = spravne_odpovedi + 1
else:
    print("✗ Špatně. Správná odpověď je 2 - 8 nohou.")

# Výsledky
print("\n" + "=" * 30)
print("VÝSLEDKY KVÍZU")
print("=" * 30)

print("Jméno: " + jmeno)
print("Věk: " + vek + " let")
print("Správné odpovědi: {} ze 3".format(spravne_odpovedi))

# Hodnocení podle výsledků
if spravne_odpovedi == 3:
    print("🏆 Výborně! Jsi expert na zvířata!")
elif spravne_odpovedi == 2:
    print("👍 Dobře! Skoro to bylo perfektní.")
elif spravne_odpovedi == 1:
    print("💪 Ujde to! Příště to bude lepší.")
else:
    print("😊 Nevadí! Zkus to znovu a určitě to půjde lépe.")

# Bonus otázka s vlastním vstupem
print("\nBonus otázka:")
oblibene_zvire = input("Jaké je tvoje oblíbené zvíře? ")
print("Wow! {} je skvělé zvíře. Děkuji za kvíz!".format(oblibene_zvire))

print("\nAhoj " + jmeno + "! Bylo mi potěšením s tebou hrát kvíz! 👋")
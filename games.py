import random

def main():
    print("=== GAME BATU GUNTING KERTAS ===")
    pilihan_game = ["batu", "gunting", "kertas"]
    skor_pemain = 0
    skor_komputer = 0

    while True:
        pemain = input("\nMasukkan Batu/Gunting/Kertas (atau 'keluar'): ").lower()

        if pemain == "keluar":
            break
        
        if pemain not in pilihan_game:
            print("Pilihan tidak valid!")
            continue

        komputer = random.choice(pilihan_game)
        print(f"Komputer memilih: {komputer}")

        if pemain == komputer:
            print("Hasil: SERI!")
        elif (pemain == "batu" and komputer == "gunting") or \
             (pemain == "gunting" and komputer == "kertas") or \
             (pemain == "kertas" and komputer == "batu"):
            print("Hasil: KAMU MENANG!")
            skor_pemain += 1
        else:
            print("Hasil: KOMPUTER MENANG!")
            skor_komputer += 1

        print(f"Skor Saat Ini -> Kamu: {skor_pemain} | Komputer: {skor_komputer}")

    print("\nGame Berakhir. Terima kasih sudah bermain!")

main()
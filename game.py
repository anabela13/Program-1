# Game tebak angka
# Angka rahasia: 987

secret = 987
attempts = 0

print("Selamat datang di game tebak angka!")
print("Angka rahasia antara 1 dan 1000.")

while True:
    try:
        guess = int(input("Masukkan tebakan Anda: "))
        attempts += 1
        if guess == secret:
            print(f"Selamat! Anda menebak benar dalam {attempts} percobaan.")
            break
        elif guess < secret:
            print("Terlalu kecil. Coba lagi!")
        else:
            print("Terlalu besar. Coba lagi!")
    except ValueError:
        print("Masukkan angka yang valid.")


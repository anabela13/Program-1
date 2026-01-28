# Aplikasi To-Do List 

todo_list = []

def tampilkan_menu():
    print("\n=== APLIKASI TO-DO LIST ===")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Keluar")

def tampilkan_tugas():
    if not todo_list:
        print("Belum ada tugas.")
    else:
        for i, tugas in enumerate(todo_list, start=1):
            status = "✔" if tugas["selesai"] else "✘"
            print(f"{i}. [{status}] {tugas['nama']}")

def tambah_tugas():
    nama = input("Masukkan nama tugas: ")
    todo_list.append({
        "nama": nama,
        "selesai": False
    })
    print("Tugas berhasil ditambahkan.")

def tandai_selesai():
    tampilkan_tugas()
    try:
        nomor = int(input("Pilih nomor tugas yang selesai: "))
        todo_list[nomor - 1]["selesai"] = True
        print("Tugas ditandai sebagai selesai.")
    except (ValueError, IndexError):
        print("Input tidak valid.")

def hapus_tugas():
    tampilkan_tugas()
    try:
        nomor = int(input("Pilih nomor tugas yang akan dihapus: "))
        tugas = todo_list.pop(nomor - 1)
        print(f"Tugas '{tugas['nama']}' berhasil dihapus.")
    except (ValueError, IndexError):
        print("Input tidak valid.")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_tugas()
    elif pilihan == "2":
        tambah_tugas()
    elif pilihan == "3":
        tandai_selesai()
    elif pilihan == "4":
        hapus_tugas()
    elif pilihan == "5":
        print("Terima kasih! 👋")
        break
    else:
        print("Pilihan tidak tersedia.")

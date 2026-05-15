class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Riwayat penuh!")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Catatan [{x}] berhasil ditambahkan.")

    def pop(self):
        if self.is_empty():
            print("Riwayat kosong, tidak ada yang bisa dibatalkan.")
            return
        print(f"Catatan [{self.st[self.top_idx]}] berhasil dibatalkan (Undo).")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Riwayat kosong.")
            return
        print(f"Riwayat terakhir yang masuk: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Riwayat kosong.")
            return
        print("Riwayat Input Stok SiToserba (Terbaru ke Lama):")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.st[i]}")
        print()

def main():
    riwayat_stok = StackArray()
    pilih = 0
    
    while pilih != 5:
        print("\n=== MANAJEMEN RIWAYAT STOK ===")
        print("1. Catat Stok Masuk")
        print("2. Batal Catat (Undo)")
        print("3. Cek Riwayat Terakhir")
        print("4. Tampilkan Semua Riwayat")
        print("5. Keluar")
        
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue
            
        if pilih == 1:
            val = input("Data stok (contoh: Tambah 12 Teh Pucuk): ")
            riwayat_stok.push(val)
        elif pilih == 2:
            riwayat_stok.pop()
        elif pilih == 3:
            riwayat_stok.peek()
        elif pilih == 4:
            riwayat_stok.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

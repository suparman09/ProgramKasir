import pandas as pd
import datetime as waktu
waktu_sekarang = 0
waktu_sekarang = waktu.datetime.now()


def garis():
    print("======================================")


garis()
print("       NASI PADANG KEDAI TECH       ")
print("      Pesan Antar 085797522591       ")

garis()

print("            DAFTAR MENU              ")
garis()
print("A.   PAKET NASI KIKIL            Rp. 25.0000 ")
print("B.   PAKET NASI RENDANG          Rp. 23.0000 ")
print("C.   PAKET NASI IKAN BAWAL       Rp. 28.0000 ")
print("D.   PAKET NASI IKAN KEMBUNG     Rp. 24.0000 ")
print("E.   PAKET NASI AYAM BAKAR       Rp. 23.0000 ")
print("F.   ES TEH MANIS                Rp. 10.0000 ")
print("G.   JUS JERUK                   Rp. 15.0000 ")

garis()

jumlah_menu_pesanan = int(input("Jumlah Menu Pesanan : "))
kode = []
banyak_item = []
menu = []
harga = []
pajak = []
jumlah = []
kasir = []
list_total = []
kasir = str(input("Nama Kasir   : "))
i = 0

print("          PESANAN ORDER              ")
print("")
while i < jumlah_menu_pesanan:
    print("Menu ke -", i+1)
    kode.append(input("Kode Menu      : "))
    banyak_item.append(int(input("Banyak item    : ")))

    if kode[i] == 'A' or kode[i] == 'a':
        menu.append('PAKET NASI KIKIL')
        harga.append(int(25000))
        jumlah.append(int(banyak_item[i]) * int(25000))
    elif kode[i] == 'B' or kode[i] == 'b':
        menu.append('PAKET NASI RENDANG')
        harga.append(int(23000))
        jumlah.append(int(banyak_item[i]) * int(23000))
    elif kode[i] == 'C' or kode[i] == 'c':
        menu.append('PAKET NASI IKAN BAWAL')
        harga.append(int(28000))
        jumlah.append(banyak_item[i] * int(28000))
    elif kode[i] == 'D' or kode[i] == 'd':
        menu.append('PAKET NASI IKAN KEMBUNG')
        harga.append(int(24000))
        jumlah.append(banyak_item[i] * int(24000))
    elif kode[i] == 'E' or kode[i] == 'e':
        menu.append('PAKET NASI AYAM BAKAR')
        harga.append(int(23000))
        jumlah.append(banyak_item[i]*int(23000))
    elif kode[i] == 'F' or kode[i] == 'f':
        menu.append('ES TEH MANIS')
        harga.append(int(10000))
        jumlah.append(banyak_item[i] * int(10000))
    elif kode[i] == 'G' or kode[i] == 'g':
        menu.append('JUS JERUK2')
        harga.append(int(15000))
        jumlah.append(banyak_item[i] * int(15000))
    else:
        print("perintah tidak valid")
    i = i + 1

print("")


def garis2():
    print("=====================================================================")


garis2()
print("                    NASI PADANG KEDAI TECH ")
garis2()
data = {
    "MENU":  menu,
    "Harga Satuan": harga,
    "Jumlah Beli": banyak_item,
    "Harga": jumlah
}
data_trx = pd.DataFrame(data)
print(data_trx)
garis2()

total_harga = 0
a = 0
while a < jumlah_menu_pesanan:
    total_harga = total_harga + jumlah[a]
    a = a+1
print("                                          Total Harga : Rp. ", total_harga)
if total_harga > 200000:
    diskon = int(total_harga * 3/100)
    print("                                          Diskon       : Rp. ", diskon)
else:
    diskon = 0
    print("                                          Diskon       : Rp. ", diskon)
total_bayar = int(total_harga - diskon)
print("                                          Total Bayar  : Rp. ", total_bayar)
garis2()
uang_bayar = int(input("Masukkan Uang Bayar : "))
uang_kembali = 0

if uang_bayar > total_bayar:
    uang_kembali = uang_bayar - total_bayar
    print("Uang Kembali        :", uang_kembali)
else:
    uang_bayar == total_bayar
    print("Uang kembali        :", uang_kembali)
print("Tanggal")
print(waktu_sekarang)
print("Nama Kasir :", kasir)
garis2()

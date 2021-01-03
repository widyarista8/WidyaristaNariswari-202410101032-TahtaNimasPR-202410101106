# WidyaristaNariswari-202410101032-TahtaNimasPR-202410101106
UAS Algoritma dan Pemrograman I

import json 
from datetime import datetime as waktu 
fileKasir = "kasir.json" 
fileStok = "stok.json"
fileTransaksi = "transaksi.json"

def tampilanMenu():
    print("\n=== SELAMAT DATANG ===")
    print("1. SIGN IN")
    print("2. LOGIN")
    print("3. EXIT")
    pilihan = str(input("\nPilih Nomor Menu : "))
    if pilihan == "1":
        getSignin()
        tampilanMenu()
    elif pilihan == "2":
        getLogin()
    elif pilihan == "3":
        print("Terimakasih")
        exit()
        return ''
    else:
        print("- Pilihan Tidak Tersedia -")
        tampilanMenu()

def getLogin():
        data = bacaData(fileKasir)
        uname = input("Masukkan Username : ")
        pw = input("Masukkan Password : ")

        for masuk in data:
            if masuk["username"] == uname and masuk["password"] == pw :
                print("Login berhasil . . . \n")
                menuUtama()

        else:
            print("Login gagal, harap coba lagi . . . ")
            tampilanMenu()

def getSignin():
    data = bacaData(fileKasir)
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    kosong = {}
    kosong["username"] = username
    kosong["password"] = password

    new_list = list()
    if len(data) != 0:
        for x in data:
            new_list.append(x)
    new_list.append(kosong)
    tulisData(fileKasir, new_list)
    print("Sign In Berhasil . . . ")
    print("Silahkan Login Untuk Melanjutkan . . . ")

def menuUtama():
    print("\n=== MENU UTAMA ===")
    print("1. Stok")
    print("2. Transaksi")
    print("3. LOG OUT")
    pilih = str(input("Pilih Menu yang Diinginkan : "))

    if pilih == "1":
        menuStok()
    elif pilih == "2":
        menuTransaksi()
    elif pilih == "3":
        tampilanMenu()
    else:
        print("- Pilihan Tidak Tersedia -")
        menuUtama()
    
def menuStok():
    print("\n=== MENU STOK ===")
    print("1. Lihat Daftar Stok")
    print("2. Tambah Stok")
    print("3. Hapus Stok")
    print("4. Kembali ke Menu Utama")
    pilihStok = str(input("Pilih Menu Stok yang Dipilih : "))

    if pilihStok == "1":
        lihatStok()
        backmenustok()
    elif pilihStok == "2":
        lihatStok()
        print("\n")
        tambahStok()
        lihatStok()
        backmenustok()
    elif pilihStok == "3":
        lihatStok()
        hapusStok()
        lihatStok()
        backmenustok()
    elif pilihStok == "4":
        menuUtama()
    else:
        print("- Pilihan Tidak Tersedia -")
    backmenustok()

def menuTransaksi():
    print("=== MENU TRANSAKSI ===")
    print("1. Lihat Daftar Transaksi")
    print("2. Tambah Transaksi")
    print("3. Hapus Transaksi")
    print("4. Pembayaran")
    print("5. Kembali ke Menu Utama")
    pilihTransaksi = str(input("Pilih Menu Transaksi yang Dipilih : "))

    if pilihTransaksi == "1":
        lihatTransaksi()
        backmenutransaksi()
    elif pilihTransaksi == "2":
        lihatStok()
        print("\n")
        tambahTransaksi()
        lihatTransaksi()
        backmenutransaksi()
    elif pilihTransaksi == "3":
        hapusTransaksi()
        lihatTransaksi()
        backmenutransaksi()
    elif pilihTransaksi == "4":
        lihatTransaksi()
        pembayaran()
        backmenutransaksi()
    elif pilihTransaksi == "5":
        menuUtama()
    else:
        print("- Pilihan Tidak Tersedia -")
        backmenutransaksi()

def bacaData(file):
    try :
        data = []   
        with open(file, 'r') as myfile: 
            baca = json.load(myfile)
        for kosong in baca:
            data.append(kosong)
    except FileNotFoundError:
        data = []
    return data

def tulisData(file,data):
    with open(file, 'w') as myfile:
        json.dump(data, myfile, indent=4)

def randKode(nama,kode):
    jumlah = str(len(nama))
    nama = nama[0:2].upper()
    return nama+jumlah+str(kode)

def backmenustok():
    input("Tekan 'enter' untuk kembali")  
    menuStok()

def lihatStok():
    try:
        with open(fileStok, 'r') as myfile: 
            baca = json.loads(myfile.read())
            print("-"*50)
            print("KODE \t NAMA BARANG \t STOK BARANG \t HARGA BARANG")
            print("-"*50)
            for stok in baca:    
                print(stok["KODE"],"\t",stok["NAMA BARANG"],"\t\t",stok["STOK BARANG"],"\t\t",stok["HARGA BARANG"])
    except:
        print("- Belum Ada Stok yang Ditambahkan -")

def tambahStok():
    data = bacaData(fileStok)
    jumlahData = len(data) #len
    nama = input("Masukkan nama barang : ") 
    kode = randKode(nama, jumlahData+1) #nama
    stok = int(input("Masukkan jumlah stok barang : "))
    harga = int(input("Masukkan harga barang : "))

    barang = dict()
    barang["KODE"] = kode
    barang["NAMA BARANG"] = nama
    barang["STOK BARANG"] = stok
    barang["HARGA BARANG"] = harga

    new_list = list()
    if len(data) != 0:
        for x in data:
            new_list.append(x)
    new_list.append(barang)
    tulisData(fileStok,new_list)
    print("- Stok Berhasil Ditambahkan -")

def hapusStok():
    hapus = bacaData(fileStok)

    if len(hapus) == 0: 
            print("Kembali ke menu sebelumnya") 
            backmenustok() 
    else: 
        print('='*50)
    stokhapus = input("Masukkan kode barang yang ingin dihapus : ") 
    for stok in hapus:
        if stok["KODE"] == stokhapus :
            hapus.remove(stok)
    tulisData(fileStok, hapus)
    print("- Stok Berhasil Dihapus -")


def backmenutransaksi():
    input("Tekan 'enter' untuk kembali")
    menuTransaksi()

def lihatTransaksi(): 
    try:
        with open(fileTransaksi) as myfile: 
            baca = json.loads(myfile.read()) 
            print("="*100) 
            print("TANGGAL \t KODE BARANG \t NAMA BARANG \t HARGA BARANG \t JUMLAH BARANG \t TOTAL HARGA") 
            print("="*100) 
            for look in baca: 
                print(look["TANGGAL"],"\t",look["KODE"],"\t\t",look["NAMA BARANG"],"\t\t",look["HARGA BARANG"],"\t\t",look["JUMLAH BARANG"],"\t\t",look["TOTAL HARGA"])
    except:
        print("- Belum Ada Riwayat Transaksi -")

def tambahTransaksi():
    try:
        tanggal = waktu.now().strftime('%d-%m-%Y')   

        kodesalah = []
        with open(fileStok,'r') as json_file:
            salah = json.load(json_file)
            for row in salah:
                kodesalah.append(row)
            kode = str(input("Masukkan kode barang : "))

            kodesalahbaru = []
            indeks = 0
            for x in kodesalah:
                if x['KODE'] == kode:
                    kodesalahbaru = kodesalah[indeks]
                indeks = indeks + 1 
            if len(kodesalahbaru) > 0:
                if kodesalahbaru['KODE'] == kode:
                    print("Kode Barang Benar")
            else:
                print("Kode Barang Salah")
                backmenutransaksi()
        
        daftar = []
        with open(fileStok,'r') as jsonfile:
            lihat = json.load(jsonfile)
            for stok in lihat:
                daftar.append(stok)

        jumlah_beli = int(input("Masukkan jumlah barang : "))
        stok = []
        indeks = 0
        for x in daftar:
            if x['KODE'] == kode:
                stok = daftar[indeks]
            indeks = indeks + 1
        
        if stok['STOK BARANG'] >= jumlah_beli:
            total_stok = stok['STOK BARANG'] - jumlah_beli
        else:
            print("- Stok Barang Tidak Cukup -")
            backmenutransaksi()

        total = jumlah_beli*stok['HARGA BARANG']
        print("TOTAL HARGA : "+str(total))

        stoknow = dict()
        stoknow['KODE'] = kode
        stoknow['NAMA BARANG'] = stok['NAMA BARANG']
        stoknow['STOK BARANG'] = total_stok
        stoknow['HARGA BARANG'] = stok['HARGA BARANG']

        daftarbaru = []
        with open(fileStok,'r') as jsonfile:
            lihat1 = json.load(jsonfile)
            for stok in lihat1:
                if stok['KODE'] == kode:
                    continue
                else:
                    daftarbaru.append(stok)

        indeks = 0
        for x in daftarbaru:
            if x['KODE'] == kode:
                daftarbaru[indeks]['KODE'] = kode
                daftarbaru[indeks]['NAMA BARANG'] = stok['NAMA BARANG']
                daftarbaru[indeks]['STOK BARANG'] = total_stok
                daftarbaru[indeks]['HARGA BARANG'] = stok['HARGA BARANG']
            indeks = indeks - 1
        daftarbaru.append(stoknow)
        tulisData(fileStok,daftarbaru)
        
        barang = dict()
        barang['TANGGAL'] = tanggal
        barang['KODE'] = kode
        barang['NAMA BARANG'] = kodesalahbaru['NAMA BARANG']
        barang['JUMLAH BARANG'] = jumlah_beli
        barang['HARGA BARANG'] = kodesalahbaru['HARGA BARANG'] 
        barang['TOTAL HARGA'] = total           

        new_list = list() 
        lihat = bacaData(fileTransaksi)
        if len(lihat) != 0:
            for x in lihat:
                new_list.append(x)
        new_list.append(barang)
        tulisData(fileTransaksi,new_list)
        print("- Transaksi Berhasil Ditambahkan -") 
    except FileNotFoundError:
        print("- Belum Ada Stok yang Ditambahkan -")
        backmenutransaksi()

def hapusTransaksi(): 
    try:
        with open(fileTransaksi) as myfile: 
            hilang = json.loads(myfile.read()) 
            print("="*100) 
            print("TANGGAL \t KODE BARANG \t NAMA BARANG \t HARGA BARANG \t JUMLAH BARANG \t TOTAL HARGA") 
            print("="*100) 
            for cut in hilang: 
                print(cut["TANGGAL"],"\t",cut["KODE"],"\t\t",cut["NAMA BARANG"],"\t\t",cut["HARGA BARANG"],"\t\t",cut["JUMLAH BARANG"],"\t\t",cut["TOTAL HARGA"]) 

        daftarBaru = [] 
        tulis = bacaData(fileTransaksi) 
        if len(bacaData(fileTransaksi)) != 0: 
            no = input("Masukkan Kode Barang yang Ingin Dihapus : ") 
            for data in tulis: 
                if data["KODE"] == no:
                    continue
                else:
                    daftarBaru.append(data)
    
            with open(fileTransaksi, "w") as myfile: 
                json.dump(daftarBaru, myfile, indent=2) 
            print("- Transaksi Berhasil Dihapus -")
    except FileNotFoundError:
        print("- Transaksi Gagal Dihapus-") 

def pembayaran():
    try:
        jumlah_bayar = 0
        x = bacaData(fileTransaksi)

        if len(x) == 0:
            print("Kembali ke Menu Sebelumnya")
            backmenutransaksi()
        else:
            print('='*50)

        for i in x:
            jumlah_bayar+=i["TOTAL HARGA"]
        print("Total Semua Harga =", "Rp.", jumlah_bayar)
        nominal = int(input("Jumlah Nominal Uang = " ))
        print("Uang Dibayar: ", "Rp.", nominal)
        if jumlah_bayar > nominal:
            print("Uang Anda Tidak Mencukupi")
            backmenutransaksi()
        kembalian = (nominal-jumlah_bayar)
        print("Uang Kembalian: ", "Rp.", kembalian)
    except:
        print("Belum Ada Transaksi")

tampilanMenu()

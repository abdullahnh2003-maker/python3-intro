print("materi 6 - pyton")
print("------------------------------")
apaAja = [
    "sapi",
      "kambing"
      ]

# [no index] membuat list
print("hewan:", apaAja)
print("item ke-1:", apaAja[0])
print("item ke-2:", apaAja[1])

# append()menambah itembaru keakhir list
apaAja.append("kaki ayam")
apaAja.append("unta")
print("isi kandang sekarang", apaAja)
print("item ke-3", apaAja[2])
print("item ke-4",apaAja[3])
#remove menghapus item
apaAja.remove("kaki ayam")
print("isi kandang akhir", apaAja)

print("semoga gk ilang pemahamannya")
print("amiin")


print("----tuple----")
#berurutan,tdk bisa diubah,boleh duplikat
#penulisannya menggunakan ()
tglLahir = (5,"maret",2010)
print("tgl lahir saya", tglLahir)
#no index = akses data tupel
print("tanggal", tglLahir[0])
print("bulan", tglLahir[1])
print("tahun", tglLahir[2])

doa = ("semoga nyantolterus","amiin")
print("doa", doa[0])
print("doa", doa[1])

#akses bulan (posisi index) : lalu batas akhir itemnya
#tambahin 1 nomer dibelankangnya
print("tanggal bulan tahun", tglLahir[0:3])

#unpacking tuple ke variabel baru
#mengikuti urutan itemnya
tgl, bulan, tahun = tglLahir
print(tgl)
print(bulan)
print(tahun)

#manipulasi list lanjtan(menggabungkan)
makanan_masboy=["jambu","nasi"]
makanan_buaya=["cewe","perempuan"]
makananMasboyDanBuaya= makanan_masboy + makanan_buaya
print(makananMasboyDanBuaya)

#list multi dimensi
listBuah= [
    ["jambu","melon","apeltg"],
    ["mangga","alpukat","pisang"],
    ["delima","jeruk"]
]
print(listBuah)
#tiap baris punya 3 index (1,2,3)

print(listBuah[2][1])
#https://bit.ly/hsiprojo-


print(len(apaAja))
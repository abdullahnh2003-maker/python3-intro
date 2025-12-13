# buku yg belum dikembalikan
print("Tugas json lokal")
print("-"*17)

import json
jumlah =0
masihDipinjam=0
print("List buku yg belum dikembalikan:")

with open(r"C:\Users\dell 7490\Desktop\Tugas-json\Tugas.json") as filePath:

    item=json.load(filePath)

for peminjam in item["anggota"]:
    for Book in peminjam["pinjam"]:
        jumlah +=1
        if Book["kembali"] == False:
            masihDipinjam += 1
            print(f"- {peminjam["nama"]} : {Book["judul"]} ({Book["tanggal"]})")

print(f"Total dipinjam: {jumlah} | Belum kembali: {masihDipinjam}")

print("-"*40)

# ayat kursi(arab)
print("tugas json-API")
print("-"*15)

import requests
url= r"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
response= requests.get(url)
data_json= response.json()

ayat_kursi =data_json["data"]
print(f"Ayat Al-Kursi (2:255) - Arab:{ayat_kursi["text"]}")

print("-"*20)

# terjemahan(B.inggris)

import requests
url= r"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
response = requests.get(url)
data_json = response.json()

terjemahan = data_json["data"]
print(f"Terjemah (EN):{terjemahan["text"]}")
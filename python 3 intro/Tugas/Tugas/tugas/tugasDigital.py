print("=== Profil Digital Saya ===")
a = input("Masukkan nama: ")
b = input("Umur: ")
c = input("Kelas: ")
d = input("Cita-cita: ")
e = input("Hobi: ")
print("Pasti jago!")
f = input("Lebih suka belajar pagi atau malam? ")

print("=== Tipe Digital ===")

pilihan = ["1. Wibu", "2. Gamer", "3. K-Popers", "4. Anak Konten", "5. Anak Nongki"]

for i in pilihan:
    print(i)

tipe = input("Kamu anak apa?: ")


if tipe == "wibu":
    print("Pasti suka nonton anime sambil ngoding.")
    input("Game apa yang kamu sukai? ")
elif tipe == "gamer":
    print("Pasti jago main game.")
    input("Game apa yang kamu sukai? ")
elif tipe == "k-popers":
    print("Ih pasti suka nonton dan dengerin lagu Korea.")
    input("Siapa bias kamu? ")
elif tipe == "anak konten":
    print("Pasti banyak like-nya!")
    input("Platform favorit kamu? TikTok? YouTube? ")
elif tipe == "anak nongki":
    print("Pasti karena gabut ya ")
    input("Nongkrong paling sering di mana? ")

# Pertanyaan tambahan
n = input("Teman di sebelahmu bau nggak? (ya/tidak): ")
if n == "ya":
    print("Suruh mandi ")
else:
    print("Alhamdulillah ")

for item in tipe,n:
    print(item)
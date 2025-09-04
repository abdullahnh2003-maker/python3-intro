print("materi 7 - python data structure")
print("---------------------------------")
makan_masboy ={"pisang","ayam","nasi"}
makan_rusa ={"jambu","daun"}
makan_masboy.add("jambu")
makan_rusa.add("rumput")
makan_masboy.remove("ayam")

print("makan masboy", makan_masboy)
print("makan rusa", makan_rusa)
makan_gabungan=makan_masboy|makan_rusa # | (or) atau
print("daftar makanan", makan_gabungan)


for makan in makan_gabungan:
    print('makanan bergizi:', makan)
    print("---> taruh", makan, "di wadah makan hewan")

# dictionari (dict) -> {key:velue} / {kunci:isi}
#->berurutan,berubah,tdk duplikat
kamus_anime={
    "one_piece":'monkey d luffy',
    'blue_lock':'isagi ren',
    'demon_slayer':'tanjiro',
    'waifu':{
        'one_piece':'big mom',
        'demon_slayer':'nezuko',
    }
}
print("kamus anime:", kamus_anime)
print("mc demon slayer:",kamus_anime["demon_slayer"])
print("waifu one piece:", kamus_anime["waifu"]["one_piece"])

#nambah item baru ke dictionari
kamus_anime["naruto"] = "shikamaru"
#mengubah item dari dictionari
kamus_anime["demon_slayer"]= "zenitsu"
#menghapus item dr dictionari
del(kamus_anime["blue_lock"])
print("anime baru", kamus_anime)
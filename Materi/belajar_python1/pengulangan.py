masboy = ["babon",2,True]

#operasi dasar sebuah list
#1. mengakses elemen [index]

print(masboy[0])

# 2.mengubah elemen
masboy[1]= "jelek"

print(masboy)

#menmbah elemen
masboy.append("kece")

#diawal
masboy.insert(0, 'dikandang')
print(masboy)

masboy.insert(1, "ada")
print(masboy)
#menghapus elemen
masboy.remove("kece")
print(masboy)
#menhapus berdasarkan index
masboy.pop(4)
print(masboy)

#5. panjang list
print(len(masboy))
#6. mencetak  isi list menggunakan looping
#seluruuntuk setiap item yg ada di(arti)
for item in masboy:
    print(item)
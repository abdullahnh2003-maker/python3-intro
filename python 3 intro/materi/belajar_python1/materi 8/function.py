print("-----materi 9 function------")
#function tdk akan di eksekusi jika tdk dipanggil
def say_hello(name):
    #kasih f diawal string untk menyisipkan variabel atau parameter
    #dngn diapit {nama_variabel}
    print(f'gimana kabarnya {name}?')
    print('alhamdulillah baik')
#lambda untk menulis fungsi yg ringkas dgn 1 baris saja
#sering disebut juga fungsi anonim(tanpa nama)
say_hello_mini= lambda name: print(f'hallo {name}')
#panggil fungsi2nya di bawah ini
say_hello('faiz')
say_hello('zidane')
print('---------->')
say_hello_mini('masboy')
say_hello_mini('ayam merak')

#contoh penerapan lambda dgn higher-order function
# map()--sorted() -- fiter()

uang_korup=[10000,50000,20000,40000,30000]
#sorted() -> mengurtkan data
urutkan= sorted(uang_korup)
balikkan= sorted(uang_korup, reverse=True)
print(f'urtkan uang korupsi:{urutkan}')
print(f'balikkan urutan:{balikkan}')
#map() -> mentrasformasi data
kurangin= map(lambda uang: uang - 2500, uang_korup)
# list() mengubah data objek map menjadi bentuk list
list_kurangin= list(kurangin)
print(f"map uang berkurang: {list_kurangin}")

#filter() -> menyaring/mengfilter data
filter_korup= filter(lambda uang: uang > 20000, uang_korup)
list_korup= list(filter_korup)
print(f'filter jajan diatas 30rb: {list_korup}')


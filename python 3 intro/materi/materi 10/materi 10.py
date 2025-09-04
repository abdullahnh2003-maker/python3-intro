print('materi 19')
print('--------------------')
file_path = r'C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\materi 10\pesan.txt'
file_pesan = open(file_path,'r')
#baca isi file
isi = file_pesan.read()
#tampilkan output isi pesan
print(f'isi pesan -> {isi}')
#tutup file
file_pesan.close()

import csv

print('materi 19')
print('--------------------')
file_path = r'C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\materi 10\jajan.csv'
file_pesan = open(file_path,'r')
#baca isi file
isi = file_pesan.read()
#tampilkan output isi pesan
print(f'isi pesan -> {isi}')
#tutup file
file_pesan.close()


print("-------append csv file-------")
#list_baru =[5,'abdul',200000,50000]
#print(f'list baru{list_baru}')
#open 'a' -> append
# newline -> tambah baris baru 
# with ... as -> buka file dgn tutup otomatis
#with open(file_path, "a",newline="") as file_baru:
    #aktifkan mode writer cvs dari file target
#    writer= csv.writer(file_baru)
 #   writer.writerow(list_baru)
#writerow menambah baris baru

import csv
file_pathy=r"C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\materi 10\jajan.csv"
with open(file_pathy, "r") as file_barus:
#    next(file_barus)
    read = csv.reader(file_barus)
    list_read =list(read)
    print("baris")
    print("😍" * 20)
    for baris in list_read:
        #print(f"{baris[1]}"
        tgl = baris[0]
        nama = baris[1]
        uang= baris[2]
        korup= baris[3]
        print(f"{tgl}| {nama} | {uang} | {korup}")


list_baru =[5,'abdul',200000,50000]
print(f'list baru{list_baru}')
#open 'a' -> append
# newline -> tambah baris baru 
# with ... as -> buka file dgn tutup otomatis
with open(file_path, "a",newline="") as file_baru:
    #aktifkan mode writer cvs dari file target
    writer= csv.writer(file_baru)
    writer.writerow(list_baru)
import csv
# tambahkan module 'cvs' dgn 'import'
print('----materi 11 - handling part 2----')
print('---update csv---')
#baca semua file -> ekstrak data -> buat data baru
# -> tlis ulang semua isi 
file_path_csv= r"C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\materi 10\jajan.csv"
#siapkan data kosong
# untk menampung data dr csv ke list
data_jajan=[]
# cvs.reader() -> mem baca isi file cvs
with open(file_path_csv, "r") as file_jajan:
    isi_table_jajan= csv.reader(file_jajan)
    # ekstrak semua data dgn for loop
    for item_jajan in isi_table_jajan:
        print(item_jajan)
        #tambah item ke list data jajan
        data_jajan.append(item_jajan)

# mengubah /membuat data baru
for baris in data_jajan:
    # jika kolom nama adlh 'x nama
    if baris[1] == 'abdul':
        #ganti kolom uang (index 2) dngn nilai baru
        baris[2] = 10000

print(f"data jajan terkini{data_jajan}")

# satu nya

print('satunya')
for baris in data_jajan:
    print(f'proses baris/iteb no => {baris[0]}')
    print(baris)
    #jika kolom nama (index 1) adlh 'nama
    if baris[1] == 'abdul':
        #ganti kolom uang (index 2) dngn nilai baru
        uang_jajan_baru= 15000
        baris[2] = uang_jajan_baru
        print(f'data ditemukan, ganti uang jajan{uang_jajan_baru}')
        print('--loop end--')
#hapus data list 
del data_jajan[2]
print(f'DATA JAJAN TERKINI: {data_jajan}')


# 4.tulis ulang dngn mode 'w'
with open(file_path_csv, "w", newline="") as file_jajan:
    writer =csv.writer(file_jajan)
    #.writerous()-> tulis sekali banyak
    writer.writerows(data_jajan)
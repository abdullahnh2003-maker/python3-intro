import csv
file_pathy=r"C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\tugas baru\tugas_csv\tugas.csv"
with open(file_pathy, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read =list(read)
    print("SEMUA KEUANGAN")
    print("|tanggal | keterangan | kategori | jumlah|")
    print("-" * 40)
    for baris in list_read:
        
        
        tgl = baris[0]
        keterangan = baris[1]
        kategori= baris[2]
        jumlah = baris[3]
        print(f"|{tgl}| {keterangan} | {kategori} | {jumlah}|")

#list_baru =[5,"ranjang","tidur",40000]
#print(f'{list_baru}')
#with open(file_pathy, "a",newline="") as file_baru:
#    writer= csv.writer(file_baru)
#    writer.writerow(list_baru)

#tambah data
with open(file_pathy, "a", newline="") as file_lama:
    write= csv.writer(file_lama)
    write.writerow(["2025-08-22","ranjang","tidur","40000"]) 
    
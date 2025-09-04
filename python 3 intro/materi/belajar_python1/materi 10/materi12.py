import json
#tambahkan module 'json' dngn 'import
print('-----materi12-----')
print('---READ JSON----')
file_path_json= r"C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\materi 10\{} materi.json"
with open(file_path_json, "r") as file_materi:
    #json.load() -> mmbaca isi file json
    data_materi= json.load(file_materi)
    print(f"judul berkas: {data_materi["title"]}")
    print(f"total santri HSI: {data_materi["total"]}")
    print(f"ini santri HSI: {data_materi["status_santri"]}")
    print(f"santri in lulus/tidak: {data_materi["status_lulus"]}")
    print(f"pelajaran yg dipelajari: {data_materi["pelajaran"]}")
    for pelajaran in data_materi["pelajaran"]:
        print(f'->>> {pelajaran}')
    

    file_path_json= r"C:\Users\dell 7490\Desktop\python\materi\New folder\materi10\materi 10\{} materi2.json"
with open(file_path_json, "r") as file_materi:
    #json.load() -> mmbaca isi file json
    data_surah= json.load(file_materi)
    print(f"surah: {data_materi["surah"]}")
    for pelajaran in data_surah["pelajaran"]:
        print(f'->>> {pelajaran}')
    print("-"*50) #gandakan simbol dgn perkalian
    print("| NO | Nama SUrah | Ayat | Tempat Turun |")
    print("-"*50)
    for surah in data_surah:
        print(f'{surah}')

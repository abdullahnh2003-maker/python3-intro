# import requests
# # datetime Dipakai untuk mengambil tanggal & waktu sekarang.
# # timedelta Dipakai untuk menambah atau mengurangi hari
# from datetime import datetime, timedelta

# def jadwal_sholat():

#     kota=input ('masukkan nama kota : ')
#     negara = input('masukkan nama negara : ')

#     print('pilih tanggal : ')
#     print('1. hari ini')
#     print('2. besok')
#     pilihan=input('pilih (1/2) : ')

#     if pilihan == "2":
#         besok = datetime.now() + timedelta(days=1)
#         tanggal = besok.strftime("%d-%m-%Y")
#         print(f"Mengambil jadwal untuk besok ({tanggal})")
#     else:
#         tanggal = datetime.now().strftime("%d-%m-%Y")
#         print(f"Mengambil jadwal untuk hari ini ({tanggal})")

#     url = "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
#     jadwal = {
#     "city": kota,
#     "country": negara,
#     "method": 20
#     }

#     response = requests.get(url, params=jadwal)
#     data = response.json()
# #requests.get Ini adalah perintah untuk mengambil data dari internet (HTTP GET).
#     if data['code'] == 200:
#         waktu = data["data"]["timings"]
#         tanggal_hijriah = data["data"]["date"]["hijri"]["date"]
        
#         print("="*50)
#         print(f"📍 {kota}, {negara}")
#         print(f"📅 {tanggal} | Hijriah: {tanggal_hijriah}")
#         print("="*50)
        
#         print(f"🕐 SUBUH    : {waktu['Fajr']}")
#         print(f"🕐 DZUHUR   : {waktu['Dhuhr']}")
#         print(f"🕐 ASHAR    : {waktu['Asr']}")
#         print(f"🕐 MAGHRIB  : {waktu['Maghrib']}")
#         print(f"🕐 ISYA     : {waktu['Isha']}")
#         print("="*50)
            
#     else:
#             print(f"❌ Error: {data.get('data', 'Kota tidak ditemukan')}")

# jadwal_sholat()



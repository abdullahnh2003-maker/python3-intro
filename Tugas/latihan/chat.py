import requests
from datetime import datetime, timedelta

def jadwal_sholat_sederhana():
    print("="*50)
    print("JADWAL SHOLAT SEDERHANA".center(50))
    print("="*50)
    
    # Input dari user
    kota = input("Masukkan nama kota: ").strip()
    negara = input("Masukkan nama negara: ").strip()
    
    # Pilihan tanggal
    print("\nPilih tanggal:")
    print("1. Hari ini")
    print("2. Besok")
    pilihan = input("Pilihan (1/2): ").strip()
    
    # Tentukan tanggal
    if pilihan == "2":
        besok = datetime.now() + timedelta(days=1)
        tanggal = besok.strftime("%d-%m-%Y")
        print(f"Mengambil jadwal untuk besok ({tanggal})")
    else:
        tanggal = datetime.now().strftime("%d-%m-%Y")
        print(f"Mengambil jadwal untuk hari ini ({tanggal})")
    
    # URL API
    url = f"https://api.aladhan.com/v1/timingsByCity/{tanggal}"
    params = {
        "city": kota,
        "country": negara,
        "method": 20  # ISNA method
    }
    
    print(f"\n⏳ Mengambil data dari API...")
    
    try:
        # Request ke API
        response = requests.get(url, params=params)
        data = response.json()
        
        if data["code"] == 200:
            timings = data["data"]["timings"]
            tanggal_hijri = data["data"]["date"]["hijri"]["date"]
            
            print("\n" + "="*50)
            print(f"📍 {kota}, {negara}")
            print(f"📅 {tanggal} | Hijriah: {tanggal_hijri}")
            print("="*50)
            
            print(f"\n🕐 SUBUH    : {timings['Fajr']}")
            print(f"🕐 DZUHUR   : {timings['Dhuhr']}")
            print(f"🕐 ASHAR    : {timings['Asr']}")
            print(f"🕐 MAGHRIB  : {timings['Maghrib']}")
            print(f"🕐 ISYA     : {timings['Isha']}")
            print("="*50)
            
        else:
            print(f"❌ Error: {data.get('data', 'Kota tidak ditemukan')}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    jadwal_sholat_sederhana()
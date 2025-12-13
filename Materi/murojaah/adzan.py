import requests

target_url = "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
print(f"target url: {target_url}")
#pttp get tarik data
response = requests.get(target_url)
#konversi ke json
data_json = response.json()
# print("response data:", data_json)
jadwal = data_json ['data']['timings']
subuh = jadwal ['Fajr']
duhur = jadwal ['Dhuhr']
asr = jadwal ['Asr']
maghrib = jadwal ['Maghrib']
print(f'sholat subuh : {subuh}')
print(f'sholat dzuhur : {duhur}')
print(f'sholat ashar : {asr}')
print(f'sholat maghrib : {maghrib}')
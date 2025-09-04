#tantangan 1 : list
print('piket hari ini:')
piket= ['zidane','faiz','ucok']
for p in piket:
    print('-',p)

#tantangan 2 : tuple(for)
rukun_islam=('syahadat','sholat','zakat','puasa','haji')
for r in range(len(rukun_islam)):
    print(f'{r + 1}.{rukun_islam[r]}')

#tantangan 3 : set(for)
print('kitab2 yg dipelajari')
kitab_pelajaran={'tajwid','fiqh','aqidah'}
for o in kitab_pelajaran:
    print(f'-{o}')

#tantangan 4: dictionari(for)
print('biodata santri:')
biodata = {'nama': 'abdullah', 'kelas': 'X-A', 'hafalan_juz': 5}
for keys, value in biodata.items():
    print(f'- {value}')
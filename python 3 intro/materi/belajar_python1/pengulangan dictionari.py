print("---pengulagan dictionari---")
purba=[5,'maret',2010]
siswa={
    1:'zidane',
    2:'faiz',
    3:'purba:'
}
print(siswa[3])
print(purba[0])
print(purba[1])
print(purba[2])

#cara menamabahkan nilai(velue)
siswa[4]= 'vino'
print(siswa)

# mengubah nilai(velue)
siswa[4]='juna'
print(siswa)

#menghapus nilai(velue)
del(siswa[4])
print(siswa)

#mengecek key
print(1 in siswa)

#cara mendapatkan semua key dan veluenya
#cara mengecek ada key apa aja
print(siswa.keys())
#cara mengecek ada velue apa aja
print(siswa.values())

#looping

for key in siswa:
    print(key)

for velue in siswa.values():
    print(velue)
for key, value in siswa.items():
    print(f'{key} --> {value}')#f = fungsi

#nested dictionari
kelas = {
    'siswa1':{
        'nama':'masboy'
        'umur':70
        'hobi':{
            'hobi1':'makan'
            'hobi2':'marah'
            'hobi':{
                'bola1':"pingpong"
                'bola2':'futsal'
            }
        }
    },
    'siswa2':{
        'nama':'vino'
        'umur':100
    },
    'siswa3':{
        'nama':'faiz'
        'umur':1000
    }
}
print(kelas['siswa1'])
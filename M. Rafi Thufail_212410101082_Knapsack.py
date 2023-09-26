import math

def pengurut(a):
    return a['value']

inputKapasitas = int(input('Ketikkan Besar kapasitas(kg) = '))
hitungBarang = int(input('Inputkan Jumlah Barang : '))

list_barang = []
isi_penampung = []
berat_penampung = 0
harga_penampung = 0 

for i in range(hitungBarang):
    print('\n=====================')
    print("Data dari Barang ke", i + 1)
    print('='*20)
    nama_barang = input("Nama Barang : ")
    berat_barang = float(input('Berat Barang (kg) : '))
    harga_barang = int(input('Harga Barang : '))

    list_barang.append({
        "nama" : nama_barang,
        "berat" : berat_barang,
        "harga" : harga_barang,
        "value" : math.floor(harga_barang/berat_barang)
    })

    list_barang.sort (key=pengurut, reverse=True)

for i in range(len(list_barang)):
    if berat_penampung < inputKapasitas:
        isi_penampung.append(list_barang[i])
        berat_penampung += isi_penampung[i]['berat']
        harga_penampung += isi_penampung[i]['harga']
        if berat_penampung > inputKapasitas:
            isi_penampung.pop(-1)
            berat_penampung -= isi_penampung[-1]['berat']
            harga_penampung -= isi_penampung[-1]['harga']
        else:
            continue

print('Jadi banyaknya barang yang dapat masuk ke dalam penampung adalah ', len(isi_penampung), "barang, seperti :")
print('='*57)
print('| %-3s| %-10s | %-10s | %-10s | %-9s |' %(" ", "Nama", "Berat (kg)", "Harga", "Value"))
print('='*57)
for i in range(len(isi_penampung)):
    print('| %-2s| %-10s | %-10s | %-10s | %-10s |' % (i+1, isi_penampung[i]['nama'],isi_penampung[i]['berat'],isi_penampung[i]['harga'],isi_penampung[i]['value']))
    print('='*57)

print("Total seluruh Berat : ", berat_penampung, 'Kg')
print('Total seluruh Harga :', harga_penampung)


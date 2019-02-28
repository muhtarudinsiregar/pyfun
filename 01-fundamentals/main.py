print("hello")
print("hello \'world")

# tipe data
nama = "Bill gates"
usia = 5
nilai = 76.9
print(nama, usia, nilai)

# looping
# for dibaca "untuk setiap i di dalam range(0, 10)"
# code dibawah akan melakukan looping sebanyak (10-1) = 9
for i in range(1, 10):
    print(i)

# looping with while

while usia > 0:
    print("usia saya adalah %s" % usia)
    usia -= 1

# list

daftar_nama = ['Bill', 'Gates', 'Bill Gates Jr']
print(daftar_nama)

daftar_nama.append("Gates Bill")
print(daftar_nama)

for dn in daftar_nama:
    print(dn)


# dictionary

manusia = {}  # init dict
manusia['nama'] = "Bill gates"
manusia['kebangsaan'] = "US"
print(manusia)

manusia['nama'] = "Melinda bill"
print(manusia)

# add new attribute on dict
manusia['alamat'] = "Jakal km 14"
print(manusia)

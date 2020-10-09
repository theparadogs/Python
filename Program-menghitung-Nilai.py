print("============================================")
print("Nama  : Felix Rizky Lesmana")
print("Kelas : 12.1J.30")
print("NIM   : 12200438")
print("============================================")

print("PROGRAM MENGHITUNG NILAI MATA KULIAH PRAKTEK")
print("--------------------------------------------")
matkul = input("masukan nama mata kuliah : ")
max_pertemuan = int(input("masukan max. pertemuan : "))
absen = int(input("masukan jumlah hadir : "))

nilai_absen = (absen*100)/max_pertemuan
print("nilai absen yang didapat dari perhitungan diatas adalah : ",nilai_absen)
print("--------------------------------------------")
nilai_tugas = int(input("masukan nilai tugas yang diberikan oleh Dosen : "))
nilai_project = int(input("masukan nilai project yang diberikan oleh Dosen : "))
print("--------------------------------------------")
total_absen = nilai_absen*(20/100)
total_tugas = nilai_tugas*(25/100)
total_project = nilai_project*(55/100)
total_nilai = (nilai_absen*(20/100)+nilai_tugas*(25/100)+nilai_project*(55/100))
print("konversi nilai berdasarkan persentase nilai sesuai ketentua")
print("nilai absen (20%) anda adalah : ",total_absen)
print("nilai tugas (25%) anda adalah : ",total_tugas)
print("nilai project (55%) anda adalah : ",total_project)
print("--------------------------------------------")
print("Pada mata kuliah : ",matkul)
print("anda mendapatkan total nilai",total_nilai)
if total_nilai > 100 :
    print('CATATAN : "JANGAN NAK NGELEBIH LEBIHKAN NILAI BOSS"')
elif total_nilai >= 80 <=100 :
    print("Dengan Grade : A")
elif total_nilai >= 70 <= 79 :
    print("Dengan Grade : B")
elif total_nilai >= 60 <= 69 :
    print("Dengan Grade : C")
elif total_nilai >= 31 <= 59 :
    print("Dengan Grade : D")
elif total_nilai >= 0 <=30 :
    print("Dengan Grade : E")
else :
    print('CATATAN : "TOLONG BAGA TUH JANGAN OVERDOSIS"')

if total_nilai > 100 :
    print("Tak Ku luluskan baru padan muke")
elif total_nilai >= 60 :
    print("Dan dinyatakan : LULUS")
elif total_nilai >= 0 <= 59:
    print("Dan dinyatakan : TIDAK LULUS")
else :
    print("DAH BALEK KE RAHIM IBUMU SANAK")





    



   



# Tugas PERTAMA

# OPERATOR ASSIGNMENT

print("================================================")
print("---------ASSIGNMENT---------")
print("================================================")
apel = int(input("Iky mempunyai apel sebanyak :"))
apel2 = int(input("Lalu Iky membeli lagi sebanyak :"))
apel += apel2
apel3 = int(input("setelah itu Iky membagikan apel kepada Annisa sebanyak :"))
apel -= apel3
print("dan sekarang apel Iky tinggal tersisa :",apel)
print("===============================================")
enter = input("Klik enter  untuk LANJUT :")


# OPERATOR LOGIKA

print("===============================================")
print("---------LOGIKA---------")
print("===============================================")
#-----------0++++++++++5----------10+++++++++++15----------
inputUser = float(input("Masukan angka yang bernilai \nlebih dari 0 dan kurang dari 5 \natau \nlebih dari 10 dan kurang dari 15\n:"))
isiLebihDari0 = inputUser > 0
isiKurangDari5 = inputUser < 5
isCorrect1 = isiLebihDari0 and isiKurangDari5

isiLebihDari10 = inputUser > 10
isiKurangDari15 = inputUser < 15
isCorrect2 = isiLebihDari10 and isiKurangDari15

isCorrect3 = isCorrect1 or isCorrect2
print("angka yang anda masukan",isCorrect3)
print("==============================================")
enter = input("Klik enter  untuk LANJUT :")


# OPERATOR BITWISE

print("==============================================")
print("---------BITWISE---------")
print("==============================================")
a = int(input("Masukan Angka pertama:"))
print("angka",a,"dikonversikan ke biner menjadi :",format(a,"08b"))
operasi = input("pilih Operasi bitwise yang ingin di gunakan\n (& , | , ^ , >> , << , ~) :")
if operasi == "~" :
    print("\n========================================")
    c = ~a
    print("nilai :",format(a,"08b"))
    print("----------------------------(~)")
    print("nilai :",format(c,"08b"))
else :
    b = int(input("Masukan Angka kedua:"))
    print("angka",b,"dikonversikan ke biner menjadi :",format(b,"08b"))
if operasi == "&" :
    print("\n========================================")
    print("nilai :",format(a,"08b"))
    print("nilai :",format(b,"08b"))
    print("-------------------(&)")
    c = a & b
    print("nilai :",format(c,"08b"))
    print("==========================================")
    enter = input("Klik enter  untuk LANJUT :")
elif operasi == "|" :
    print("\n========================================")
    print("nilai :",format(a,"08b"))
    print("nilai :",format(b,"08b"))
    print("-------------------(|)")
    c = a | b
    print("nilai :",format(c,"08b"))
    print("==========================================")
    enter = input("Klik enter  untuk LANJUT :")
elif operasi == "^" :
    print("\n========================================")
    print("nilai :",format(a,"08b"))
    print("nilai :",format(b,"08b"))
    print("-------------------(^)")
    c = a ^ b
    print("nilai :",format(c,"08b"))
    print("==========================================")
    enter = input("Klik enter  untuk LANJUT :")
elif operasi == "<<" :
    print("\n========================================")
    print("nilai :",format(a,"08b"))
    print("nilai :",format(b,"08b"))
    print("-------------------(<<)")
    c = a << b
    print("nilai :",format(c,"08b"))
    print("==========================================")
    enter = input("Klik enter  untuk LANJUT :")
elif operasi == ">>" :
    print("\n========================================")
    print("nilai :",format(a,"08b"))
    print("nilai :",format(b,"08b"))
    print("-------------------(>>)")
    c = a >> b
    print("nilai :",format(c,"08b"))
    print("===========================================")
    enter = input("Klik enter  untuk LANJUT :")
elif operasi == "~" :
    print("===========================================")
    enter = input("Klik enter  untuk LANJUT :")
else :
    print("Operator tidak TEPAT")

# OPERATOR IDENTITAS

print("================================================")
print("---------IDENTITAS---------")
print("================================================")
data = int(input("Masukan bilangan bulat pertama :"))
data2 = int(input("Masukan Bilangan bulat kedua kedua :"))
print("================================================")
print("Bilangan bulat pertama adalah :",data)#,type(data),hex(id(data)))
print("Bilangan bulat kedua adalah :",data2)#,type(data2),hex(id(data2)))
print("apakah Bilangan bulat pertama dan bilangan bulat kedua identik :" ,data is data2)
print("===============================================")
enter = input("Klik enter  untuk LANJUT :")


# OPERATOR KEANGGOTAAN

print("===============================================")
print("---------KEANGGOTAAN---------")
print("===============================================")
nama = input("Masukan Nama:")
print("Nama anda adalah :",nama)
huruf = input("masukan huruf yang terdapat di nama anda:")
print("apakah huruf",huruf,"termasuk anggota di nama",nama,":", huruf in nama)
print("===============================================")
enter = input("Klik enter untuk SELESAI :")
print("===============================================")
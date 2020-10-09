print("===============================================")

#masukan input dari user
print("Selamat Datang di Program Kalkulator sederhana")
enter = input("klik enter untuk lanjut : ")
print("Program ini dibuat oleh Felix Rizky Lesmana")
enter = input("klik enter untuk lanjut : ")

print("===============================================")
a = float(input("Masukan nilai pertama: "))
aritmatika = input("pilih operator +, -, /, * : ")
b = int(input("Masukan nilai kedua: "))

if aritmatika == '+' :
    print(a ,"+", b, "= ",(a + b))
elif aritmatika == '-' :
    print(a ,"-", b, "= ",(a - b))
elif aritmatika == '*' :
    print(a ,"*", b, "= ",(a * b))
elif aritmatika == '/' :
    print(a ,"/", b, "= ",(a / b))
else :
    print("Operator salah")
enter = input("klik enter untuk selesai : ")


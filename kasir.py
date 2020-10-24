print("GEROBAK FRIED CHICKEN".center(64,"-"))
print(64*"-")
print("kode".ljust(20," "),"Jenis potong".center(20," "),"Harga".rjust(20," "))
print("D".ljust(20," "),"Dada".center(20," "),"Rp. 2500".rjust(20," "))
print("P".ljust(20," "),"Paha".center(20," "),"Rp. 2000".rjust(20," "))
print("S".ljust(20," "),"Sayap".center(20," "),"Rp. 1500".rjust(20," "))
print(64*"-")

# Banyak Jenis
bj = int(input("Banyak jenis : "))
# Kode Potong
kp = []
# Banyak Potong
bp = []
# Jenis potong
jp = []
# Harga Satuan
hs = []
# Jumlah Harga
jh = []

# Input
a = 0
for a in range(bj) :
    print("Jenis ke - ", a+1)
    kp.append(input("Masukan Kode Potong (D/P/S) : "))
    bp.append(int(input("Banyak Potong : ")))
    if kp[a] == "D" or kp[a] == "d":
        jp.append("Dada")
        hs.append(2500)
        jh.append(bp[a] * 2500)
    elif kp[a] == "P" or kp[a] == "p":
        jp.append("Paha")
        hs.append(2000)
        jh.append(bp[a] * 2000)
    elif kp[a] == "S" or kp[a] == "s":
        jp.append("Sayap")
        hs.append(1500)
        jh.append(bp[a] * 1500)
    else :
        jp.append("Error Not Found")
        hs.append(0)
        jh.append(bp[a] * 0)
# Output
print("="*18,"GEROBAK FRIED CHICKEN","="*18)
print("NO".ljust(3," "),"Jenis-Potong".center(5," "),"Harga-satuan".center(15," "),"Banyak-beli".ljust(10," "),"Jumlah-harga".rjust(13," "))
print("-"*59)
b = 0
jb = 0
for b in range(bj):
    jb += jh[b]
    print(b+1," "*3,jp[b]," "*11,hs[b]," "*8,bp[b]," "*10,"Rp ",jh[b])
    b += 1
print("-"*59)
print(" "*33,"Jumlah bayar = Rp ",jb)
pajak = jb * (10/100)
total = jb + pajak
print(" "*33,"Pajak 10 %   = Rp ",pajak)
print(" "*33,"Total Bayar  = Rp ",total)





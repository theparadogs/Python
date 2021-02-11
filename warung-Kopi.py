print("El's Coffee".center(70,"-"))
print(70*"-")
print("kode".ljust(20," "),"Jenis Kopi".center(20," "),"Harga".rjust(20," "))
print(70*"-")
print("1".ljust(20," "),"Espressoo".center(20," "),"Rp. 15000".rjust(20," "))
print("2".ljust(20," "),"FlatWhite".center(20," "),"Rp. 30000".rjust(20," "))
print("3".ljust(20," "),"Picollooo".center(20," "),"Rp. 35000".rjust(20," "))
print("4".ljust(20," "),"Machiatoo".center(20," "),"Rp. 45000".rjust(20," "))
print("5".ljust(20," "),"Cold Brew".center(20," "),"Rp. 50000".rjust(20," "))
print(64*"-")

nk = input("Masukan nama Kasir : ")
np = input("Masukan nama Pembeli : ")

# Banyak Jenis
bj = int(input("Banyak jenis : "))
# Kode kopi
kk = []
# Banyak pemesanan kopi
bp = []
# Jenis kopi
jk = []
# Harga Satuan
hs = []
# Jumlah Harga
jh = []




# Input
a = 0
for a in range(bj) :
    print("Jenis ke - ", a+1)
    kk.append(input("Masukan Kode Kopi (1/2/3/4/5) : "))
    bp.append(int(input("Banyak Pemesanan Kopi : ")))
    if kk[a] == "1" :
        jk.append("Espressoo")
        hs.append(15000)
        jh.append(bp[a] * 15000)
    elif kk[a] == "2" :
        jk.append("FlatWhite")
        hs.append(30000)
        jh.append(bp[a] * 30000)
    elif kk[a] == "3" :
        jk.append("Picollooo")
        hs.append(35000)
        jh.append(bp[a] * 35000)
    elif kk[a] == "4" :
        jk.append("Machiatoo")
        hs.append(45000)
        jh.append(bp[a] * 45000)
    elif kk[a] == "5" :
        jk.append("Cold Brew")
        hs.append(50000)
        jh.append(bp[a] * 50000)
    else :
        jk.append("Error Not Found")
        hs.append(0)
        jh.append(bp[a] * 0)


    
# Output
print(70*"-")
print("="*18,"El's Coffee","="*18)
print(70*"-")
print("Nama kasir       : ",nk)
print("Nama Pembeli     : ",np)
print("NO".ljust(3," "),"Nama".center(5," "),"Harga".center(15," "),"Jumlah".ljust(10," "),"Total".rjust(13," "))
print("-"*59)
b = 0
jb = 0
for b in range(bj):
    jb += jh[b]
    print(b+1," "*3,jk[b]," "*11,hs[b]," "*8,bp[b]," "*10,"Rp ",jh[b])
    b += 1
print("-"*59)
print("Jumlah bayar = Rp ",jb)
#uang bayar
ub = int(input("Masukan uang bayar = Rp "))
kmb = ub - jb
print("Kembalian  = Rp ",kmb)
print("-"*70)
print("Terima kasih telah membeli :)")
print("-"*70)
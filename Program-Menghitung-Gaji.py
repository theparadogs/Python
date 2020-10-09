print("----------------------------")
print("PROGRAM HITUNG GAJI KARYAWAN")
print("----------------------------")

# GAJI POKOK
gp = 300000
# BONUS LEMBUR
bonus = 3500

#DATA INPUT
#NAMA
nama = input("Nama karyawan : ")

#JABATAN
jabatan = input("Golongan jabatan (1/2/3)  : ")
if jabatan == "1" :
    tj = (5/100) * gp
elif jabatan == "2" :
    tj = (10/100) * gp
elif jabatan == "3" :
        tj = (15/100) * gp


# LOPPING JABATAN
jab = ["1","2","3"]
while jabatan not in jab:
    loop = input("Golongan jabatan (1,2,3)  : ")

    if loop == "1" :
        tj = (5/100) * gp
        break
    elif loop == "2" :
        tj = (10/100) * gp
        break
    elif loop == "3" :
        tj = (15/100) * gp
        break


#PENDIDIKAN
pendidikan = input("Pendidikan (SMA/D1/D3/S1) : ")
if pendidikan == "SMA" :
    tp = (2.5/100) * gp
elif pendidikan == "D1" :
    tp = (5/100) * gp
elif pendidikan == "D3" :
    tp = (20/100) * gp
elif pendidikan == "S1" :
    tp = (30/100) * gp

# LOOPING PENDIDIKAN
pend = ["SMA","D1","D3","S1"]
while pendidikan not in pend :
    loop = input("Pendidikan (SMA/D1/D3/S1) : ")
    
    if loop == "SMA" :
        tp = (2.5/100) * gp
        break
    elif loop == "D1" :
        tp = (5/100) * gp
        break
    elif loop == "D3" :
        tp = (20/100) * gp
        break
    elif loop == "S1" :
        tp = (30/100) * gp
        break


#JAM KERJA

jam_kerja = int(input("Jumlah jam kerja          : "))
if jam_kerja <= 8 :
    hl = 0
elif jam_kerja > 8 :
    hl = (jam_kerja - 8) *  bonus

print("Karyawan yang bernama " + nama)
print("Honor yang diterima")
print("-----------------------------------------------------")
print("     Gaji Pokok              = Rp",gp)
print("     Tunjangan Jabatan       = Rp",int(tj))
print("     Tunjangan Pendidikan    = Rp",int(tp))
print("     Honor Lembur            = Rp",int(hl))
print("--------------------------------------------------(+)")
total = tj + tp + hl + gp
print("         Total Gaji          = Rp",int(total))
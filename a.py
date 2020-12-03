#!/usr/bin/env python
# -*- coding: utf-8 -*-
i=0
nm=[]
ni=[]
tgs=[]
uts=[]
uas=[]
akh=[]
raw_input=input

while True :
    nama = raw_input("Nama\t\t: ")
    nm.append(nama)
    nim = input("NIM\t\t    : ")
    ni.append(nim)
    nilai_tugas = int(input("Nilai Tugas\t: "))
    tgs.append(nilai_tugas)
    nilai_uts = int(input("Nilai UTS\t: "))
    uts.append(nilai_uts)
    nilai_uas = int(input("Nilai UAS\t: "))
    uas.append(nilai_uas)
    akhir = (nilai_tugas*30/100)+(nilai_uts*35/100)+(nilai_uas*35/100)
    akh.append(akhir)

    data = ' '
    while data!='y' and data!='t':
        data = raw_input("Tambah data (y/t)? ")
    i+=1
    if data=='t':
        break

print ("================UNIVERSITAS PELITA BANGSA==================")
print ("| No |    Nama    |     NIM     |Tugas| UTS | UAS | Akhir |")
print ("===========================================================")
for n in range(i):
     print ("| ",n+1, "|  ", nm[n], " | ", ni[n], " | ", tgs[n], "| ", uts[n], "| ", uas[n],"| ", akh[n], "|")
print ("===========================================================")

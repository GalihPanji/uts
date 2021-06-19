"""
Created on Thu Jun 17 09:42:01 2021

@author: Galih
"""
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==============================================")
    print(" TRANSAKSI BIAYA EKSPEDISI ")
    print("==============================================")
    print(" a = Surabaya")
    print(" b = Bandung")
    print(" ")

    kode =['a','b']
    kota = ['Surabaya','Bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]

    pilihan = input(">> Masukkan Kode Tujuan = ")
    
    no = 0
    while no < len(kode):
        if kode[no] == pilihan:

            print(">>> Pilihan Tujuan   = " + kota[no ])
            print(">>>          Jarak   = " + str(jarak[no]) + " km")
            print(">>>  Ongkir per Km   = Rp. " + str(ongkirperkm[no]))

            ongkir = jarak[no] * ongkirperkm[no]

            print(">>>> Total           = Rp. " + str(ongkir))
            print(" ")
            print("==============================================")
    
        no = no + 1 
        
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break

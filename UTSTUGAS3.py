"""
Created on Thu Jun 17 11:13:12 2021

@author: Galih
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("=========================================================")
    print("                    TRANSAKSI TOKO BANGUNAN UD. SUBUR ")
    print("=========================================================")
    print("a = Asbes Gelombang")
    print("b = Cat Tembok Dulux 1 Galon")
    print("c = Cat Tembok Avian 1 Galon")
    print("d = Aquaproof 5kg")
    print("e = Seng 2mm")
    print("f = Spandeks 1mm")
    print(" ")

    kode =['a','b','c','d','e','f']
    oli = ['Asbes Gelombang','Cat Tembok Dulux 1 Galon', 'Cat Tembok Avian 1 Galon', 'Aquaproof 5kg', 'Seng 2mm' ,'Spandeks 1mm']
    Harga = [60000,250000,350000,50000,70000,92000]
    diskon = 0.05
    ppn = 0.02
    minimaldiskon =  500000
    TotalAwal = 0
    NilaiDiskon = 0

  
    pilih = input("Masukkan Kode Barang = ")    

    no = 0
    while no < len(kode):
        if kode[no] == pilih:

            print("Pilihan Barang  = " + oli[no])
            print("Harga Barang = Rp " + str (Harga[no]))

            


            JmlBeli = int(input("Masukkan Jumlah Oli yang dibeli = "))
            
            if JmlBeli > 0:
                TotalAwal = Harga[no] * int(JmlBeli)
                print(">> Total Awal  = Rp " + str (TotalAwal))
            
    
            if (TotalAwal) > minimaldiskon:
                NilaiDiskon = int(TotalAwal) * float(diskon)
                print("Nilai Diskon = " + str (NilaiDiskon))
            else: 0

            ppn = 0.02 * (int(TotalAwal) - int(NilaiDiskon))
            print("PPN  = " + str (ppn))

 
            TotalBayar = int(TotalAwal) - int(NilaiDiskon) + ppn
            print("Total dibayarkan                = Rp " + str (TotalBayar))
            print()
            print("=========================================================")
            
        no = no + 1


    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break

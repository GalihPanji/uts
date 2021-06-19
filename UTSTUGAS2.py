"""
Created on Thu Jun 17 10:23:08 2021

@author: Galih
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("=========================================================")
    print("                    TRANSAKSI BIAYA OLI ")
    print("=========================================================")
    print("a = Duration SW20 1L")
    print("b = Castrol Magnatec 1L")
    print("c = Federal Supreme XX 1L")
    print("d = Yamalube 1L")
    print("e = Shell 1L")
    print(" ")

    kode =['a','b','c','d','e']
    oli = ['Duration SW20 1L','Castrol Magnatec 1L', 'Federal Supreme XX 1L', 'Yamalube 1L', 'Shell 1L']
    Harga = [53000,50000,54000,45000,46000]
    diskon = 0.05
    ppn = 0.01
    minimaldiskon =  200000
    TotalAwal = 0
    NilaiDiskon = 0

  
    pilih = input("Masukkan Kode Oli = ")    

    no = 0
    while no <= len(kode):
        if kode[no] == pilih:

            print("Pilihan Oli  = " + oli[no])
            print("Harga Oli = Rp " + str (Harga[no]))

            


            JmlBeli = int(input("Masukkan Jumlah Oli yang dibeli = "))
            
            if JmlBeli > 0:
                TotalAwal = Harga[no] * int(JmlBeli)
                print(">> Total Awal  = Rp " + str (TotalAwal))
            
    
            if (TotalAwal) > minimaldiskon:
                NilaiDiskon = int(TotalAwal) * float(diskon)
                print("Nilai Diskon = " + str (NilaiDiskon))
            else: 0

            ppn = 0.01 * (int(TotalAwal) - int(NilaiDiskon))
            print("PPN  = " + str (ppn))

 
            TotalBayar = int(TotalAwal) - int(NilaiDiskon) + ppn
            print("Total dibayarkan                = Rp " + str (TotalBayar))
            print()
            print("=========================================================")
            
        no = no + 1


    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break
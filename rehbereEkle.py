
def rehbereEkleme():
    f = open("c:\\Users\\yasin\\Desktop\\dosyaIslemi\\rehber.txt", "a")
    for i in range(1):
        global kullanıcı
        #kullanıcı.append(input(f"Kişi adını ve numarasını giriniz:"))
        ad=str(input("AD: "))
        soyad=str(input("SOYAD: "))
        numara=str(input("NUMARA: "))
        kullanıcı="AD: "+ad+" SOYAD: "+soyad+" Numara: "+numara+"\n"
        f.write(kullanıcı)##!AD SOYADA VE AYRICA NUMARUYA ÇEVİR
        f.close()
def main():
    rehbereEkleme()

if __name__ == "__main__":
    main()
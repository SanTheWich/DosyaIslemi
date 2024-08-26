#! PROJE 2
kullanıcı=[]
def dosyaOlustur():
    f = open("c:\\Users\\yasin\\Desktop\\dosyaIslemi\\rehber.txt", "a")
    for i in range(1):
        global kullanıcı
        kullanıcı.append(input(f"Kişi adını ve numarasını giriniz:"))
        f.write(kullanıcı[i],"\n")
        
    f.close() # oluşturulan her dosya kapatılmalıdır.
def listele():
    f = open("c:\\Users\\yasin\\Desktop\\dosyaIslemi\\rehber.txt", "r")
    count=0
    for x in f:
        count+=1
        print(f"{count}-)",x)
    #!
    # f = open('c:\\Users\\yasin\\Desktop\\dosyaIslemi\\rehber.txt', 'r')
    # count = 0

    # while True:
    #     count += 1
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(f"{count}-) {line.strip()}")

    f.close()


def sil():
    print()

print("╔═════════════════════════════╗")
print("║    Rehber Kayıt Listesi     ║")
print("╠═════════════════════════════╣")
print("║1-)Rehbere Ekle              ║")
print("║2-)Kayıtları Listele         ║")
print("║3-)Kayıt Sil                 ║")
print("║4-)Kayıt Düzenle             ║")
print("╚═════════════════════════════╝")
secim=int(input("\nLütfen seçim yapınız: "))

if secim==1:
    dosyaOlustur()
elif secim==2:
    listele()
elif secim==3:
    sil()

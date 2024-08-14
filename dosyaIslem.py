#! PROJE 2
kullanıcı=[]
def dosyaOlustur():
    f = open("c:\\Users\\yasin\\Desktop\\dosyaIslem\\rehber.txt", "a")
    for i in range(1):
        global kullanıcı
        kullanıcı.append(input(f"Kullanıcı {i} adını giriniz:"))
        f.write(f"{i}")
        f.write(kullanıcı[i])
        
    f.close() # oluşturulan her dosya kapatılmalıdır.
def listele():
    f = open("c:\\Users\\yasin\\Desktop\\dosyaIslem\\rehber.txt", "r")
    for i in range(1):
        print(f.read())

    f.close() # oluşturulan her dosya kapatılmalıdır.
def sil():
    print()

print("╔═════════════════════════════╗")
print("║    Rehber Kayıt Listesi     ║")
print("╠═════════════════════════════╣")
print("║1-)İsim Ekle                 ║")
print("║2-)Listele                   ║")
print("║1-)İsim Ekle                 ║")

secim=int(input("\nLütfen seçim yapınız: "))

if secim==1:
    dosyaOlustur()
elif secim==2:
    listele()
elif secim==3:
    sil()
abc = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\rehber.txt", "w")
abc.write("Dosyaya kayded-2.\nİkinci satır!!\n")
abc.write("Üçüncü satır") 
abc.write("Üçüncü satır") 
abc.close() # oluşturulan her dosya kapatılmalıdır.

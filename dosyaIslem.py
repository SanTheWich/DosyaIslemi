#! PROJE 2
import rehbereEkle
import listeleme
kullanıcı=[]
# def listele():
#     f = open("c:\\Users\\yasin\\Desktop\\dosyaIslemi\\rehber.txt", "r")
#     count=0
#     for x in f:
#         count+=1
#         print(f"{count}-)",x)
#     f.close()


def sil():
    print()
def duzenle():
    print()

print("╔═════════════════════════════╗")
print("║    Rehber Kayıt Listesi     ║")
print("╠═════════════════════════════╣")
print("║1-)Rehbere Ekle              ║")
print("║2-)Kayıtları Listele         ║")
print("║4-)Kayıt Arama               ║")
print("║3-)Kayıt Sil                 ║")
print("║4-)Kayıt Düzenle             ║")
print("╚═════════════════════════════╝")
secim=int(input("\nLütfen seçim yapınız: "))

if secim==1:
    rehbereEkle.rehbereEkleme()
elif secim==2:
    listeleme.listele()
elif secim==3:
    ()
elif secim==4:
    duzenle()
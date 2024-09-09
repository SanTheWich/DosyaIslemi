#! PROJE 2
import rehbereEkle
import listeleme
import arama
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
print("║3-)Kayıt Arama               ║")
print("║4-)Kayıt Sil                 ║")
print("╚═════════════════════════════╝")
secim=int(input("\nLütfen seçim yapınız: "))

if secim==1:
    rehbereEkle.rehbereEkleme()
elif secim==2:
    listeleme.listele()
elif secim==3:
    arama.ara()
elif secim==3:
    duzenle()

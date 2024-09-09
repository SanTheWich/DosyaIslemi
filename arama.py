# import ast
# def ara():
#     kayit = {}
#     dosya = open("rehber.txt","r")
#     okunan = dosya.readlines()
#     print (okunan)
#     print("\nSatır satır")
#     for a in okunan:
#         kayit = ast.literal_eval(a)
#         print (type(kayit))
#         print(kayit)
#         print(kayit["ad"])
#     dosya.close()
# def ara():
    # dosya = open("rehber.txt","r")
    # okunan = dosya.readlines()
    # import os
    # liste = os.listdir()
    # durum = "yok"
    # for a in liste:
    #     aranan=str(input("Aranan: "))
    #     if a == aranan: durum = "var"

    # print(durum)
    # if durum == "yok":
    #     os.mkdir(aranan)
import os
def ara():
    liste = os.listdir()
    durum = "yok"
    aranan=str(input("Aranıcak Isim: "))
    for a in liste:
        if a == aranan: durum = "var"

    print(durum)
    if durum == "yok":
        os.mkdir(aranan)

def main():
    ara()

if __name__ == "__main__":
    main()

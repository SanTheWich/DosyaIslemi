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
def ara():
    with open('rehber.txt') as f:
        aranan=str(input("Aranan: "))
        if aranan in f.read():
            kelime=(f.readline(f.read))
            print("true")
            print(kelime)
        else:
            print("Yok")

def main():
    ara()

if __name__ == "__main__":
    main()

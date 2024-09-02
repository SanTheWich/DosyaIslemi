def listele():
    f = open("c:\\Users\\yasin\\Desktop\\dosyaIslemi\\rehber.txt", "r")
    count=0
    for x in f:
        count+=1
        print(f"{count}-)",x)
    f.close()
def main():
    listele()

if __name__ == "__main__":
    main()
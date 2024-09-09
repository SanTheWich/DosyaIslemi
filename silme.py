import os
ad=str(input("Silinecek Isim: "))
def sil(ad):
    original_file = "rehber.txt"
    temp_file = "temp.txt"
    string_to_delete=[ad]
    with open(original_file, "r") as input:
        with open(temp_file, "w") as output:
            for line in input:
                for word in string_to_delete:
                    line = line.replace(word, "")
                output.write(line)

# replace file with original name
os.replace('temp.txt', 'rehber.txt')
def main():
    sil(ad)

if __name__ == "__main__":
    main()

import os
i=1
files = os.listdir("Excersise1-clutteredfolder")
for file in files:
    if file.endswith(".txt"):
        os.rename(f"Excersise1-clutteredfolder/{file}",f"Excersise1-clutteredfolder/{i}.txt")
        i=1+i
        print(file)
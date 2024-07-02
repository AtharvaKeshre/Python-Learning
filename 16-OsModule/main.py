import os

if(not os.path.exists("data")):
    os.mkdir("Data")


# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")


# for i in range(0,100):
#     os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")

folders = os.listdir("data")

# print(folders)

for folder in folders:
    if(not os.path.exists(f"data/{folder}")):
        os.rmdir(f"data/{folder}")
        print(os.listdir(f"data/{folder}"))
        if(not os.path.exists(f"data/{folder}/main.py")):
            with open(f"data/{folder}/main.py",'w'):
                pass
file = open("text.txt", 'r')
i = 0

while True:
    line = file.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"Marks of student {i} in English id {m1}")
    print(f"Marks of student {i} in English id {m2}")
    print(f"Marks of student {i} in English id {m3}")
    print(line)
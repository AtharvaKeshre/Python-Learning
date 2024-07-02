    # This is how to open a file 

# file = open("text.txt", 'r')
# text = file.read()
# print(text)
# file.close()

    # This is how to write a file 
file = open("text.txt", 'w')
text = file.write("Hello World")
print(text)
file.close()

    # This is how to write a file without using the close()
with open('text.txt', 'r') as file:
    text = file.read()
    print(text)
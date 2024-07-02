letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Atharva"
# print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")
price = 49.0999
text = f"For only ${price:.2f}"

print(text)
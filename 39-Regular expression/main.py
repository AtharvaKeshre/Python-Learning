import re

pattern = r"[A-Z]lanet"

text = '''A Planet is a large, rounded body Glanet that is generally required to be in orbit around a star, stellar remnant or brown dwarf. The Solar System has eight (pictured): four terrestrial planets, Mercury, Venus, Earth and Mars; and four giant planets, Jupiter, Saturn, Uranus and Neptune. The term "Planet" at first included the Sun, Moon and the five planets visible to the naked eye in the sky; they were seen as having associations with the gods. Copernicus theorized the Earth was a planet and, like the others, orbited the Sun. "Planet" came to include many objects, such as moons, within and beyond the Solar System. The International Astronomical Slanet Union in 2006 defined a planet in the Solar System to have cleared its neighborhood of other bodies, and that extrasolar planets should orbit stars and not be large enough to support deuterium fusion. Many planetary scientists, though, still apply the word "planet" more broadly, including dwarf planets, planetary-mass moons, rogue planets and brown dwarfs.'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
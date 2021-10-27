print("Klasser")
print("=======\n")


class car():
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


bil1 = car("Saab", "Grön", 2004)
bil2 = car("Audi", "Röd", 2006)
bil3 = car("Volvo", "Blå", 2020)

print(
    f"Första bilen är en {bil1.brand} och är {bil1.color} och den kom ut {bil1.year}")

print(
    f"Andra bilen är en {bil2.brand} och är {bil2.color} och den kom ut {bil2.year}")

print(
    f"Tredje bilen är en {bil3.brand} och är {bil3.color} och den kom ut {bil3.year} \n")

shopping_list = {
            "piekarnia" : ["Chleb", "Paczek", "Bulki"],
            "warzywniak" : ['Marchew', 'Seler', 'Rukola'],
            "biedronka" : ['Ser', 'Maslo'],
}

x = 0
print()
for shop, items in shopping_list.items():
    print(f"idę do {shop.capitalize()} i kupuję {items}")
    for items in shopping_list[shop]:
        x += 1
        
print (f"w sumie kupuję {x} produktów")

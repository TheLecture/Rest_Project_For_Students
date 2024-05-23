menu=[
    {"first":{"Home Bread":12,"Fresh Salad":18,"Hummus":16,"French Fries":17}},
    {"main":{"Kebab":24,"Chicken":24,"Steak":113,"Combination":160}},
    {"desserts":{"Malabi":15,"Chocolate Cake":17,"Ice-Cream":8}},
    {"drinks":{"Coca-Cola":12,"Diet-Coke":12,"Mineral-Water":10,"Orange juice":12}}
]

order = ["Coca-Cola","Home Bread","Fresh Salad","Steak"]

check = []

for item in order:
    for som in menu:
        for cat in som.values():
            for dish in cat:
                if item==dish:
                    check.append(cat[dish])

total = 0

for price in check:
    print(price,"\n")
    total+=price

print(total)
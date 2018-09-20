inventory = {'rope': 4, 'apples': 5, 'gold': 98, 'potion': 3}

def displayInventory(inv):
    for k, v in inv.items():
        print(k, v)

displayInventory(inventory)
inventory = {'rope': 4, 'apples': 5, 'gold': 98, 'potion': 3}

dragonLoot = ['gold', 'rope', 'gold', 'gold', 'apples', 'diamond', 'diamond']


def displayInventory(inv):
    item_count = 0

    print('\n' + 'Your Inventory: ' + '\n')
    for k, v in inv.items():
        print(v, k)
        item_count += v
    
    print('\n' + 'There are ' + str(item_count) + ' items in your inventory' + '\n')


def addToInventory(inv, loot):
    for item in loot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


addToInventory(inventory, dragonLoot)
displayInventory(inventory)
# 01/08/2020

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin':42, 'rope':1}


def add_to_inventory(inventory, added_items):
    print('Inventory:\n')
    coins = 0
    dagger = 0
    ruby = 0
    for item in dragon_loot:
        if 'gold coin' == item in dragon_loot:
            coins += 1
            
    for i in dragon_loot:
        if 'dagger' == i in dragon_loot:
            dagger += 1
    for v in dragon_loot:
        if 'ruby' == v in dragon_loot:
            ruby += 1
    coins = coins + inv['gold coin']
    for items in dragon_loot:
        if items not in inv:
            inv.setdefault(items, 1)
    for k, v in inv.items():
    	print(v, k)

add_to_inventory(inv, dragon_loot)
    
    



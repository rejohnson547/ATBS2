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
            
    #for i in dragon_loot:
        if 'dagger' in dragon_loot:
            dagger += 1
    #for v in dragon_loot:
        if 'ruby' in dragon_loot:
            ruby += 1
    print(coins)

add_to_inventory(inv, dragon_loot)
    
    



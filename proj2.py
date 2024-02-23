#MINI PROJECT 2: CREATING AN INVENTORY MANAGEMENT SYSTEM USING PYTHON


inventory = {} #item: [quantity_available, price_of_each]

def add_item(item, quantity_available, price_of_each):
    if item not in inventory.keys():
        inventory[item] = [quantity_available, price_of_each]
    else:
        inventory[item] = [inventory[item][0] + quantity_available, (inventory[item][1] + price_of_each)/2] 

def list_items(item, price):
    print(f'Cost of each {item} is Rs.{price}.')

def sell_items(quan_to_sell, item, price):
    if item in inventory.keys():
        if inventory[item][0] > quan_to_sell:
            print(f'{quan_to_sell} {item} sold')
            inventory[item] = [inventory[item][0] - quan_to_sell, price_of_each]
            print(f'{inventory[item][0]} of {item} left.')
            if inventory[item][0] < 10:
                print('RESTOCK SOON!')
        
        else:
            print('Item insufficient to sell!')
    
    else:
        print('Item not found in inventory.')

def show_command():
    print('add: add item in inventory and if it exists update its quantity and price with the average of the old and new ones')
    print('sell: sell items and update availability')
    print('list: list pair of item and price')
    print('help: to show what can be done')
    print('quit: quit program')


while True:
    user_input = input('Enter a command or type \'help\' to see what can be done: ')

    if user_input == 'help':
        show_command()

    elif user_input == 'add':
        i = input('Enter item: ') #item
        q = int(input('Enter quantity of item: ')) #quantity
        p = float(input('Enter per item price upto two digits: ')) #price
        add_item(i, q, p)

    elif user_input == 'sell':
        i = input('Enter item you want to sell: ') #item
        q = int(input('Enter quantity of item: ')) #quantity
        p = float(input('Enter per item price upto two digits: ')) #price
        sell_items(q, i, p)

    elif user_input == 'quit':
        break

    elif user_input == 'list':
        i = input('Enter item: ') #item
        p = float(input('Enter per item price upto two digits: ')) #price
        list_items(i, p)

    else:
        print('Invalid command, try AGAIN!')

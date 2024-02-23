#MINI PROJECT 1: CREATING A SHOPPING CART USING PYTHON


shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f'Added {item} to the list.')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed {item} from the list.')
    else:
        print(f'{item} not found in the list.')

def show_list():
    print(shopping_list)

def clear_list():
    shopping_list.clear()
    print(f'List is cleared: {shopping_list}')

def sort_list():
    shopping_list.sort()
    print(f'List is sorted: {shopping_list}')

def list_of_commands():
    print('add: add an item to the list')
    print('remove : removed an item from the list')
    print('show: shows the list')
    print('clear : clears the list')
    print('sort : sorts the list')
    print('quit : quit program')
    print('help : shows the list of commands available')


while True:
    user_input = input("Enter a command or type 'help' for the list of commands: ")

    if user_input == 'help':
        list_of_commands()

    elif user_input == 'add':
        ele = input('Enter item to add to the list: ')
        add_item(ele)

    elif user_input == 'remove':
        ele = input('Item you want to remove from the list: ')
        remove_item(ele)

    elif user_input == 'show':
        show_list()

    elif user_input == 'clear':
        clear_list()

    elif user_input == 'sort':
        sort_list()

    elif user_input == 'quit':
        break

    else:
        print('Invalid command!')


'''
OUTPUT:-

Enter a command or type 'help' for the list of commands: help
add: add an item to the list
remove : removed an item from the list
show: shows the list
clear : clears the list
sort : sorts the list
quit : quit program
help : shows the list of commands available
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: cake
Added cake to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: candles
Added candles to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: balloon
Added balloon to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: popper                  
Added popper to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: matches
Added matches to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: gift
Added gift to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: biryani
Added biryani to the list.
Enter a command or type 'help' for the list of commands: add
Enter item to add to the list: sprite
Added sprite to the list.
Enter a command or type 'help' for the list of commands: show
['cake', 'candles', 'balloon', 'popper', 'matches', 'gift', 'biryani', 'sprite']
Enter a command or type 'help' for the list of commands: asd
Invalid command!
Enter a command or type 'help' for the list of commands: sort
List is sorted: ['balloon', 'biryani', 'cake', 'candles', 'gift', 'matches', 'popper', 'sprite']
Enter a command or type 'help' for the list of commands: remove
Item you want to remove from the list: biryani
Removed biryani from the list.
Enter a command or type 'help' for the list of commands: show
['balloon', 'cake', 'candles', 'gift', 'matches', 'popper', 'sprite']
Enter a command or type 'help' for the list of commands: sort
List is sorted: ['balloon', 'cake', 'candles', 'gift', 'matches', 'popper', 'sprite']
Enter a command or type 'help' for the list of commands: clear
List is cleared: []
Enter a command or type 'help' for the list of commands: quit
'''
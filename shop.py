import sys

sale_items = [
    {'item': 'T-shirt', 'price': 19.99},
    {'item': 'Hoodie', 'price': 39.99},
    {'item': 'Cap', 'price': 14.99},
    {'item': 'Mug', 'price': 9.99},
    {'item': 'Keychain', 'price': 5.99},
    {'item': 'Poster', 'price': 12.99},
    {'item': 'Sticker', 'price': 2.99},
    {'item': 'Phone Case', 'price': 24.99},
    {'item': 'Backpack', 'price': 49.99},
    {'item': 'Water Bottle', 'price': 17.99}
]

customer_money = 100
customer_name = input('Hello, what is your name? ')


def purchase_or_exit() -> None:
    print(f'Hi {customer_name}, welcome to the CFG merch store')
    print('Please see the list of items on sale and the respective prices')

    for item in sale_items:
        print(f"Item: {item['item']}, Price: {item['price']}")

    while True:
        option = input('Enter the item you want to purchase (type "exit" to leave): ').lower()

        if option == 'exit':
            print('Thanks for looking through our store today. Goodbye!')
            sys.exit(0)
        elif option == 'stay':
            continue

        selected_item = {}

        for item in sale_items:
            if item['item'].lower() == option:
                selected_item = item
                break

        if not selected_item:
            print('Invalid input, please choose an item on sale.')
            continue

        global customer_money

        if customer_money >= selected_item['price']:
            print(f'Here’s your {selected_item["item"]}!')
            customer_money -= selected_item['price']
            print(f'Your remaining balance is £{customer_money:.2f}.')
            print('Thanks for shopping with us')
            sys.exit(0)
        else:
            print(f'Sorry, you cannot afford the {selected_item["item"]}.')
            add_money = input('Do you want to add more money to your account? (yes or no): ')
            if add_money.lower() == 'yes':
                while True:
                    try:
                        add_amount = float(input('How much do you want to add to your account? '))
                        if add_amount < 0:
                            raise ValueError
                        customer_money += add_amount
                        print(
                            f'You have added £{add_amount:.2f} to your account, your new balance is £{customer_money:.2f}.')
                        break
                    except ValueError:
                        print('Invalid input, please enter a positive number.')
            else:
                print('Goodbye!')
                sys.exit(0)


purchase_or_exit()

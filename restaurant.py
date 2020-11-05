class Menu(dict):
    def __init__(self, menu_items):
        for food, price in menu_items.items():
            self.update({food: price})
    
    def __str__(self):
        print("Welcome!\nWe have amazing things on our menu:")

        # prints menu items in nice format with price formatting and capitalisation
        for food, price in self.items():
            print("{}, Price: £{:,.2f}".format(food.title(), price))

        return "Hope you enjoy your visit"

class Order()


if __name__ == "__main__":
    japanese_items = {"sushi": 9, "ramen": 5, "katsu curry": 6}

    japan_menu = Menu(japanese_items)
    print(japan_menu)
    print(japan_menu.keys())
    print(japan_menu.values())
    japan_menu["ramune"] = 3
    print(japan_menu)
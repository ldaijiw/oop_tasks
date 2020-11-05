class Menu(dict):
    def __init__(self, menu_items):
        for food, price in menu_items.items():
            self.update({food: price})
    
    def __str__(self):
        print("\n\n***\nWelcome!\nWe have amazing things on our menu:")

        # prints menu items in nice format with price formatting and capitalisation
        for food, price in self.items():
            print("{}, Price: £{:,.2f}".format(food.title(), price))

        return "Hope you enjoy your visit\n***"

class Order(list):
    def __init__(self):
        allowed_menus = [k for k, v in globals().items() if isinstance(v, Menu)]
        
        print("\n***Possible Menus:\n")
        for menu in allowed_menus:
            print(menu.replace('_', ' ').title())
        
        self.menu = input("\nWhich menu will you be ordering from?\n").lower().replace(' ', '_')
        assert self.menu in allowed_menus
        print(self.menu)
        
        

if __name__ == "__main__":
    japanese_items = {"sushi": 9, "ramen": 5, "katsu curry": 6}
    lunch_items = {"katsu curry": 5, "onigiri": 2}
    
    japan_menu = Menu(japanese_items)
    japan_lunch_menu = Menu(lunch_items)
    print(japan_lunch_menu)
    japan_menu["ramune"] = 3
    
    leo_order = Order()
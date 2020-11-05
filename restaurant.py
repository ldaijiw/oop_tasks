class Menu(dict):
    def __init__(self, menu_items):
        for item, price in menu_items.items():
            self.update({item: price})




if __name__ == "__main__":
    japanese_items = {"sushi": 9, "ramen": 5, "katsu curry": 6}

    japan_menu = Menu(japanese_items)
    print(japan_menu)
    print(japan_menu.keys())
    print(japan_menu.values())
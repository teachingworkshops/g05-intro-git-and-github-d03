class Item:
    def __init__(self, name, description, discovery):
        # title of item appearing in inventory
        self.name = name
        # text displayed when first picking up the item (automatic action)
        self.discovery = discovery
        # text displayed when item is inspected in inventory
        self.description = description

    def discover(self):
        print(self.discovery)
        choice = input(f"Do you want to pick up the {self.name}? (Y/n)\n")
        choice = choice.strip(" ").lower()

        if len(choice) == 0:  # default
            return True

        return choice[0] == "y"  # if yes

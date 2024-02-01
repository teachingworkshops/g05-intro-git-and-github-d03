class Item:

  def __init__(self, name, description, discovery):
    #title of item appearing in inventory
    self.name = name
    #text displayed when first picking up the item (automatic action)
    self.discovery = discovery
    #text displayed when item is inspected in inventory
    self.description = description

  def discover(self):
    print(self.discovery)

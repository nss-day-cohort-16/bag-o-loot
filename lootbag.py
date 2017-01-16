class LootBag():
  '''This class provides the ability to add and
  remove items from a collection of toys to be
  delivered to children'''

  def add(self, child, toy):
    '''Append the toy to the list of existing toys for the
    specified child'''
    kids = set()
    kids.add(child)

    with open("{}.txt".format(child), "a+") as child_toys:
      child_toys.write(toy+"\n")

    try:
      with open("good_children.txt", "r") as good_kids:
        [ kids.add(k[:-1]) for k in good_kids ]

    except FileNotFoundError:
      print("No good children yet")

    with open("good_children.txt", "w+") as good_kids:
      [good_kids.write(kid+"\n") for kid in kids]

  def remove(self, child, toy):
    '''Remove the toy from the specified child's existing list
    of toys'''
    with open("{}.txt".format(child), "r") as child_toys:
      toys = [ toy[:-1] for toy in child_toys ]

    toys.remove(toy)

    with open("{}.txt".format(child), "w") as child_toys:
      [child_toys.write(toy+"\n") for toy in toys]

    with open("{}.txt".format(child), "r") as child_toys:
      toys = [ toy[:-1] for toy in child_toys ]

    return toys

  def list_good_children(self):
    '''List all children who are getting at least one toy'''

    with open("good_children.txt", "r") as good_kids:
      list_of_kids = [k[:-1] for k in good_kids]

    return list_of_kids


  def get_by_child(self, child):
    '''List all toys for the specified child'''

    with open("{}.txt".format(child), "r") as child_toys:
      toys = [ toy[:-1] for toy in child_toys ]

    return toys

  def toys_delivered(self, child):
    '''Mark a child as having all their toys delivered'''
    pass














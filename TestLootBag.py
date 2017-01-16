import unittest
from lootbag import *

class TestLootBag(unittest.TestCase):

  def test_ToyCanBeAddedToBag(self):

    bag = LootBag()
    toy = "Nerf Gun"
    child = "Teriq"

    # Add a toy to the child's bag
    bag.add(child, toy)

    # Retrieve list of all toys for child
    teriq_toys = bag.get_by_child(child)

    self.assertIn(toy, teriq_toys)

  def test_ToyCanBeRemovedFromBag(self):
    bag = LootBag()
    toy = "Power Ranger"
    child = "Teriq"

    # Add a toy to the child's bag
    bag.add(child, toy)

    # Retrieve list of all toys for child
    teriq_toys = bag.get_by_child(child)

    # Verify that the toy got added
    self.assertIn(toy, teriq_toys)

    # Remove toy from child's bag
    new_toys = bag.remove(child, toy)

    # Verify that the toy got removed
    self.assertNotIn(toy, new_toys)

  def test_CanListChildrenReceivingToys(self):
    bag = LootBag()

    bag.add("Abigail", "Water slide")
    bag.add("Marcus", "Baseball glove")
    bag.add("Sabrina", "Microscope")
    bag.add("Tessa", "Arduino")

    all_good_children = bag.list_good_children()

    self.assertGreater(len(all_good_children), 0)
    self.assertIn("Sabrina", all_good_children)
    self.assertIn("Abigail", all_good_children)
    self.assertIn("Marcus", all_good_children)
    self.assertIn("Tessa", all_good_children)

  def test_CanListAllToysForASingleChild(self):
    bag = LootBag()

    bag.add("Abigail", "Water slide")
    bag.add("Abigail", "Baseball glove")
    bag.add("Abigail", "Microscope")
    bag.add("Abigail", "Arduino")

    abigail_toys = bag.get_by_child("Abigail")

    self.assertGreater(len(abigail_toys), 0)
    pass




import sys
import sqlite3
from peewee import *

db = SqliteDatabase('bagoloot.db')

class Child(Model):
    name = CharField()

    class Meta:
        database = db

class Toy(Model):
    name = CharField()
    child = ForeignKeyField(Child, related_name="toys")

    def __str__(self):
        return self.name

    class Meta:
        database = db

class LootBag():

    def __init__(self):
        try:
            db.connect()
            db.create_tables([Child, Toy])
        except OperationalError:
            pass

    def add_toy_for_child(self, child, toy):
        try:
            kid = Child.select().where(Child.name == child).get()
        except Exception as ex:
            kid = Child.create(name=child)

        the_toy = Toy.create(name=toy, child=kid)

    def remove_toy_for_child(self, child, toy):
        kid = Child.select().where(Child.name == child).get()
        t = Toy.select().where(Toy.child == kid).get()
        t.delete_instance()

    def get_by_child(self, child):
        kid = Child.select().where(Child.name == child).get()
        toys = Toy.select().where(Toy.child == kid)
        return [toy.name for toy in toys]

    def get_list_of_kids(self):
        return [kid for kid in self.good_children.keys()]

    def is_child_happy(self, child):
        return self.good_children[child]["delivered"]

    def deliver_toys_to_child(self, child):
        self.good_children[child]["delivered"] = True

    def report(self):
        toy_ct = fn.Count(Toy.id)
        
        children = (Child
                .select(Child, toy_ct.alias('toy_count'))
                .join(Toy, JOIN.LEFT_OUTER)
                .group_by(Child)
                .order_by(toy_ct.desc()))

        [print("{} has {} toys".format(child.name, child.toy_count)) for child in children]





if __name__ == "__main__":
    bag = LootBag()
    if sys.argv[1] == "add":
      bag.add_toy_for_child(sys.argv[2], sys.argv[3])
      print(bag.get_by_child(sys.argv[2]))
    elif sys.argv[1] == "remove":
      bag.remove_toy_for_child(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ls":
      print(bag.get_by_child(sys.argv[2]))
    elif sys.argv[1] == "report":
      bag.report()












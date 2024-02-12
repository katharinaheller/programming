class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Familiäre Beziehungen definieren
anna = Person("Anna", "female")
albert = Person("Albert", "male")
steven = Person("Steven", "male")
dana = Person("Dana", "female")
emily = Person("Emily", "female")
fred = Person("Fred", "male")
george = Person("George", "male")
hannah = Person("Hannah", "female")
ian = Person("Ian", "male")

anna.add_child(albert)
albert.add_child(steven)
steven.add_child(dana)
steven.add_child(emily)
dana.add_child(fred)
dana.add_child(george)
emily.add_child(hannah)
emily.add_child(ian)

# Funktionen für Abfragen definieren
def is_sibling(person1, person2):
    return person1 != person2 and any(child in person1.children for child in person2.children)

def is_parent(person, child):
    return child in person.children

def is_grandparent(grandparent, grandchild):
    return any(is_parent(parent, grandchild) for parent in grandparent.children)

# Beispielabfragen
print(is_parent(anna, albert))  # True
print(is_sibling(anna, dana))  # False
print(is_grandparent(steven, ian))  # True
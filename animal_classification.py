#animal_classification.py: Separating animals into different groups

class Kingdom():
  def __init__(self,name):
    self.name = "Animalia"

class Phylum(Kingdom):
  Chordata
  
class Class(Phylum):
  Mammalia
  
class Order(Class):
  Carnivora

class Suborder(Order):
  Feliformia
  
class Family(Suborder):
  Felidae
  
class Subfamily(Family):
  Felinae
  
class Genus(Subfamily):
  Felis
  
class Species(Genus):
  F. catus
  Felis catus
  
class CommonName(Species):
  Cat

class Ninja:
  name = ""
  hp = 100
  strength = 70
  speed = 50

  def attack(self, other):
    #k
  

class SuperNinja(Ninja):
  

naruto = Ninja(name="Naruto", hp=100, strength=80, speed=70)
kakashi = Ninja(name="Kakashi", hp=100, strength=60, speed=50)

naruto.attack(kakashi)
kakashi.attack(naruto)
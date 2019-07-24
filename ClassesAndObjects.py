class Robot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight
  def introduceSelf(self):
    print("My name is " + self.name)

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)


class Person:
  def __init__(self, name, personality, isSitting, robotOwned):
    self.name = name
    self.personality = personality
    self.isSitting = isSitting
    self.robotOwned = robotOwned
  def sitDown(self):
    self.isSitting = True
  def standUp(self):
    self.isSitting = False

p1 = Person("Alice", "aggresive", False, r1)
p2 = Person("Becky", "talkative", True, r2)

p1.robotOwned.introduceSelf()
p2.robotOwned.introduceSelf()

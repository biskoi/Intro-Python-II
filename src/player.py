# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
   def __init__(self, name, location):
      self.name = name
      self.location = location

   def __str__(self):
      return f'I\'m {self.name}, and the {self.location.name} is my favourite spot on the Citadel.'

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
   inventory = []
   def __init__(self, name, location):
      self.name = name
      self.location = location

   def __str__(self):
      return f'I\'m {self.name}, and the {self.location.name} is my favourite spot on the Citadel.'
   
   def chk_inv(self):
      if len(self.inventory) > 0:
         print('Your inventory:')
         for count, val in enumerate(self.inventory):
            print(val)
      else:
         print('You have no items.')


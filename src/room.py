# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
   n_to = None
   e_to = None
   s_to = None
   w_to = None
   # items2 = []
   def __init__(self, name, description):
      self.name = name
      self.description = description
      self.items = []

   def print_items(self):
      if self.items is not None:
         string = ''
         for thing in self.items:
            string += f'{thing}\n'
         return string
      else:
         return '   None.'

   def __str__(self):
      return f'{self.name}.\n{self.description}. \nN: {self.n_to.name if self.n_to else None}\nE: {self.e_to.name if self.e_to else None}\nS: {self.s_to.name if self.s_to else None}\nW: {self.w_to.name if self.w_to else None}\nItems:\n{self.print_items()}' 
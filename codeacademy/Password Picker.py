import random
import string

noun = ['actor', 'account', 'achieve', 'acoustic', 'action', 'butter']

colour = ['red', 'yellow', 'blue', 'orange', 'black', 'purple', 'green', 'pink',
          'white', 'brown', 'grey']

things = ['car', 'box', 'glass', 'chocolate', 'hairbrush', 'sandwich',
         'shoe', 'fork', 'camera']

print("Welcome to the password picker! \n")

noun = random.choice(noun)
things = random.choice(things)
colour = random.choice(colour)
special_char = random.choice(string.punctuation)

password = noun.capitalize() + colour.capitalize() + things.capitalize() + special_char
print('Your new password is: %s' % password)

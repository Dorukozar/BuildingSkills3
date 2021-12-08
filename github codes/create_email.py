# Doruk Ozar

import random 

def make_email(name):
  name = name.split()
  random_ = random.randint(0, 99)
  email = (name[0][0].lower()+(name[1][0]).lower()+(name[2][0].lower())+str(random_))
  return email
  pass

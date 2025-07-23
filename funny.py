import random 
#smallchanges
#did_a_funy
def number_generator(int a, int b) -> int: 
  return (a*random.randint(a,b)*b - random.randint(a,b)*a*a*b*b)

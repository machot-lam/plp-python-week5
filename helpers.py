import math

def tables_needed(people, seat):
    return math.ceil (people / seat)
def welcome(name):
      return f"Welcome to PLP, {name}!"
if __name__ == "__main__":
    print(tables_needed(10, 4))

import math

def tables_needed(people, seat):
    return math. ceil (people / seat)
def welcome(name):
    return f"welcome to PLP, {name}!"
if __name__ == "__main__":
    print(tables_needed(10, 4))

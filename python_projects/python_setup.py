def hello():
   print("Hello user!")

def pack(first, second, third):
   return {first, second, third}
   

def eat_lunch(list_input):
   for thing in list_input:
      print(f"I would like to eat {thing}")

hello()
eat_lunch(pack("Chicken", "Salmon", "Whey"))
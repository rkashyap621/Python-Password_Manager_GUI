import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
  password_list = []

  password_list += [random.choice(letters) for _ in range(random.randint(4, 6))]

  password_list += [random.choice(letters).upper() for _ in range(random.randint(4, 6))]

  password_list += [random.choice(symbols) for _ in range(random.randint(4, 6))]

  password_list += [random.choice(numbers) for _ in range(random.randint(4, 6))]

  random.shuffle(password_list)

  password = "".join(password_list)

  return password

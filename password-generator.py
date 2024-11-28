import random, string
length = int(input("Enter password length (min 8): "))
if length < 8:
  print("Minimum password length is 8")
else:
  print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length)))

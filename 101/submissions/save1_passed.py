MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
  if age < MIN_DRIVING_AGE:
      print(name, 'is not allowed to drive')
  else:
      print(name, 'is allowed to drive')
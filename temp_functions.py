"""I put the functions I have created so far in one file"""
def fahr_to_celsius(temp_fahrenheit):
  """Substituting Fahrenheit for temp_fahrenheit changes to Celsius and returns that value"""
  converted_temp=( temp_fahrenheit - 32 ) / 1.8
  return converted_temp
  
def temp_classifier(temp_celsius):
  """Substituting the Celsius you want to classify into temp_celsius and devide the temperature into some of the four classes"""
  if temp_celsius<-2:
    return 0
  elif temp_celsius>=-2 and temp_celsius<2:
    return 1
  elif temp_celsius>=2 and temp_celsius<15:
    return 2
  elif temp_celsius>=15:
    return 3

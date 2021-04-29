"""Create a new script file containing the function fahr_to_celsius and temp_classifier."""

def fahr_to_celsius(temp_fahrenheit):
  """Convert from Fahrenheit to Celsius"""
  converted_temp =(temp_fahrenheit-32)/1.8
  return converted_temp 

def temp_classifier(temp_celsius):
  """Create a "temp_classifier" that classifies the temperature and return the classification number."""
  if temp_celsius<-2:
    number=0
  elif -2<=temp_celsius<2:
    number=1
  elif 2<=temp_celsius<15:
    number=2
  else:
    number=3
  return number
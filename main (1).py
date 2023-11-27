def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return True
    

year = int(input("Enter a year: "))
if isleapyear(year):
  print('{} is a leapyeat.'.format(year))
else:
  print('{} is not a leapyeat.'.format(year))

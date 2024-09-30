print('Welcome! This program will help you choose the cheapest way to ship your packages.')
weight = float(input('How much lb does your package weight?  '))

#ground shipping
if weight <= 2:
  price_pound = 1.50
  total = (price_pound*weight) + 20
  print('The cost for Ground Shipping is: $' + str(total))
elif weight > 2 and weight <= 6:
  price_pound = 3
  total = (price_pound*weight) + 20
  print('The cost for Ground Shipping is: $' + str(total))
elif weight > 6 and weight <= 10:
  price_pound = 4
  total = (price_pound*weight) + 20
  print('The cost for Ground Shipping is: $' + str(total))
elif weight > 10:
  price_pound = 4.75
  total = (price_pound*weight) + 20
  print('The cost for Ground Shipping is: $' + str(total))
else:
  print('Invalid.')

#Ground Shipping Premium
total_premium = 125
print('The cost for Ground Shipping Premium is: $' + str(total_premium))

#Drone Shipping
if weight <= 2:
  price_pound = 4.50
  total = price_pound * weight
  print('The cost for Drone Shipping is: $' + str(total))
elif weight > 2 and weight <= 6:
  price_pound = 9
  total = price_pound * weight
  print('The cost for Drone Shipping is: $' + str(total))
elif weight > 6 and weight <= 10:
  price_pound = 12
  total = price_pound * weight
  print('The cost for Drone Shipping is: $' + str(total))
elif weight > 10:
  price_pound = 14.25
  total = price_pound * weight
  print('The cost for Drone Shipping is: $' + str(total))
else:
  print('Please write a valid number.')
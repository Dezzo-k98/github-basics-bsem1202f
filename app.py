weight = input ('enter your weight: ')
print (f'is this in {pounds} or{kilograms}')
answer = input ('--')
pounds = int (weight) / 0.454
kilograms = 2.205 * int (weight)
if pounds:
 print (f"{pounds} kg")
else:
    print (f"{kilograms} lbs")
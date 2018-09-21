#Nick 

#This program will calculate the number of seconds a user has studied for a test.

print('This program will calcute your studied hours into seconds. Please enter \n your hours studied below.')

hours_studied = float(input('Please enter how many hours you have studied for the test:'))
seconds_studied = hours_studied * 60 * 60
minutes_studied = hours_studied * 60


print('The number of minutes you studied for the test is:', minutes_studied)
print('\n The number of seconds you studied for the test is:', seconds_studied)

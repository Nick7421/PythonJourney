#Nick Neiert ng7034mm
#This program will calculate the wage and overtime.

HourlyWage= 15
OverTimeHours = 10
OverTime= int((HourlyWage * 2) * OverTimeHours)
WeeklyWage = HourlyWage * 40 + OverTime


print('The weekly wage for the employee who worked 40 hours and 10 hours overtime is:')
print(WeeklyWage)

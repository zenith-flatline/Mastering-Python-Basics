from datetime import datetime

year = input("type your birth year: ")
month = input("type your birth month: ")
day = input("type the day: ")

age = datetime.now() - datetime(int(year),int(month),int(day))

age_in_day = age.days
age_in_year = age_in_day/364
print("you are about %s years old" %int(age_in_year))
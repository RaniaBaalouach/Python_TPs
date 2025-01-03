def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))
print(f"Is {year} a leap year? {is_leap_year(year)}")

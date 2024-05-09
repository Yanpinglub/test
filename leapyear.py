def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

for year in range(1950, 2025):
    if is_leap_year(year):
        print(year)
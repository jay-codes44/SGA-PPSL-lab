def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND
    - If divisible by 100, it must also be divisible by 400
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Get input from user
year = int(input("Enter a year: "))

# Check and display result
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Test cases
print("\n--- Test Cases ---")
test_years = [2000, 2004, 2100, 2020, 2021, 1900, 2024]
for y in test_years:
    print(f"{y}: {is_leap_year(y)}")

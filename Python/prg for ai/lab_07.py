print("CALENDAR VERIFICATION SYSTEM")

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Please enter a positive year.")

else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
        days_in_year = 366
        days_in_february = 29

    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
        days_in_year = 365
        days_in_february = 28

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
        days_in_year = 366
        days_in_february = 29

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"
        days_in_year = 365
        days_in_february = 28

    print("\nYear:", year)
    print("Status:", status)
    print("Days in Year:", days_in_year, "days")
    print("Days in February:", days_in_february, "days")
    print("Reason:", reason)
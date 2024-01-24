import calendar

def get_number_of_days(year, month):
    # Check if the month and year are valid
    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")
    
    # Use calendar.monthrange() to get the number of days in the month
    _, num_days = calendar.monthrange(year, month)
    
    return num_days
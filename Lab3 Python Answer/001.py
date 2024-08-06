#1. Write a function called check-season, it takes a month parameter and returns the season:  Autumn, Winter, Spring or Summer.

def check_season(month):
    # Define the seasons and the corresponding months
    seasons = {
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November']
    }
    
    # Check which season the month belongs to and return it
    for season, months in seasons.items():
        if month.capitalize() in months:
            return season
    
    # If the month is not found, return an error message
    return "Invalid month"

# Example usage with user input
month = input("Enter the name of a month: ")
season = check_season(month)
print(f"The season for {month} is {season}.")

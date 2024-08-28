# Dictionary to map month number to season
seasons = {
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
}

# Function to get season name based on month number
def get_season(month):
    return seasons.get(month, "Invalid month")

# Example usage
month_number = 3  # Replace with any month number
season_name = get_season(month_number)
print("Season:", season_name)

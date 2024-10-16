# 11-1: City, Country

def get_full_location(city, country, population=''):
    """Create a formatted string of the city and country"""
    if population:
        full_location = f"{city.title()}, {country.title()} - population={population}"
    else:
        full_location = f"{city.title()}, {country.title()}"
    
    return full_location
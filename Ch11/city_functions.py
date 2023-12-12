#!/usr/bin/python3

def f_city_function(city, country, population=''):
    """Generate a neatly formatted string: City, Country - population value"""
    formatted = f"{city}, {country}".title()
    if population:
        return f"{formatted} - population {population}"
    else:
        return formatted

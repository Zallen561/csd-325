def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

# Final required function calls for screenshot
print(city_country("Santiago", "Chile"))
print(city_country("Dallas", "USA", 1300000))
print(city_country("Tokyo", "Japan", 10000000, "Japanese"))

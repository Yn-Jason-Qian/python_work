def format_city(city, country, population=0):
    """ 格式化城市 """
    if population == 0:
        result = city + ', ' + country
    else:
        result = city + ', ' + country + ', population = ' + str(population)
    return result.title()

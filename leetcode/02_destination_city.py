def destCity(paths):
    """
    O(n) Time
    O(n) Space
    """
    cities_count = {}

    for path in paths:
        city_a, city_b = path
        cities_count[city_a] = cities_count.get(city_a, 0) + 1
        cities_count[city_b] = cities_count.get(city_b, 0)

    for city in cities_count:
        if cities_count[city] == 0:
            return city

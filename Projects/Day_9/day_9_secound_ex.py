travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(param, param1, param2):
    add_new = {}

    add_new["country"] = param
    add_new["visits"] = param1
    add_new["cities"] = param2

    travel_log.append(add_new)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



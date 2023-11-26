spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = []
    for dic in spicy_foods:
        for item in dic:
            if item == "name":
                name_list.append(dic[item])
            else:
                pass
    return name_list
        

def get_spiciest_foods(spicy_foods):
    spicy_list = []
    for dic in spicy_foods:
        if dic["heat_level"] >= 6:
            spicy_list.append(dic)
        else:
            pass
    return spicy_list

def print_spicy_foods(spicy_foods):
    for dic in spicy_foods:
        name = dic["name"]
        cuisine = dic["cuisine"]
        heat = ("🌶" * dic["heat_level"])

        print(f'{name} ({cuisine}) | Heat Level: {heat}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dic in spicy_foods:
        if dic["cuisine"] == cuisine:
            return dic
        else:
            pass

def print_spiciest_foods(spicy_foods):
    for dic in spicy_foods:
        name = dic["name"]
        cuisine = dic["cuisine"]
        heat = ("🌶" * dic["heat_level"])
        if dic["heat_level"] > 5:
            print(f'{name} ({cuisine}) | Heat Level: {heat}')
        else:
            pass

def get_average_heat_level(spicy_foods):
    counter = 0
    heat = 0
    for dic in spicy_foods:
        heat=heat + dic["heat_level"]
        counter=counter+1
    return (heat/counter)
    

def create_spicy_food(spicy_foods, spicy_food):
    list = []
    for dic in spicy_foods:
        list.append(dic)
    list.append(spicy_food)
    return list

# Сравнивает доступные продукты с рецептом, выводит кол-во тортиков
def cakes(recipe: dict, available: dict) -> int:
    s = 0
    try:
        i = 100000000
        for k, v in recipe.items():
            r = available[k]//recipe[k]
            if r <= i:
                i = r
        s = i
    except KeyError:
        s = 0
    return s

def cakes_r(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

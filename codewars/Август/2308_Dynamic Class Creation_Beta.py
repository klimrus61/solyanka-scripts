def create_class(name, inheritance=tuple(), methods={}):
    # type не только проверяет тип обьекта, но и создает новый объект (Класс)
    return type(name, inheritance, methods if not methods else {f.__name__: f for f in methods})
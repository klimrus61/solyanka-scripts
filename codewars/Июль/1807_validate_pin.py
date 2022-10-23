# Проверяет состоит ли строка только из 4 или 6 чисел
def validate_pin(pin):
    return len(pin) == 4 or len(pin) == 6 if pin.isdigit() else False

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

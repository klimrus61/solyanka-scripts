def race(v1, v2, g):
    """v1 and v2 скорости черепах, через какое время 2 черепаха догонит 1"""
    if v1 >= v2: return None
    # Скорость сближения
    v = v2 - v1
    t = g / v # Время в часах
    seconds = int(t * 60 * 60 % 60)
    minutes = int(t * 60 % 60)
    hours = int(t % 24)
    return [hours, minutes, seconds]

# Чужое решение
from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g*3600/(v2-v1))))
        d = datetime(1,1,1) + sec

        return [d.hour, d.minute, d.second]

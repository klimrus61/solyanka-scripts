def make_readable(seconds):
    if seconds >= 0 and seconds <=359999:
        sec = seconds % 60
        mins = seconds // 60 % 60
        hours = seconds // 60 // 60
        return "%02i:%02i:%02i" % (hours, mins, sec)

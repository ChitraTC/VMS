class Time:
    def __init__(self , hour , min , sec):
        self.hour = hour
        self.min = min
        self.sec = sec

def is_after(t1 , t2):
    if t1.hour > t2.hour:
        return True
    elif t1.hour == t2.hour:
        if t1.min > t2.min:
            return True
        elif t1.min == t2.min:
            if t1.sec > t2.sec:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
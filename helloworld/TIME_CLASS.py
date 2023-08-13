class Time:
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def is_after(t1, t2):
        return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second

        if sum.second >= 60:
            sum.second -= 60
            sum.minute += 1

        if sum.minute >= 60:
            sum.minute -= 60
            sum.hour += 1
        return sum

    def print_time(done):
	    print("the time is %.2d : %.2d : %.2d" %(done.hour,done.minute,done.second))

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

Time.print_time(start)
start.print_time()
class Time:
    def print_time(done):
        print("the time is %.2d : %.2d : %.2d" % (done.hour, done.minute, done.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

Time.print_time(start)
start.print_time()
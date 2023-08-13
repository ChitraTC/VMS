from __future__ import print_function, division
class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(done):
        print("the time is %.2d : %.2d : %.2d" % (done.hour, done.minute, done.second))



    def int_to_time(seconds):
        """Makes a new Time object.
        seconds: int seconds since midnight.
        """
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time


    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def intt_to_time(self,seconds):
        #self = Time()
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)
        return self

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


start = Time(9, 45)
start.print_time()
end=start.increment(1337)
end.print_time()


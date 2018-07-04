class TimeGen:
    times = []

    def init_times(self):
        for i in range(24):
            j = 0
            for k in range(60 // 5):
                if i == 0:
                    hour = 12
                else:
                    hour = i if (i < 13) else (i - 12)
                minute = '%02d' % j
                if i < 12:
                    time = (str(hour) + ':' + str(minute)) + ' am'
                else:
                    time = (str(hour) + ':' + str(minute)) + ' pm'
                self.times.append(time)
                j += 5

    def print_times(self):
        for time in self.times:
            print(time)


time_gen = TimeGen()
time_gen.init_times()
time_gen.print_times()

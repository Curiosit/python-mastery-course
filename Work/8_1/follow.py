def frange(start,stop,step):
        while start < stop:
            yield start
            start += step


for x in frange(0, 2, 0.25):
        print(x, end=' ')

# 0 0.25 0.5 0.75 1.0 1.25 1.5 1.75



class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
        def __iter__(self):
            n = self.start
            while n < self.stop:
                yield n
                n += self.step
class Counter:
    def __init__(self, initial = 0, step = 1):
        self._count = initial
        self._step = step

    def increment(self):
        self._count += self._step

    @property
    def total(self):
        return self._count
    
    @property
    def step(self):
        return self._step
    
class TwowayCounter(Counter):
     def decrement(self):
         self._count -= self._step

class LimitedCounter(Counter):
    def __init__(self, max, initial = 0, step = 1):
        super().__init__(initial, step)
        self._max = max

    def increment(self):
        if self.count + self.step <= self._max:
            super().increment()

    @property
    def max(self):
        return self._max
    
class LimitedTwowayCounter(LimitedCounter, TwowayCounter):
    def __init__(self, min, max, initial = 0, step = 1):
        super().__init__(max, initial, step)
        self._min = min

    def decrement(self):
        if self.count - self.step >= self._min:
            super().decrement()

    @property
    def min(self):
        return self._min
    
class Semaphore(LimitedTwowayCounter):
    def __init__(self, is_available = False):
        super().__init__(0, 1, int(is_available))

    def is_available(self):
        return self._count > 0
    
    def wait(self):
        self.decrement()

    def signal(self):
        self.increment()
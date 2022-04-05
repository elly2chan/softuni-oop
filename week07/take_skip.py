class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        while self.count > 0:
            current = self.start
            self.count -= 1
            return current
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)

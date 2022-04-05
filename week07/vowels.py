class vowels:
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.end = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            current_char = self.data[self.start]
            self.start += 1
            if current_char in 'AEOUYIaeouyi':
                return current_char
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
class dictionary_iter:
    def __init__(self, data):
        self.data = dict(data)
        self.i = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        while self.i > 0:
           for key, value in self.data.items():
               current = key, value
               self.data.pop(key)
               self.i -= 1
               return current
        else:
            raise StopIteration()


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        if len(value) > 0:
            self.__topping_type = value
            return
        raise ValueError('The topping type cannot be an empty string')
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
            return
        raise ValueError('The weight cannot be less or equal to zero')

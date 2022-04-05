from animal import Animal
from worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if self.__budget < price:
            return 'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return 'Not enough space for animal'
        self.__budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_care_money = 0
        for animal in self.animals:
            total_care_money += animal.money_for_care

        if self.__budget >= total_care_money:
            self.__budget -= total_care_money
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        result += self.__build_animal_str('Lion')
        result += self.__build_animal_str('Tiger')
        result += self.__build_animal_str('Cheetah')
        return result.rstrip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__build_worker_str('Keeper')
        result += self.__build_worker_str('Caretaker')
        result += self.__build_worker_str('Vet')
        return result.rstrip()

    def __build_animal_str(self, animal_type):
        counter = 0
        result = ''
        for animal in self.animals:
            if animal.__class__.__name__ == animal_type:
                counter += 1
                result += repr(animal) + '\n'
        return f'----- {counter} {animal_type}s:\n' + result

    def __build_worker_str(self, worker_type):
        counter = 0
        result = ''
        for worker in self.workers:
            if worker.__class__.__name__ == worker_type:
                counter += 1
                result += repr(worker) + '\n'
        return f'----- {counter} {worker_type}s:\n' + result
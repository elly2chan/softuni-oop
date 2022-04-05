from unittest import TestCase, main

from car_manager import Car


class CarManagerTests(TestCase):
    def setUp(self) -> None:
        self.car = Car('Peugeot', '206', 10, 100)

    def test_car_constructor(self):
        make = 'Peugeot'
        model = '206'
        fuel_consumption = 10
        fuel_capacity = 100
        car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual(car.make, make)
        self.assertEqual(car.model, model)
        self.assertEqual(car.fuel_consumption, fuel_consumption)
        self.assertEqual(car.fuel_capacity, fuel_capacity)
        self.assertEqual(car.fuel_amount, 0)

    def test_make_is_empty_str_raises(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_model_is_empty_str_raises(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_fuel_consumption_is_zero_or_negative_raises(self):
        for fuel_consumption in [0, -50]:

            with self.assertRaises(Exception) as context:
                self.car.fuel_consumption = fuel_consumption
            self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_fuel_capacity_is_zero_or_negative_raises(self):
        for fuel_capacity in [0, -50]:

            with self.assertRaises(Exception) as context:
                self.car.fuel_capacity = fuel_capacity
            self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_fuel_amount_is_negative_raises(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(context.exception))

    def test_refuel_when_fuel_for_refill_is_zero_or_negative_raises(self):
        for fuel in [0, -50]:
            with self.assertRaises(Exception) as context:
                self.car.refuel(fuel)
            self.assertEqual('Fuel amount cannot be zero or negative!', str(context.exception))

    def test_refuel_when_fuel_is_correct_amount_and_refill_plus_amount_is_less_than_capacity(self):
        self.car.refuel(90)
        self.assertEqual(self.car.fuel_amount, 90)

    def test_refuel_when_fuel_is_correct_amount_and_refill_plus_amount_is_more_than_capacity(self):
        self.car.refuel(120)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_when_destination_is_not_reachable(self):
        distance = 1000
        with self.assertRaises(Exception) as context:
            self.car.drive(distance)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_drive_when_destination_is_reachable(self):
        distance = 10
        self.car.refuel(10)
        self.car.drive(distance)
        self.assertEqual(self.car.fuel_amount, 9)



if __name__ == '__main__':
    main()
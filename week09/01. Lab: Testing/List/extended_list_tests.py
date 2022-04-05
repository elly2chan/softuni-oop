from unittest import TestCase, main

from week09.List.extended_list import IntegerList


class IntegerListTests(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data_type(self):
        integer = IntegerList("asd", 1.5, 2.2, 1)
        self.assertEqual([1], integer._IntegerList__data)

    def test_is_initialized_correctly_with_integers(self):
        integer = IntegerList("asd", 1, 2)
        self.assertEqual([1, 2], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5, 'asd')
        self.assertEqual([5], integer._IntegerList__data)
        result = integer.get_data()
        self.assertEqual([5], result)

    def test_add_method_incorrect_data_raises(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            integer.add('5')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_method_adds_correct_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        integer.add(3)
        self.assertEqual([5, 3], integer._IntegerList__data)

    def test_remove_method_correct_index(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_remove_method_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_method_returns_element_after_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5, result)

    def get_with_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual('Index is out of range', str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_valid_index_returns_element(self):
        integer = IntegerList(5)
        result = integer.get(0)
        self.assertEqual(5, result)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(1, 3)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_invalid_data_type_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, '3')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert_adds_element(self):
        integer = IntegerList(5)
        integer.insert(0, 10)
        self.assertEqual([10, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, 2, 100, 101, 3, -6, -100)
        result = integer.get_biggest()
        self.assertEqual(101, result)

    def test_get_index(self):
        integer = IntegerList(5, 3, 10, 16, -6, -20, 300)
        result = integer.get_index(3)
        self.assertEqual(1, result)


if __name__ == '__main__':
    main()
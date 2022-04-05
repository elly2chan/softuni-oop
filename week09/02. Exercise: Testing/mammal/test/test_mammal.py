from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def test_animal_init(self):
        name = 'Test'
        mammal_type = 'TestType'
        sound = 'Boo'
        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(mammal.name, name)
        self.assertEqual(mammal.type, mammal_type)
        self.assertEqual(mammal.sound, sound)
        self.assertEqual(mammal._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        mammal = Mammal('Test', 'TestType', 'Boo')
        self.assertEqual(mammal.make_sound(), 'Test makes Boo')

    def test_get_kingdom(self):
        mammal = Mammal('Test', 'TestType', 'Boo')
        self.assertEqual(mammal.get_kingdom(), 'animals')

    def test_getting_info(self):
        mammal = Mammal('Test', 'TestType', 'Boo')
        self.assertEqual(mammal.info(), 'Test is of type TestType')


if __name__ == '__main__':
    main()
from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Batman', 10, 100, 50)
        self.enemy = Hero('Pacman', 10, 100, 50)

    def test_hero_init(self):
        username = 'Batman'
        level = 99
        health = 100
        damage = 1000

        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_battle_when_username_is_same_as_ours_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_when_health_is_zero_or_less_raises(self):
        for health in [0, -50]:
            self.hero.health = health

            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_when_enemy_health_is_zero_or_less_raise(self):
        for health in [0, -50]:
            self.enemy.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f'You cannot fight {self.enemy.username}. He needs to rest', str(ex.exception))

    def test_battle_returns_draw_when_both_heroes_die(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual('Draw', result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_returns_win_when_player_wins(self):
        enemy = Hero('Defender', 1, 100, 50)
        result = self.hero.battle(enemy)
        self.assertEqual('You win', result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(55, self.hero.health)

    def test_battle_returns_lose_when_player_looses(self):
        hero = Hero('Warrior', 1, 100, 50)
        enemy = Hero('Defender', 1, 100, 50)
        result = hero.battle(enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(55, enemy.damage)

    def test_hero_str(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, str(self.hero))
        

if __name__ == '__main__':
    main()

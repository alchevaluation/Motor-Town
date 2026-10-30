import unittest
from motortown.demo import make_player
from motortown.game import Game, Phase


class GameTests(unittest.TestCase):
    def make_game(self):
        return Game((make_player('Alex', 'a'), make_player('Blair', 'b')))

    def test_opening_hands(self):
        game = self.make_game()
        game.start(seed=12)
        self.assertEqual([len(p.hand) for p in game.players], [3, 3])
        self.assertEqual(game.phase, Phase.MAIN)

    def test_end_turn_draws_for_next_player(self):
        game = self.make_game()
        game.start()
        game.end_turn()
        self.assertEqual(game.current_player.name, 'Blair')
        self.assertEqual(game.turn_number, 2)
        self.assertEqual(len(game.current_player.hand), 4)

    def test_play_card_moves_zone(self):
        game = self.make_game()
        game.start()
        player = game.current_player
        chosen = player.hand[0]
        player.move_from_hand_to_play(chosen.card_id)
        self.assertEqual(len(player.hand), 2)
        self.assertIn(chosen, player.play)

    def test_missing_card_raises(self):
        game = self.make_game()
        game.start()
        with self.assertRaises(ValueError):
            game.current_player.move_from_hand_to_play('missing')

    def test_empty_deck_raises(self):
        game = self.make_game()
        game.start()
        game.current_player.deck.clear()
        with self.assertRaises(ValueError):
            game.current_player.draw()


if __name__ == '__main__':
    unittest.main()

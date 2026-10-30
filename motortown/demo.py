"""Run: python -m motortown.demo"""
from .game import Card, Car, Driver, Game, Player


def make_player(name: str, prefix: str) -> Player:
    cards = [Card(f'{prefix}-{i}', f'Prototype Card {i}', 'action') for i in range(1, 11)]
    return Player(name, Car(f'{name} Car', 8, 7), Driver(f'{name} Driver', 9, 6), cards)


def main() -> None:
    game = Game((make_player('Alex', 'a'), make_player('Blair', 'b')))
    game.start(seed=42)
    print('Motor Town TCG - prototype')
    for player in game.players:
        print(f'{player.name}: {len(player.hand)} cards in hand, {len(player.deck)} in deck')
    print(f'Turn {game.turn_number}: {game.current_player.name} ({game.phase.value})')
    game.end_turn()
    print(f'Turn {game.turn_number}: {game.current_player.name} ({game.phase.value})')


if __name__ == '__main__':
    main()

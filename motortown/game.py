"""Core turn and zone tracking. Resource and racing rules are intentionally not implemented."""
from dataclasses import dataclass, field
from enum import Enum
import random


class Zone(str, Enum):
    DECK = 'deck'
    HAND = 'hand'
    PLAY = 'play'
    DISCARD = 'discard'


class Phase(str, Enum):
    DRAW = 'draw'
    MAIN = 'main'
    END = 'end'


@dataclass(frozen=True)
class Card:
    card_id: str
    name: str
    kind: str


@dataclass
class Car:
    name: str
    reliability: int
    precision: int


@dataclass
class Driver:
    name: str
    endurance: int
    concentration: int


@dataclass
class Player:
    name: str
    car: Car
    driver: Driver
    deck: list[Card]
    hand: list[Card] = field(default_factory=list)
    play: list[Card] = field(default_factory=list)
    discard: list[Card] = field(default_factory=list)

    def draw(self) -> Card:
        if not self.deck:
            raise ValueError(f'{self.name} cannot draw from an empty deck')
        card = self.deck.pop()
        self.hand.append(card)
        return card

    def move_from_hand_to_play(self, card_id: str) -> Card:
        """Prototype zone movement; card costs and permissions are out of scope."""
        for index, card in enumerate(self.hand):
            if card.card_id == card_id:
                self.play.append(self.hand.pop(index))
                return card
        raise ValueError(f'Card {card_id!r} is not in {self.name} hand')


@dataclass
class Game:
    players: tuple[Player, Player]
    current_player_index: int = 0
    turn_number: int = 1
    phase: Phase = Phase.DRAW

    def __post_init__(self) -> None:
        if len(self.players) != 2:
            raise ValueError('Prototype requires exactly two players')

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    def start(self, seed: int = 0, opening_hand_size: int = 3) -> None:
        rng = random.Random(seed)
        for player in self.players:
            if len(player.deck) < opening_hand_size:
                raise ValueError('Not enough cards to deal the opening hand')
        for player in self.players:
            rng.shuffle(player.deck)
            for _ in range(opening_hand_size):
                player.draw()
        self.phase = Phase.MAIN

    def end_turn(self) -> None:
        self.phase = Phase.END
        self.current_player_index = 1 - self.current_player_index
        self.turn_number += 1
        self.phase = Phase.DRAW
        self.current_player.draw()
        self.phase = Phase.MAIN

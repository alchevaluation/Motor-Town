# Motor Town TCG - Prototype

A minimal Python prototype for a two-player automotive card game.

## What works
- Cards with identifiers and types
- Cars and drivers with attributes
- Deck, hand, play and discard zones
- Seeded shuffle and opening hands
- Alternating turns and drawing on the next player's turn
- Standard-library unit tests

## Not implemented yet
- Resource and card-cost rules
- Racing or overtaking mechanics
- Wear, repairs, pits, and multiplayer
- Gameplay UI

## Run
```sh
python -m motortown.demo
python -m unittest discover -s tests -v
```

Python 3.11+; no third-party dependencies.

This is a prototype, not a finished game or an Alignerr task submission.

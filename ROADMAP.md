# Motor Town TCG — Roadmap

Status: early Python prototype. Updated: 2026-10-30.

## Goal

Build a playable, local two-player motorsport strategy card game. Players
manage fuel, vehicle condition, driver performance, and tactical cards to
complete a 300 km race in the fewest turns possible.

This roadmap describes planned development. Estimates are approximate hands-on
development time, include implementation and validation, and are not hours
already worked or fixed delivery commitments.

## Current baseline

The repository currently contains:

- Card, car, driver, player, and game-state models.
- Deck, hand, play, and discard zones.
- Seeded shuffling and an opening hand of three cards.
- Alternating turns, card draws, and basic hand-to-play movement.
- A command-line demonstration and five unit tests.

Fuel, racing, pit stops, card costs, wear, recovery, and a gameplay interface
are not implemented. Existing card movement does not yet validate resource
costs or action legality.

## Working design

The following rules guide the next prototype and remain subject to playtesting:

- Initial fuel cards in play plus cards in hand total seven.
- Each fuel card has three consumable states: full, half, and reserve.
  Consuming reserve discards that fuel card.
- Vehicle weight depends on the number of fuel cards in play, regardless of
  their remaining fuel.
- A player draws one card per turn and may play at most one new fuel card
  per turn.
- A strategic pit stop discards the hand and draws seven replacement cards.
- A refueling pit stop returns all fuel cards in play to full and preserves
  the hand.
- The two pit-stop choices are mutually exclusive. Each consumes the whole
  turn and produces no distance.
- Race distance is 300 km. Fuel-to-distance conversion, weight penalties,
  action timing, and tie-breaking still need explicit rules.

## Milestones

All milestones below are planned and incomplete.

| Order | Milestone | Estimated effort | Depends on |
| --- | --- | --- | --- |
| 1 | Rules and game-state lifecycle | 4–6 hours | Current baseline |
| 2 | Fuel, preparation, and weight | 6–9 hours | 1 |
| 3 | Distance and race resolution | 5–8 hours | 2 |
| 4 | Pit stops | 4–6 hours | 3 |
| 5 | Tactical cards, car, and driver effects | 6–10 hours | 4 |
| 6 | Playable command-line match | 5–8 hours | 5 |
| 7 | Simulations, balance, and documentation | 6–10 hours | 6 |
| **Total** | **Planned development** | **36–57 hours** | |

### 1. Rules and game-state lifecycle

- [ ] Document setup, turn phases, legal actions, and the end of a match.
- [ ] Define the timing of draws, fuel placement, racing actions, and pit stops.
- [ ] Decide deck-exhaustion behavior and limits on actions per turn.
- [ ] Reject invalid actions before changing game state.
- [ ] Add tests for phase transitions, invalid actions, and card conservation.

**Done when:** every legal turn transition is defined and tested; a rejected
action leaves the state unchanged; cards cannot be lost or duplicated by
zone movement.

### 2. Fuel, preparation, and weight

- [ ] Replace the fixed three-card opening with the seven-slot preparation rule.
- [ ] Validate starting fuel choices against the available deck and setup rules.
- [ ] Implement full → half → reserve → discard consumption.
- [ ] Let players choose which fuel cards to consume when multiple are available.
- [ ] Enforce at most one new fuel card per turn.
- [ ] Calculate weight from the number of fuel cards in play.
- [ ] Define configurable weight bands and their distance modifiers.
- [ ] Test every fuel transition, setup boundary, and weight-band boundary.

**Done when:** setup always totals seven slots, fuel cannot be spent twice,
discarding an empty tank updates weight immediately, and fuel placement
limits reset only at the correct turn boundary.

### 3. Distance and race resolution

- [ ] Define the base conversion from consumed fuel to distance.
- [ ] Apply weight and relevant action modifiers in a documented order.
- [ ] Track each player's distance and completed turns.
- [ ] Specify race completion and tie-breaking, including equal-turn finishes.
- [ ] Prevent actions after the match has ended.
- [ ] Test distance calculations and finishes at, below, and above 300 km.

**Done when:** a deterministic match can reach a documented result, distance
calculations are reproducible, and both players receive the opportunities
required by the chosen finishing rule.

### 4. Pit stops

- [ ] Implement the strategic stop: discard the hand and draw seven cards.
- [ ] Implement refueling: restore existing fuel cards without changing the hand.
- [ ] Enforce mutual exclusivity and consumption of the entire turn.
- [ ] Specify how the normal turn draw interacts with each pit-stop choice.
- [ ] Apply the deck-exhaustion rule consistently during strategic stops.
- [ ] Test empty hands, insufficient decks, partial tanks, and repeated pit stops.

**Done when:** each stop has exactly its documented effects, no racing distance
is gained, and refueling changes neither tank count nor vehicle weight.

### 5. Tactical cards, car, and driver effects

- [ ] Define a small initial card set with explicit costs, timing, and effects.
- [ ] Validate affordability and targeting before resolving a card.
- [ ] Give the existing car and driver attributes documented gameplay effects.
- [ ] Introduce a minimal wear and recovery system.
- [ ] Test interacting effects, insufficient resources, and attribute limits.

**Done when:** a complete initial deck supports meaningful choices, every
implemented effect is documented, and illegal card plays cannot bypass
resource or timing rules.

### 6. Playable command-line match

- [ ] Add a local two-player gameplay loop alongside the existing demonstration.
- [ ] Display distance, fuel states, weight, hand, car, and driver condition.
- [ ] Offer legal choices for setup, racing, card play, and pit stops.
- [ ] Handle invalid input without losing or corrupting the match.
- [ ] Support a fixed seed for reproducible playtesting.
- [ ] Document commands and a short example match.

**Done when:** two people can complete a match from setup to result through
the terminal, following the documented instructions.

### 7. Simulations, balance, and documentation

- [ ] Add reproducible simulations with simple strategies for comparison.
- [ ] Compare light, balanced, and fuel-heavy starting configurations.
- [ ] Compare strategic and refueling pit-stop decisions.
- [ ] Track turns to finish, fuel use, pit stops, and stalled matches.
- [ ] Investigate whether preserving many tanks enables a dominant refueling loop.
- [ ] Tune provisional values using recorded results and human playtests.
- [ ] Add regression tests for defects discovered during playtesting.
- [ ] Update the README with implemented rules, limitations, and run instructions.

**Done when:** simulation results and known balance limitations are recorded,
a reproducible set of matches terminates under the chosen rules, and the
documentation matches the playable implementation.

## First playable release

The first playable release is complete when milestones 1–6 meet their
acceptance criteria, the documented test suite passes, and two local players
can finish a 300 km match. Milestone 7 then provides evidence for balance
changes rather than treating the initial numeric values as final.

## Later possibilities

These items are outside the effort estimate and will be prioritized after
the local game is playable:

- A graphical interface.
- More cards, cars, drivers, and track variants.
- Expanded overtaking and race-position mechanics.
- More than two players.
- Save/resume and network play.

## Tracking progress

Check an item only after its implementation and relevant validation are
complete. Record rule decisions and balance changes as they are made, and
revise estimates when playtesting changes the scope. Use synthetic players
and sample data throughout development.

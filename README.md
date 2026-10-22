# Mining and Alien Dueling Game

A space-themed game I built in Python for my business programming class (MIS 221) at the University of Alabama in Spring 2026. You start with 50 energy crystals and spend them on two mini-games. Get to 300 crystals and you win. Hit 0 and the alien eats you for breakfast.

## How It Works

Everything runs off one currency: energy crystals. Each mini-game costs crystals to play, so every round is a decision about how much risk you want to take.

### Asteroid Mining (10 crystals)

You head out to mine and pray you hit big. The outcome is random:

| Outcome | Chance |
|---|---|
| Earn 50 crystals | 40% |
| Nothing happens | 30% |
| Lose 25 crystals | 20% |
| Earn or lose 100 crystals | 5% |
| Lose everything | 5% |

I set these odds on purpose. Most of the time you either make steady progress or break even, and the big swings are rare. I wanted average luck to feel rewarding instead of punishing, while still keeping a little danger in every trip.

### Alien Duel (5 crystals)

A dice game against an alien, similar to blackjack. You bet any amount of crystals you have, then roll two 10-sided dice. After that you can keep rolling one die at a time or stop.

- Go over 21 and you bust and lose your bet
- The alien rolls until it reaches at least 17
- Highest score without busting wins
- If you tie at 21, that's a Plasma Blast and you win
- Any other tie goes to the alien

Win and you earn back what you bet on top of keeping your stake.

## Features

The assignment required a main menu, a resource system, and mini-games. I added a few more things because I wanted it to feel like a finished product, not just something that checks the boxes.

- **Tutorials:** Each game has an optional tutorial with unlimited crystals, so new players can learn the rules without losing anything
- **Save and load:** Save your crystal count and pick up where you left off
- **Autosave:** Can be turned on in settings to save every time you return to the menu
- **Settings menu:** Change the menu music, adjust the volume, or reset everything to default
- **Original music:** I produced the background tracks myself, with separate songs for the menu and each game
- **Input checks:** Every menu handles typos and invalid entries so the game never crashes or leaves you stuck

## How to Run

You'll need Python 3.10 or newer (the code uses match statements) and Pygame for the music.

Type the following into terminal
```
pip install pygame
python app.py
```
if this doesn't work try,

```
pip install --user pygame-ce
python app.py
```

Keep the `.mp3` files in the same folder as the code, or the music won't load.

## Project Structure

| File | What it does |
|---|---|
| `app.py` | Starts the game and runs the main menu loop |
| `utilities.py` | Shared functions: menu, save/load, music, screen helpers |
| `mining_game.py` | Asteroid Mining logic |
| `duel_game.py` | Alien Duel logic |
| `mining_tutorial.py` | Asteroid Mining tutorial |
| `duel_tutorial.py` | Alien Duel tutorial |
| `settings.py` | Settings menu (music, volume, autosave, reset) |

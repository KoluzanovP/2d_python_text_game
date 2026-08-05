# 2D Python Text Game

A text-and-graphics adventure game written in Python. The player explores a dungeon,
collects items, solves puzzles and tries to escape through the main entrance by defeating a
boss. Input is typed as text commands, and the room layout is drawn in a window with the
`graphics.py` library.

## Table of contents

- [Features](#features)
- [Interface](#interface)
- [Requirements](#requirements)
- [Installation and running](#installation-and-running)
- [How to play](#how-to-play)
- [Commands](#commands)
- [World map](#world-map)
- [Items and walkthrough logic](#items-and-walkthrough-logic)
- [Scoring](#scoring)
- [Project structure](#project-structure)
- [How it works internally](#how-it-works-internally)
- [Ideas for improvement](#ideas-for-improvement)

## Features

- 6 connected rooms, each with its own geometry and colour scheme, drawn with `graphics.py`
  primitives.
- A text command parser with input validation (`look`, `go`, `get`, `view inventory`).
- An inventory of 5 items that affects the available actions and the ending.
- Puzzles and conditions: locked doors, a safe that only opens with the right item, and a
  final boss fight.
- A score at the end of the game based on the items collected.
- A log of every player action written to `logs.txt`.
- Two endings, victory or death, depending on the gear you collected.

## Interface

The game window (1000 x 500) is split into two parts:

- Left panel: the command input field, a "Send command" button, a status line showing
  whether the command is valid, the current room description, and messages and inventory.
- Right panel: a schematic view of the current room with walls, doors (brown) and the hero
  (a red circle).

The game waits for a mouse click inside the window, then reads the text from the input
field and runs the command.

## Requirements

- Python 3.x
- The [`graphics.py`](https://mcsp.wartburg.edu/zelle/python/) library, John Zelle's
  graphics library, a wrapper around Tkinter
- Tkinter, which usually ships with Python. On Linux it may need to be installed
  separately.

## Installation and running

```bash
# 1. Clone the repository
git clone https://github.com/KoluzanovP/2d_python_text_game.git
cd 2d_python_text_game

# 2. Install the graphics library
#    Download graphics.py from https://mcsp.wartburg.edu/zelle/python/graphics.py
#    and place it next to main.py, or install via pip:
pip install graphics.py

# 3. (Linux) install Tkinter if needed
#    sudo apt-get install python3-tk

# 4. Run the game
python main.py
```

The file must be named `graphics.py` and be importable (`from graphics import *`).

## How to play

1. Run `main.py`. A window opens with the starting room, the Dungeon.
2. Type a command in the input field on the left.
3. Click the mouse anywhere in the window so the game reads and runs the command.
4. Watch the status line: the command is marked as valid or invalid.
5. Collect items, move between rooms and find your way to the main exit.

## Commands

| Command            | Action                                                          | Example           |
|--------------------|-----------------------------------------------------------------|-------------------|
| `look`             | Look around: shows items in the room and available doors        | `look`            |
| `go <direction>`   | Move to an adjacent room (`north`, `south`, `west`, `east`)     | `go west`         |
| `get <item>`       | Pick up an item (`map`, `key`, `garlic`, `paper`, `energy`)     | `get key`         |
| `view inventory`   | Show the contents of your inventory                             | `view inventory`  |

Input validation rules:

- A command cannot contain more than two words.
- A single word is only allowed for `look`.
- `go` accepts only the 4 compass directions, and `get` only accepts existing items.

## World map

```
              [ Main entrance ]   <- exit / finale
                     ^ north
                 [ Elevator ]
                     ^ (north when you have energy)
   [ Kitchen ] <-west [ The Great Hall ] east-> [ Dungeon ] (start)
                     v south
               [ Laboratory ]
```

- Dungeon: the starting room. The west door to the Great Hall is locked without the key.
- The Great Hall: the central hub with four doors.
- Kitchen / Laboratory / Elevator: rooms with items and connections.
- Main entrance: the final location, where the outcome depends on your inventory.

## Items and walkthrough logic

| Item      | Where to find | What it's for                                                    |
|-----------|---------------|------------------------------------------------------------------|
| `map`     | Dungeon       | Score (part of the inventory)                                    |
| `key`     | Dungeon       | Opens the locked west door into the Great Hall                   |
| `garlic`  | Kitchen       | Defeats the boss in the finale                                   |
| `paper`   | Kitchen       | Lets you open the safe in the Laboratory                         |
| `energy`  | Laboratory    | Activates the elevator ride to the main exit (finale)            |

Recommended walkthrough for a win:

1. In the Dungeon, collect `map` and `key`.
2. `go west` to the Great Hall.
3. `go west` to the Kitchen, collect `garlic` and `paper`.
4. `go east` back to the Great Hall, then `go south` to the Laboratory.
5. In the Laboratory, take `energy`. The safe only opens if you have `paper`.
6. `go north` to the Great Hall.
7. `go north`. With `energy`, the hero takes the elevator up to the Main entrance.
   - With `garlic`, you kill the boss and win.
   - Without `garlic`, you die.

## Scoring

Once the game ends, your score is:

```
Final score = 100 x (number of collected items)
```

The maximum is 500 points for all 5 items.

## Project structure

```
2d_python_text_game/
├── main.py        # All game logic: room rendering, command parser, inventory, game loop
├── README.md
└── logs.txt       # (created at runtime) a log of all player actions
```

## How it works internally

Key functions in `main.py`:

| Function           | Purpose                                                                      |
|--------------------|------------------------------------------------------------------------------|
| `draw_room(...)`   | Draws the geometry of a room, its doors, label and the hero                   |
| `validation(...)`  | Checks the syntax of the entered command                                      |
| `look(...)`        | Builds the description of the current room and the visible items and doors    |
| `get(...)`         | Item pickup logic with conditions, for example the safe requiring `paper`     |
| `go(...)`          | Movement between rooms, locked-door checks and finale conditions              |
| `view_invent(...)` | Prints the list of items in the inventory                                     |
| `main()`           | Window setup, game loop, logging and scoring                                  |

Game state lives in the `inv` dictionary (inventory) and the `curr_place` variable (current
room).

## Ideas for improvement

- Replace mouse-click waiting with an Enter key handler or a dedicated button.
- Move room and item descriptions into separate data structures, which makes adding
  locations easier.
- Add more rooms, enemies and items.
- Add save and load of progress.
- Cover the logic (`validation`, `get`, `go`) with unit tests.

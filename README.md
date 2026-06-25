# 2D Python Text Game 🏰

A text-and-graphics adventure game written in Python. The player explores a dungeon, collects items, solves puzzles, and tries to escape through the main entrance by defeating a boss. Input is given as text commands, while the room layout is rendered in a window using the `graphics.py` library.

---

## 📑 Table of Contents

- [Features](#-features)
- [Interface](#-interface)
- [Requirements](#-requirements)
- [Installation & Running](#-installation--running)
- [How to Play](#-how-to-play)
- [Commands](#-commands)
- [World Map](#-world-map)
- [Items & Walkthrough Logic](#-items--walkthrough-logic)
- [Scoring](#-scoring)
- [Project Structure](#-project-structure)
- [How It Works Internally](#-how-it-works-internally)
- [Ideas for Improvement](#-ideas-for-improvement)

---

## ✨ Features

- 🗺️ **6 connected rooms**, each with its own geometry and color scheme, rendered through `graphics.py` primitives.
- ⌨️ **Text command parser** with input validation (`look`, `go`, `get`, `view inventory`).
- 🎒 **Inventory** of 5 items that affects available actions and the ending.
- 🔒 **Puzzles and conditions**: locked doors, a safe that only opens with the right item, and a final boss fight.
- 🏆 **Scoring** at the end of the game based on collected items.
- 📝 **Logging** of all player actions to `logs.txt`.
- 🏁 **Two endings** — victory or death — depending on the gear you collected.

---

## 🖼 Interface

The game window (1000 × 500) is split into two parts:

- **Left panel** — command input field, a "Send command" button, a status line (whether the command is valid), the current room description, and messages/inventory.
- **Right panel** — a schematic rendering of the current room: walls, doors (brown), and the hero (a red circle).

> Mouse-click control: the game waits for a **mouse click** inside the window, then reads the text from the input field and executes the command.

---

## 🧰 Requirements

- **Python 3.x**
- The **[`graphics.py`](https://mcsp.wartburg.edu/zelle/python/)** library (John Zelle's graphics library, a wrapper around Tkinter)
- **Tkinter** (usually ships with Python; on Linux it may need to be installed separately)

---

## 🚀 Installation & Running

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

> ⚠️ The file must be named `graphics.py` and be importable (`from graphics import *`).

---

## 🎮 How to Play

1. Run `main.py` — a window opens with the starting room, **Dungeon**.
2. Type a command in the input field on the left.
3. **Click the mouse** anywhere in the window so the game reads and executes the command.
4. Watch the status line: the command is highlighted as *valid* or *invalid*.
5. Collect items, move between rooms, and find your way to the main exit.

---

## ⌨️ Commands

| Command            | Action                                                          | Example           |
|--------------------|-----------------------------------------------------------------|-------------------|
| `look`             | Look around: shows items in the room and available doors        | `look`            |
| `go <direction>`   | Move to an adjacent room (`north`, `south`, `west`, `east`)     | `go west`         |
| `get <item>`       | Pick up an item (`map`, `key`, `garlic`, `paper`, `energy`)     | `get key`         |
| `view inventory`   | Show the contents of your inventory                             | `view inventory`  |

**Input validation rules:**
- A command cannot contain more than two words.
- A single word is only allowed for `look`.
- `go` accepts only the 4 compass directions; `get` only accepts existing items.

---

## 🗺 World Map

```
              [ Main entrance ]   ← exit / finale
                     ↑ north
                 [ Elevator ]
                     ↑ (north when you have energy)
   [ Kitchen ] ←west [ The Great Hall ] east→ [ Dungeon ] (start)
                     ↓ south
               [ Laboratory ]
```

- **Dungeon** — the starting room. The west door to the Great Hall is locked without the key.
- **The Great Hall** — the central hub with four doors.
- **Kitchen / Laboratory / Elevator** — rooms with items and connections.
- **Main entrance** — the final location (the outcome depends on your inventory).

---

## 🎒 Items & Walkthrough Logic

| Item      | Where to find | What it's for                                                    |
|-----------|---------------|------------------------------------------------------------------|
| `map`     | Dungeon       | Score (part of the inventory)                                    |
| `key`     | Dungeon       | Opens the locked west door → into the Great Hall                 |
| `garlic`  | Kitchen       | **Defeats the boss** in the finale                               |
| `paper`   | Kitchen       | Lets you open the safe in the Laboratory                         |
| `energy`  | Laboratory    | Activates the elevator ride to the main exit (finale)            |

**Recommended walkthrough (victory):**

1. In the **Dungeon**, collect `map` and `key`.
2. `go west` → **The Great Hall**.
3. `go west` → **Kitchen**, collect `garlic` and `paper`.
4. `go east` → **The Great Hall**, then `go south` → **Laboratory**.
5. In the **Laboratory**, take `energy` (the safe only opens if you have `paper`).
6. `go north` → **The Great Hall**.
7. `go north` — with `energy`, the hero takes the elevator up to the **Main entrance**.
   - Have `garlic` → **you kill the boss and win! 🎉**
   - No `garlic` → **you die. ☠️**

---

## 🏆 Scoring

Once the game ends, your score is:

```
Final score = 100 × (number of collected items)
```

The maximum is **500 points** for all 5 items.

---

## 📂 Project Structure

```
2d_python_text_game/
├── main.py        # All game logic: room rendering, command parser, inventory, game loop
├── README.md      # This file
└── logs.txt       # (created at runtime) a log of all player actions
```

---

## 🔧 How It Works Internally

Key functions in `main.py`:

| Function           | Purpose                                                                      |
|--------------------|------------------------------------------------------------------------------|
| `draw_room(...)`   | Renders the geometry of a specific room, its doors, label, and the hero       |
| `validation(...)`  | Checks the syntactic correctness of the entered command                       |
| `look(...)`        | Builds the description of the current room and visible items/doors            |
| `get(...)`         | Item pickup logic with conditions (e.g. the safe requires `paper`)            |
| `go(...)`          | Movement between rooms, locked-door checks, and finale conditions             |
| `view_invent(...)` | Prints the list of items in the inventory                                     |
| `main()`           | Window initialization, game loop, logging, and scoring                        |

Game state is stored in the `inv` dictionary (inventory) and the `curr_place` variable (current room).

---

## 💡 Ideas for Improvement

- Replace mouse-click waiting with handling of an Enter key / a dedicated button.
- Move room and item descriptions into separate data structures (simplifies adding new locations).
- Add more rooms, enemies, and items.
- Add save/load of progress.
- Cover the logic (`validation`, `get`, `go`) with unit tests.

---

> An educational project demonstrating how to work with the `graphics.py` library, parse text commands, and model a game world's state in Python.

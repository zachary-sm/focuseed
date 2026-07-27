<p align="center">

  <img src="logo.png" alt="Focuseed logo" width="180">

</p>

# Focuseed

**Focuseed** is a gamified command-line focus timer that helps you stay productive. Complete focus sessions, maintain your daily streak, earn coins, and grow a collection of virtual plants as you build consistent study and work habits.

## Features

- ⏱️ Countdown timers
- ⌚ Stopwatch mode
- 🍅 Built-in Pomodoro timer
- 📊 Focus history and statistics
- 🔥 Daily streak tracking
- 🌱 Virtual plants that grow as you focus
- 🪙 Coin system and in-app shop

## Requirements

- Python 3.12 or later
- `pipx`

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd focuseed
```

### 2. Install `pipx`

If you don't already have `pipx` installed:

**Ubuntu / Debian**

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Restart your terminal if prompted.

For other operating systems, see the official pipx installation guide:
https://pipx.pypa.io/stable/installation/

### 3. Install Focuseed

From the project directory, run:

```bash
pipx install .
```

If you're planning to modify the source code and want changes to be reflected immediately, install it in editable mode instead:

```bash
pipx install --editable .
```

## Getting Started

Display the help menu:

```bash
focuseed --help
```

Start a 25-minute focus session:

```bash
focuseed countdown --minutes 25 --note "Study session"
```

Start a stopwatch:

```bash
focuseed stopwatch
```

Start a Pomodoro session:

```bash
focuseed pomodoro
```

## Available Commands

- `balance`
- `countdown`
- `log`
- `pomodoro`
- `shop`
- `stats`
- `stopwatch`
- `switch`
- `tree`
- `trees`

To view the available options for any command:

```bash
focuseed <command> --help
```

## Updating

If you installed Focuseed in editable mode, update after pulling the latest changes with:

```bash
git pull
pipx reinstall --editable .
```

Otherwise, run:

```bash
pipx reinstall focuseed
```

## Running Tests

```bash
python -m unittest discover -v
```

## Project Structure

```
commands/    CLI command implementations
data/        Application data
tests/       Unit tests
utils/       Shared helper functions
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

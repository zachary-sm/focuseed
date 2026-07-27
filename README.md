<p align="center">

  <img src="logo.png" alt="Focuseed logo" width="180">

</p>

# Focuseed

**Focuseed** is a gamified command-line focus timer that helps you stay productive. Complete focus sessions, maintain your daily streak, earn coins, and grow a collection of virtual plants as you build consistent study and work habits.

# About

The philosophy behind Focuseed's design is to provide a minimalist approach to productivity. By focusing on only the features that directly support productive work and meaningful gamification, Focuseed avoids unnecessary distractions and steep learning curves. The goal is to create an experience that is approachable for new users while remaining efficient for experienced users, allowing them to quickly return to focused work with minimal friction.

## Features

- ⏱️ Countdown timers
- ⌚ Stopwatch mode
- 🍅 Built-in Pomodoro timer
- 📊 Focus history and statistics
- 🌱 Virtual plants that grow as you focus
- 🪙 Coin system and in-app shop

## Technical Decisions

### Command-Line Interface

Focuseed was designed as a command-line application in order to keep it distraction-free and quick to use. Many people often find themselves wandering around on the internet or on their computer with GUI tools, and being a CLI application reduces this urge. In addition, it is more lightweight as a CLI tool and can run more easily on older systems to maximize productivity for the user.

### Python

Python was chosen due to its readability, modularity, and standard language libraries which make it easier for other developers to expand on it in the future or to customize the code for their own use case. Python was also chosen because of its portability. Because it uses an interprerer, it can run on a wider variety of machines than if it was compiled.

### Local-First Design

Keeping it entirely local allows the application to be more lightweight and for the user to focus without worrying about having an internet connection. This also keeps the application lightweight and private so the user feels more compelled to use the app to focus without fearing others may see it which ties into the central design goal of having as little friction as possible for being productive.

### Gamification System

The gamification features were designed to encourage consistency without distracting from the main purpose of the application. They were kept as intuitive and unobtrusive as possible while still encouraging the user to be productive. Features such as streaks, coins, and virtual plants provide users with visible progress and motivation while keeping focus sessions simple. The user has to go out of their way to view their stats in the gamified features, so they are also easy to ignore if a user would prefer not to use them.

### Minimal Feature Set

Each feature in Focuseed was chosen based on whether it directly supports productive work or user engagement. The amount of commands chosen is the sweet spot where there are enough to cover a broad range of productivity functions but few enough to not get in the way of focus or the scope of the app. Avoiding unnecessary functionality keeps the application easy to learn while allowing experienced users to quickly return to a focus session without worrying about clicking through several interfaces.

### Local Data Storage

Focuseed uses JSON files to store user progress, statistics, and game data. Since the application is designed for individual users and does not require complex data relationships, JSON provides a lightweight and human-readable solution without introducing unnecessary database complexity.

That implementation keeps the application easy to set up, portable, and simple to maintain while still allowing user data to persist between sessions.

### Project Structure

The project is organized into separate modules for commands, utilities, application data, and tests. This separation keeps responsibilities clear, improves maintainability, and makes future changes easier to implement.

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

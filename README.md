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

## Command-Line Interface

Focuseed was designed as a command-line application to provide a simple, distraction-free, and efficient interface. By avoiding unnecessary graphical elements and menus, the application reduces distractions within the tool itself and allows users to quickly start and manage focus sessions. A CLI design also keeps the application lightweight and makes it easier to run on a wider range of systems, including older hardware.

## Python

Python was chosen because of its readability, modularity, and extensive standard libraries, which make the application easier for other developers to understand, modify, and extend in the future. Python's large ecosystem also provides access to many existing tools and libraries that support development.

Python was also selected because of its portability. Since Python applications run through an interpreter, Focuseed can operate across different platforms as long as a compatible Python environment is available.

## Local-First Design

Focuseed follows a local-first design approach, meaning that the application does not depend on external servers or an internet connection for its core functionality. This allows users to access their productivity tools reliably while keeping their data stored locally.

Storing data locally also improves privacy by reducing the need to transmit personal productivity information to external services. This supports the application's goal of minimizing friction and allowing users to focus without concerns about unnecessary data sharing.

## Gamification System

The gamification features in Focuseed were designed to provide optional motivation and visible progress without interfering with the main focus workflow. Features such as streaks, coins, and virtual plants give users feedback on their consistency and progress while keeping focus sessions simple.

The gamification system is intentionally unobtrusive. Users can choose to interact with these features when they want additional motivation, while users who prefer a minimal experience can continue using the core focus functionality without relying on them.

## Minimal Feature Set

Each feature in Focuseed was selected based on whether it directly supports productivity or improves user engagement. The number of commands was intentionally limited to provide useful functionality while avoiding unnecessary complexity.

By maintaining a focused feature set, the application remains easier to learn and allows users to quickly return to their work without navigating through excessive menus or options.

## Local Data Storage

Focuseed uses JSON files to store user progress, statistics, and gamification data. Since the application is designed for individual users and does not require complex relationships between large amounts of data, JSON provides a lightweight and human-readable storage solution. It also allows the user to easily edit their save manually if it fits their usage.

This approach allows user data to persist between sessions while keeping the application simple to set up, portable, easy to maintain.

## Project Structure

The project is organized into separate modules for commands, utilities, application data, and tests. This separation keeps different responsibilities organized and improves maintainability.

A modular structure also makes future development easier by allowing individual components to be updated or expanded without requiring major changes throughout the entire application.
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

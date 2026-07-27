<p align="center">

  <img src="logo.png" alt="Focuseed logo" width="180">

</p>

# focuseed

A gamified CLI focus app. Create focus countdowns/stopwatches, view history, keep your streak going, and buy plants that grow when you focus.

## Installation

Focuseed requires Python 3.12 or later and has no third-party dependencies.

From a cloned repository, install it with:

```bash
python -m pip install .
```

Then run:

```bash
focuseed --help
```

For example, start a 25-minute countdown with:

```bash
focuseed countdown --minutes 25 --note "Study session"
```

Available commands include `stopwatch`, `countdown`, `pomodoro`, `log`,
`stats`, `shop`, `trees`, `tree`, `switch`, and `balance`.

To run the unit tests:

```bash
python -m unittest discover -v
```

## Project Structure

commands/ - CLI commands
utils/ - Helper functions shared across multiple areas
data/ - Saved study data
tests/ - Unit tests

## License

This project is licensed under the MIT License. See the LICENSE file for details.

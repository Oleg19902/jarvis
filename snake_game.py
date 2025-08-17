"""Simple terminal Snake game.

This module provides :class:`SnakeGame` for programmatic interaction
and a `play` function for interactive terminal play using `curses`.
"""

from __future__ import annotations

import curses
import random
from collections import deque
from dataclasses import dataclass
from typing import Deque, Iterable, Tuple


Direction = Tuple[int, int]


UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)


@dataclass
class SnakeGame:
    """Basic snake game logic.

    The game board is a rectangle of ``height`` rows and ``width`` columns.
    ``step`` advances the game by one tick.  The snake moves in the current
    direction and grows when it eats food.  Collisions with walls or the
    snake's own body end the game.
    """

    height: int = 20
    width: int = 20

    def __post_init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        center = (self.height // 2, self.width // 2)
        self.snake: Deque[Tuple[int, int]] = deque([center])
        self.direction: Direction = RIGHT
        self.food = self._random_free_cell()
        self.game_over = False

    def _random_free_cell(self) -> Tuple[int, int]:
        free = {
            (r, c)
            for r in range(self.height)
            for c in range(self.width)
        } - set(self.snake)
        return random.choice(list(free))

    def change_direction(self, direction: Direction) -> None:
        """Change movement direction unless opposite of current."""
        opp = (-self.direction[0], -self.direction[1])
        if direction != opp:
            self.direction = direction

    def step(self) -> None:
        """Advance the game by one tick."""
        if self.game_over:
            return

        head_r, head_c = self.snake[0]
        dr, dc = self.direction
        new_head = (head_r + dr, head_c + dc)

        r, c = new_head
        if not (0 <= r < self.height and 0 <= c < self.width):
            self.game_over = True
            return
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.appendleft(new_head)

        if new_head == self.food:
            self.food = self._random_free_cell()
        else:
            self.snake.pop()

    def render(self) -> Iterable[str]:
        """Return an iterable of strings representing the board."""
        board = [[" "] * self.width for _ in range(self.height)]
        for r, c in self.snake:
            board[r][c] = "O"
        fr, fc = self.food
        board[fr][fc] = "*"
        for row in board:
            yield "".join(row)


def play(game: SnakeGame | None = None) -> None:
    """Play snake in the terminal using ``curses``."""
    game = game or SnakeGame()

    def _main(stdscr: "curses._CursesWindow") -> None:
        curses.curs_set(0)
        stdscr.nodelay(True)
        while not game.game_over:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                game.change_direction(UP)
            elif key == curses.KEY_DOWN:
                game.change_direction(DOWN)
            elif key == curses.KEY_LEFT:
                game.change_direction(LEFT)
            elif key == curses.KEY_RIGHT:
                game.change_direction(RIGHT)
            game.step()
            stdscr.clear()
            for row in game.render():
                stdscr.addstr(row + "\n")
            stdscr.refresh()
            curses.napms(100)
        stdscr.addstr("Game over! Press any key to exit.")
        stdscr.nodelay(False)
        stdscr.getch()

    curses.wrapper(_main)


if __name__ == "__main__":
    play()

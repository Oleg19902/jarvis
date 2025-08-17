"""Tests for the :mod:`snake_game` module."""

import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from snake_game import SnakeGame, RIGHT


def run_steps(game, direction, steps):
    game.change_direction(direction)
    for _ in range(steps):
        game.step()


def test_snake_grows_when_eating_food():
    game = SnakeGame(height=5, width=5)
    # Place food directly in front of the snake
    head_r, head_c = game.snake[0]
    game.food = (head_r, head_c + 1)
    run_steps(game, RIGHT, 1)
    assert len(game.snake) == 2
    assert not game.game_over


def test_collision_with_wall():
    game = SnakeGame(height=3, width=3)
    # Move right until collision
    for _ in range(3):
        game.step()
    assert game.game_over

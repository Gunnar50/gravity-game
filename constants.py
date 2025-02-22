# Colours (r, g, b)
import enum

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
COLOURS = [GREEN, BLUE, YELLOW]

# Game settings
TOP_MARGIN = 50
WIDTH = 820
HEIGHT = 600 + TOP_MARGIN
MARGIN_X = 100
MARGIN_Y = 110
NUM_LANES = 5
FPS = 60
TITLE = 'EUREKA!'
BGCOLOUR = DARKGREY


class GameState(enum.Enum):
  MAIN_MENU = 'main_menu'
  IN_GAME = 'in_game'
  GAME_OVER = 'game_over'

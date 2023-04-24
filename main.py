import pygame, sys
from pygame.locals import QUIT
import random

SIZE = 90
COLUMNS = 3

pygame.init()
screen = pygame.display.set_mode((900, 800))

def create_cards():
    result = []
    for i in range(6):
      card = pygame.image.load(f"card{i}.jfif")
      size = (SIZE, SIZE)
      card = pygame.transform.scale(card, size)
      result.append(card)
    return 2 * result

cards = create_cards() 
random.shuffle(cards)
reversed = [] # [5, 6]
finished = []



# 0 ..... 5/blue theme is best

def pos_to_index(pos):
    (x, y) = pos
    row = y // (SIZE+5)
    column = x // (SIZE+5)
    idx = row * COLUMNS + column
    print(f"{x}, {y} -> {idx}")
    return idx

def draw_card(idx):
    row = idx // COLUMNS
    column = idx % COLUMNS
    pos = (column * (SIZE+5), row * (SIZE+5))
    screen.blit(cards[idx], pos)
    #cover-cover
    rect = (pos, (SIZE, SIZE))
    color = (40, 40, 40)
    if idx in finished:
      ...
    elif idx in reversed:
      ...
    else:
      pygame.draw.rect(screen, color, rect)
  
def draw_game():
  screen.fill(background)
  for i in range(len(cards)):
      draw_card(i)
  pygame.display.update()

def wait_event():
  global running
  global reversed
  event = pygame.event.wait()
  if event.type == pygame.QUIT:
      running = False
  elif event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      idx = pos_to_index(pos)
      if idx < 12:
        if len(reversed) == 0:
            reversed.append(idx)
        elif len(reversed) == 1:
            if idx not in reversed:
              reversed.append(idx)
              #  reversed = [5, 6]
              print("???")
              if cards[reversed[0]] is cards[reversed[1]]:
                finished.append(reversed[0])
                finished.append(reversed[1])
                reversed = []
        else:
            reversed = []
  
def run():
  pygame.display.set_caption('Find the Aircraft pairs')
  while running:
      draw_game()
      wait_event()

running = True
background = (1, 2, 255)
  
run()

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
click_inicial = (0, 0)
first_click = False
click_final = (0, 0)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      click_inicial = pygame.mouse.get_pos()
      first_click = True
    if event.type == pygame.MOUSEBUTTONDOWN and first_click:
      click_final = pygame.mouse.get_pos()
      first_click = False

  screen.fill('Red')
  pygame.draw.line(screen, 'Gold', click_inicial, pygame.mouse.get_pos(), 10)
  
  pygame.display.update()
  clock.tick(60)
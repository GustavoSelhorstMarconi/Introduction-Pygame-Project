import pygame, math
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
circle = pygame.image.load('circle.png')
rect = circle.get_rect(center = (225, 225))
i = 0
while True:
  screen.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  i += 0.5
  screen.blit(circle, rect)
  rect.x += math.cos(i) * 2
  rect.y -= math.sin(i) * 2
  pygame.display.update()
  clock.tick(60)
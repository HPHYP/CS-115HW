import pygame

# init pygame

pygame.init()

# window dimensions

width = 600
height = 400
screen = pygame.display.set_mode((width,height))

# set window title

pygame.display.set_caption("snake")

# fps

clock = pygame.time.Clock()
dt = 0
speed = 10

# game loop

running = True
while running: 
  # Handle events 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  #update our game state

  # draw to our screen

# clear screen

  screen.fill("White")

  # draw rectangle
  # road 1
  pygame.draw.rect(
    screen, 
    
    (128,128,128), 
    pygame.Rect((0,270), (800, 50))
  )
  # road 2
  pygame.draw.rect(
    screen, 

    (128,128,128), 
    pygame.Rect((0,170), (800, 50))
  )
  # road 3
  pygame.draw.rect(
    screen, 

    (128,128,128), 
    pygame.Rect((0,70), (800, 50))
  )
  # draw frog
  pygame.draw.circle(screen, "green", (300,360), 30)

 # car 1
  pygame.draw.rect(
    screen, 

    "red", 
    pygame.Rect((3,70), (70, 40))
  )
# car 2
  pygame.draw.rect(
    screen, 

    "blue", 
    pygame.Rect((3,170), (70, 40))
  )
# car 3
  pygame.draw.rect(
    screen, 

    "yellow", 
    pygame.Rect((3,270), (70, 40))
  )
  # update screen
  
 
  
  pygame.display.flip()
  
  # fps
  
  dt = clock.tick(speed)/1000

# quit pygame

pygame.quit()

import sys
import pygame
from setting1 import Settings
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    bg_color = (230, 230, 230)
    ship = Ship(screen)
#
    while True:
 
        for event in pygame.event.get():
       
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)     

        pygame.display.flip()
run_game()
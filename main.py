import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
from player import Player

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    
    while True:
        log_state()
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill(("black"))
        player.draw(screen)

        player.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Calculate delta time in seconds
        # print(f"Delta time: {dt} seconds")
    

if __name__ == "__main__":
    main()
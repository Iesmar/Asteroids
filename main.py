import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shots

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shots.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField() # creating the astroid field.
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2) # creating the player in the middle of the screen.
    

    while True:
        log_state()
            
        for event in pygame.event.get(): # handling events, such as quitting the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill(("black")) # make screen black
        
        for draw in drawable:   # drawing all drawable objects.
            draw.draw(screen)

        updatable.update(dt)    # updating all updatable objects.

        for asteroid in asteroids: # checking for collision between player and asteroids.
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids: # checking for collision between shots and asteroids.
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Calculate delta time in seconds
        # print(f"Delta time: {dt} seconds")
    

if __name__ == "__main__":
    main()
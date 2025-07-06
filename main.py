# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #init
    pygame.init()
    pygame.font.init()
    

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Groups for the containers  
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #setting up life
    hp = PLAYER_LIFE

    #setting timer between hits
    last_hit_time = 0
    

    # Set up the font object
    font = pygame.font.Font(None, 36)
    

    #Game loop
    while True:


        #to close window when clicking the x instead of doinc CTRL+C in CLI
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        current_time = pygame.time.get_ticks()

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if current_time - last_hit_time > HIT_COOLDOWN:
                    hp -= 1 
                    last_hit_time = current_time
                    if hp == 0:
                        print("Game over !")
                        sys.exit()                    
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        # Draw the score to the lifes
        hp_text = font.render(f'Score: {hp}', True, (255, 255, 255))
        screen.blit(hp_text, (10, 10))

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000
   



if __name__ == "__main__":
    main()

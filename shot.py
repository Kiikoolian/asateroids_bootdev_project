from circleshape import *
from constants import *


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    #We override draw by redifining it here   
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    #We override update by redifining it here 
    def update(self, dt):
        self.position += self.velocity * dt
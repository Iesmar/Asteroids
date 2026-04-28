import pygame
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, LINE_WIDTH
from circleshape import CircleShape
from shot import Shots

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_cooldown = 0

    def move(self, dt): # moving the player in direction they are facing, using rotation and speed.
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector   

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def shoot(self): # creating a bullet and giving it velocity and speed.
        if self.shoot_cooldown > 0: # check if cooldown is 0, if not, return.
            return
        else:
            bullet = Shots(self.position.x, self.position.y, SHOT_RADIUS)
            unit_vector_shot = pygame.Vector2(0, 1)
            rotated_unit_vector_shot = unit_vector_shot.rotate(self.rotation)
            rotated_unit_vector_shot_with_speed = rotated_unit_vector_shot * PLAYER_SHOOT_SPEED
            bullet.velocity += rotated_unit_vector_shot_with_speed
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS


    
    def update(self, dt):   # this is where we will handle input and movement

        if self.shoot_cooldown > 0:  # this is where we will handle the shoot cooldown
            self.shoot_cooldown -= dt

        keys = pygame.key.get_pressed() # this is where we will handle input

        if keys[pygame.K_a]:
           self.rotate(-dt)
        if keys[pygame.K_d]:
           self.rotate(dt)
        if keys[pygame.K_w]:
           self.move(dt)
        if keys[pygame.K_s]:
           self.move(-dt)
        if keys[pygame.K_SPACE]:
           self.shoot()

    def triangle(self): # defining a player as a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen): # drawing the player as a triangle
        pygame.draw.polygon(screen, ("white"), self.triangle(), LINE_WIDTH)

        


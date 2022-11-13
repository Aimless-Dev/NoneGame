import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self, accion, frames, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load(f"sprites/player/{accion}.png")
        self.sprite = pygame.transform.scale(self.sprite, (x, y))

        self.type = type

        self.current_frame  = 0
        self.frame          = frames
        self.frame_width    = 32
        self.frame_height   = 32
        self.area           = pygame.Rect(0, 0, 5, 5)

    def update(self, screen, x, y):
        if self.current_frame >= self.frame - 1:
            self.current_frame = 0

        else:
            self.current_frame += 1
        self.area.left  = x
        self.area.top = y
        new_area        = pygame.Rect((self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height))
        
        screen.blit(self.sprite.subsurface(new_area), (x, y))
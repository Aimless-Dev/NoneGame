import pygame, sys
from player import Player
class LevelOne:

    def __init__ (self):
        pygame.init()
        pygame.display.set_caption('NoneGame')
        self.screen = pygame.display.set_mode((960, 640))
        self.clock  = pygame.time.Clock()
        self.sprites        = pygame.sprite.Group()
        self.player_idle_r    = Player('Idle_r', 11, 352, 32)
        self.sprites.add(self.player_idle_r)
        self.player_idle_l    = Player('Idle_l', 11, 352, 32)
        self.sprites.add(self.player_idle_l)
        self.player_run_r     = Player('Run_right', 12, 384, 32)
        self.sprites.add(self.player_run_r)
        self.player_run_l     = Player('Run_left', 12, 384, 32)
        self.sprites.add(self.player_run_l)
        self.player_jump_r     = Player('Jump_r', 1, 32, 32)
        self.sprites.add(self.player_jump_r)
        self.player_jump_l     = Player('Jump_l', 1, 32, 32)
        self.sprites.add(self.player_jump_l)
        self.jump = False
        self.salto = 6
        self.speed = 0
        self.pos   = 0 # 0 es derecha y 1 es izquierda
        self.left = False
        self.rigth = True

        self.test_background = pygame.image.load('sprites/backgrounds/MapaUno.png').convert()

    def run(self):
        x = 60
        y = 400
        while True:
            self.screen.blit(self.test_background, [0, 0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if pygame.key.get_pressed()[pygame.K_d] :
                #Corre a la derecha
                self.rigth = True
                self.left = False
                self.player_run_r.update(self.screen, x, y)
                self.speed += 5
                x += 5
                self.pos = 0

            elif pygame.key.get_pressed()[pygame.K_a] :
                #Corre a la izquierda
                self.left = True
                self.rigth = False
                self.player_run_l.update(self.screen, x, y)
                self.speed -= 5
                x -= 5
                self.pos = 1

            elif pygame.key.get_pressed()[pygame.K_w] :
                #Corre a la izquierda
                self.jump = True
                
                if self.rigth is True and self.left is False:
                    self.player_jump_r.update(self.screen, x, y)

                if self.rigth is False and self.left is True:
                    self.player_jump_l.update(self.screen, x, y)

                if pygame.key.get_pressed()[pygame.K_d]:
                    
                    self.player_run_r.update(self.screen, x, y)
                    x += 5 

                if pygame.key.get_pressed()[pygame.K_a]:
                    
                    self.player_run_l.update(self.screen, x, y)
                    x -= 5 
            else:
                #se queda parado
                self.speed = 0
                if self.pos == 0:
                    self.player_idle_r.update(self.screen, x, y)

                if self.pos == 1:
                    self.player_idle_l.update(self.screen, x, y)
                    
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return 

            if self.jump:
                if self.salto >= -6:
                    y -= (self.salto * abs(self.salto)) * 0.5
                    self.salto -= 1
                else:
                    self.salto = 6
                    self.jump = False



            self.clock.tick(15)
            pygame.display.update()
            pygame.display.flip()
